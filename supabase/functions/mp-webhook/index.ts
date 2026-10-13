// Rolê City: o Mercado Pago avisa aqui quando um pagamento muda de situação.
// Não confia no aviso: busca o pagamento direto na API do Mercado Pago (com o MP_ACCESS_TOKEN) antes de aprovar.
// Os tokens só entram no jogo pela função resgatar_tokens() do banco, uma única vez por pedido.
import { createClient } from 'jsr:@supabase/supabase-js@2';

const ok = () => new Response('ok', { status: 200 });

Deno.serve(async (req) => {
  const mp = Deno.env.get('MP_ACCESS_TOKEN');
  if (!mp) return ok();
  const u = new URL(req.url);
  const body = await req.json().catch(() => ({} as Record<string, unknown>)) as { type?: string; topic?: string; data?: { id?: string | number } };
  const tipo = body.type || body.topic || u.searchParams.get('type') || u.searchParams.get('topic');
  const id = (body.data && body.data.id) || u.searchParams.get('data.id') || u.searchParams.get('id');
  if (!id || (tipo && tipo !== 'payment')) return ok();

  const r = await fetch(`https://api.mercadopago.com/v1/payments/${encodeURIComponent(String(id))}`, { headers: { Authorization: `Bearer ${mp}` } });
  if (!r.ok) return ok();
  const p = await r.json();
  const ref = p.external_reference;
  if (!ref) return ok();

  const admin = createClient(Deno.env.get('SUPABASE_URL')!, Deno.env.get('SUPABASE_SERVICE_ROLE_KEY')!);
  const { data: ped } = await admin.from('pagamentos').select('id,status,valor').eq('id', ref).maybeSingle();
  if (!ped) return ok();

  let status = 'pendente';
  if (p.status === 'approved') status = 'aprovado';
  else if (p.status === 'rejected' || p.status === 'cancelled') status = 'recusado';
  else if (p.status === 'refunded' || p.status === 'charged_back') status = 'estornado';
  if (status === 'aprovado' && (p.currency_id !== 'BRL' || Number(p.transaction_amount) + 0.001 < Number(ped.valor))) status = 'valor_errado';
  if (ped.status === 'aprovado' && status !== 'estornado') return ok(); // aprovado não volta para trás

  await admin.from('pagamentos').update({ status, mp_pagamento: String(id), atualizado: new Date().toISOString() }).eq('id', ref);
  return ok();
});
