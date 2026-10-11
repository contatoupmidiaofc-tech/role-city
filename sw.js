/* Rolê City: permite instalar no celular e abrir mais rápido (guarda modelos e bibliotecas). A página sempre busca a versão nova primeiro. */
const CACHE = 'role-city-v2';
self.addEventListener('install', e => { self.skipWaiting(); e.waitUntil(caches.open(CACHE).then(c => c.addAll(['./', 'manifest.webmanifest', 'icons/icon-192.png']).catch(() => {}))); });
self.addEventListener('activate', e => { e.waitUntil(caches.keys().then(ks => Promise.all(ks.filter(k => k !== CACHE).map(k => caches.delete(k)))).then(() => self.clients.claim())); });
self.addEventListener('fetch', e => {
  const req = e.request; if (req.method !== 'GET') return;
  const url = new URL(req.url);
  if (/supabase\.co$/.test(url.hostname)) return; // dados do jogo online: nunca do cache
  const cdn = /(cdnjs\.cloudflare\.com|cdn\.jsdelivr\.net|unpkg\.com|fonts\.(googleapis|gstatic)\.com)$/.test(url.hostname);
  const heavy = url.origin === location.origin && /\/(modelos|icons)\//.test(url.pathname);
  if (cdn || heavy) { // bibliotecas e modelos 3D: do cache, e baixa se não tiver
    e.respondWith(caches.match(req).then(r => r || fetch(req).then(res => { if (res.ok || res.type === 'opaque') { const cp = res.clone(); caches.open(CACHE).then(c => c.put(req, cp)); } return res; })));
    return;
  }
  if (url.origin === location.origin) { // página: rede primeiro (sempre a versão nova), cache se estiver sem internet
    e.respondWith(fetch(req, { cache: 'no-cache' }).then(res => { if (res.ok) { const cp = res.clone(); caches.open(CACHE).then(c => c.put(req, cp)); } return res; }).catch(() => caches.match(req).then(r => r || caches.match('./'))));
  }
});
