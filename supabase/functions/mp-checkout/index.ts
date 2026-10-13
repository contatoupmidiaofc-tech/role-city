// Rolê City: cria o pedido de tokens e o link de pagamento do Mercado Pago (Pix ou cartão).
// Segredo necessário (Supabase → Edge Functions → Secrets): MP_ACCESS_TOKEN
import { createClient } from 'jsr:@supabase/supabase-js@2';

// preços definidos aqui no servidor (o navegador só escolhe o pacote)
const PACOTES: Record<string, { t: number; v: number }> = {
  p1: { t: 100, v: 4.90 },
  p2: { t: 550, v: 19.90 },
  p3: { t: 1200, v: 39.90 },
  p4: { t: 3000, v: 89.90 },
};
const SITES = /^(role-city\.pages\.dev|upmidiaoficial1789521775000\.1370262\.meusitehostgator\.com\.br)$/;
const cors = { 'Access-Control-Allow-Origin': '*', 'Access-Control-Allow-Headers': 'authorization, x-client-info, apikey, content-type', 'Access-Control-Allow-Methods': 'POST, OPTIONS' };
const json = (o: unknown, s = 200) => new Response(JSON.stringify(o), { status: s, headers: { ...cors, 'Content-Type': 'application/json' } });

Deno.serve(async (req) => {
  if (req.method === 'OPTIONS') return new Response('ok', { headers: cors });
  const mp = Deno.env.get('MP_ACCESS_TOKEN');
  if (!mp) return json({ erro: 'Os pagamentos ainda não foram configurados.' }, 503);
  const url = Deno.env.get('SUPABASE_URL')!;
  const admin = createClient(url, Deno.env.get('SUPABASE_SERVICE_ROLE_KEY')!);
  const jwt = (req.headers.get('Authorization') || '').replace(/^Bearer\s+/i, '');
  const { data: { user } } = await admin.auth.getUser(jwt);
  if (!user) return json({ erro: 'Entre na sua conta para comprar.' }, 401);

  const { pacote, volta } = await req.json().catch(() => ({}));
  const P = PACOTES[pacote];
  if (!P) return json({ erro: 'Pacote inválido.' }, 400);

  const { data: ped, error } = await admin.from('pagamentos').insert({ user_id: user.id, pacote, tokens: P.t, valor: P.v }).select('id').single();
  if (error || !ped) return json({ erro: 'Não foi possível criar o pedido.' }, 500);

  let back = 'https://role-city.pages.dev/';
  try { const u = new URL(volta); if (u.protocol === 'https:' && SITES.test(u.hostname)) back = u.origin + u.pathname; } catch (_) { /* usa o padrão */ }

  const pref = {
    items: [{ id: pacote, title: `Rolê City · ${P.t} tokens`, quantity: 1, unit_price: P.v, currency_id: 'BRL' }],
    external_reference: ped.id,
    notification_url: `${url}/functions/v1/mp-webhook`,
    back_urls: { success: `${back}?pag=ok`, pending: `${back}?pag=pendente`, failure: `${back}?pag=falhou` },
    auto_return: 'approved',
    statement_descriptor: 'ROLECITY',
    payer: user.email ? { email: user.email } : undefined,
  };
  const r = await fetch('https://api.mercadopago.com/checkout/preferences', {
    method: 'POST',
    headers: { Authorization: `Bearer ${mp}`, 'Content-Type': 'application/json', 'X-Idempotency-Key': ped.id },
    body: JSON.stringify(pref),
  });
  const j = await r.json().catch(() => ({}));
  if (!r.ok || !j.init_point) {
    await admin.from('pagamentos').update({ status: 'erro', atualizado: new Date().toISOString() }).eq('id', ped.id);
    return json({ erro: 'O Mercado Pago não aceitou o pedido. ' + (j.message || r.status) }, 502);
  }
  await admin.from('pagamentos').update({ mp_preferencia: j.id }).eq('id', ped.id);
  return json({ url: j.init_point, pedido: ped.id });
});
