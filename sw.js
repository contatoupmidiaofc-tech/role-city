/* Rolê City: permite instalar no celular e abrir mais rápido (guarda modelos e bibliotecas). A página sempre busca a versão nova primeiro. */
const CACHE = 'role-city-v3';            // cópia da página (para abrir sem internet)
const ASSETS = 'role-city-assets-v1';    // modelos 3D, animações, ícones e bibliotecas: ficam guardados entre as atualizações
self.addEventListener('install', e => { self.skipWaiting(); e.waitUntil(caches.open(CACHE).then(c => c.addAll(['./', 'manifest.webmanifest', 'icons/icon-192.png']).catch(() => {}))); });
// apaga caches antigos (inclusive a role-city-v2, que guardava os modelos pesados de antes)
self.addEventListener('activate', e => { e.waitUntil(caches.keys().then(ks => Promise.all(ks.filter(k => k !== CACHE && k !== ASSETS).map(k => caches.delete(k)))).then(() => self.clients.claim())); });
self.addEventListener('fetch', e => {
  const req = e.request; if (req.method !== 'GET') return;
  const url = new URL(req.url);
  if (/supabase\.co$/.test(url.hostname)) return; // dados do jogo online: nunca do cache
  const cdn = /(cdnjs\.cloudflare\.com|cdn\.jsdelivr\.net|unpkg\.com|fonts\.(googleapis|gstatic)\.com)$/.test(url.hostname);
  const heavy = url.origin === location.origin && /\/(modelos|icons|lib|marca)\//.test(url.pathname);
  if (cdn || heavy) { // bibliotecas e modelos 3D: do cache, e baixa se não tiver
    e.respondWith(caches.match(req).then(r => r || fetch(req).then(res => {
      if (res.ok || res.type === 'opaque') {
        const cp = res.clone();
        caches.open(ASSETS).then(async c => {
          // guarda a versão nova e joga fora as versões velhas do mesmo arquivo (ex.: rpm_f.glb?v=1 quando chega a ?v=2)
          if (heavy) for (const k of await c.keys()) { const u = new URL(k.url); if (u.pathname === url.pathname && u.search !== url.search) c.delete(k); }
          c.put(req, cp);
        });
      }
      return res;
    })));
    return;
  }
  if (url.origin === location.origin) { // página: rede primeiro (sempre a versão nova), cache se estiver sem internet
    e.respondWith(fetch(req, { cache: 'no-cache' }).then(res => { if (res.ok) { const cp = res.clone(); caches.open(CACHE).then(c => c.put(req, cp)); } return res; }).catch(() => caches.match(req).then(r => r || caches.match('./'))));
  }
});
