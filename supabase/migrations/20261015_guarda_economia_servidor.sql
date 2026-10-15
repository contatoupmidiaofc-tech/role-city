-- Rolê City: o servidor passa a ser o dono do saldo de tokens e barra saltos impossíveis de dinheiro no save.
alter table public.jogadores
  add column if not exists tokens_srv bigint,
  add column if not exists dinheiro_srv numeric,
  add column if not exists eco_em timestamptz,
  add column if not exists bonus_tok_em timestamptz;

create or replace function public._num(j jsonb, k text) returns numeric
language sql immutable set search_path = public as $$
  select case when jsonb_typeof(j->k) = 'number' and (j->>k)::numeric >= 0 then (j->>k)::numeric else 0 end
$$;

create or replace function public._eh_adm(uid uuid) returns boolean
language sql stable security definer set search_path = public, auth as $$
  select coalesce((select encode(extensions.digest(convert_to(lower(trim(email)), 'UTF8'), 'sha256'), 'hex')
                   = 'e5dbdf40026e65e6db8263242375130d629eebf526f848d00245fc6f188d04d4'
                   from auth.users where id = uid), false)
$$;
revoke all on function public._eh_adm(uuid) from public, anon, authenticated;

-- base: quem já joga mantém o que tem hoje
update public.jogadores set
  tokens_srv = floor(public._num(save, 'tokens'))::bigint,
  dinheiro_srv = public._num(save, 'coins') + public._num(save, 'wallet') + public._num(save, 'bank'),
  eco_em = now()
where tokens_srv is null;

create or replace function public.guarda_economia() returns trigger
language plpgsql security definer set search_path = public as $$
declare
  tok numeric; tot numeric; base_tok numeric; teto_tok numeric; base_din numeric; lim numeric; mins numeric; c numeric;
begin
  if auth.uid() is null then return new; end if; -- painel / funções do servidor
  -- atualização que não mexe no save (ex.: resgatar_tokens somando no saldo oficial) passa direto
  if tg_op = 'UPDATE' and new.save is not distinct from old.save then return new; end if;
  if new.save is null or jsonb_typeof(new.save) <> 'object' then new.save := coalesce(old.save, '{}'::jsonb); end if;
  tok := floor(public._num(new.save, 'tokens'));
  tot := public._num(new.save, 'coins') + public._num(new.save, 'wallet') + public._num(new.save, 'bank');
  if public._eh_adm(auth.uid()) then
    new.tokens_srv := tok; new.dinheiro_srv := tot; new.eco_em := now();
    if tg_op = 'UPDATE' then new.bonus_tok_em := old.bonus_tok_em; end if;
    return new;
  end if;

  if tg_op = 'INSERT' then
    base_tok := (select coalesce(sum(tokens), 0) from public.pagamentos where user_id = new.id and creditado);
    teto_tok := base_tok; base_din := 0; mins := 0; new.bonus_tok_em := null;
  else
    base_tok := coalesce(old.tokens_srv, floor(public._num(old.save, 'tokens')));
    teto_tok := base_tok + case when old.bonus_tok_em is null or old.bonus_tok_em < now() - interval '10 minutes' then 25 else 0 end;
    base_din := coalesce(old.dinheiro_srv, public._num(old.save, 'coins') + public._num(old.save, 'wallet') + public._num(old.save, 'bank'));
    mins := least(60, greatest(0, extract(epoch from now() - coalesce(old.eco_em, old.atualizado_em, now())) / 60));
    new.bonus_tok_em := old.bonus_tok_em;
  end if;

  -- tokens: só sobem por compra aprovada (resgatar_tokens) ou bônus da caixa lendária (25 a cada 10 min)
  if tok > teto_tok then
    tok := base_tok; new.save := jsonb_set(new.save, '{tokens}', to_jsonb(tok));
  elsif tok > base_tok then
    new.bonus_tok_em := now();
  end if;
  new.tokens_srv := tok;

  -- dinheiro: no máximo $ 20 milhões de uma vez + $ 1 milhão por minuto desde o último save (até 1 hora)
  lim := base_din + 20000000 + 1000000 * mins;
  if tot > lim then
    c := greatest(0, public._num(new.save, 'coins') - (tot - lim));
    new.save := jsonb_set(new.save, '{coins}', to_jsonb(floor(c)));
    tot := public._num(new.save, 'coins') + public._num(new.save, 'wallet') + public._num(new.save, 'bank');
  end if;
  new.dinheiro_srv := tot; new.eco_em := now();

  -- nível do ranking não pula mais de 3 por save
  if tg_op = 'UPDATE' then new.nivel := least(coalesce(new.nivel, 1), coalesce(old.nivel, 1) + 3); end if;
  return new;
end $$;
revoke all on function public.guarda_economia() from public, anon, authenticated;

drop trigger if exists guarda_economia on public.jogadores;
create trigger guarda_economia before insert or update on public.jogadores
  for each row execute function public.guarda_economia();

-- compra aprovada: além de marcar como creditada, soma no saldo oficial de tokens
create or replace function public.resgatar_tokens() returns integer
language plpgsql security definer set search_path = public as $$
declare total integer;
begin
  if auth.uid() is null then return 0; end if;
  with r as (
    update public.pagamentos set creditado = true, atualizado = now()
    where user_id = auth.uid() and status = 'aprovado' and not creditado
    returning tokens)
  select coalesce(sum(tokens), 0) into total from r;
  if total > 0 then
    update public.jogadores set tokens_srv = coalesce(tokens_srv, 0) + total where id = auth.uid();
  end if;
  return total;
end $$;
