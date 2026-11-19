# Deforma os vértices da cabeça do modelo masculino para seguir os pontos do rosto da foto (thin-plate spline no plano XY).
import json, sys, numpy as np
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lerglb import ler
sys.argv += []  # nada
j, P, UV, J, W, I = ler('/home/user/role-city/modelos/rpm_m.glb')
marcas = json.load(open('marcas.json'))['frontal_660.jpg']; Lm = np.array(marcas)
px = UV * 2048.0                                   # pixel na textura 2048 (head block = canto superior esquerdo)
head_idx = np.where((UV[:, 0] <= 0.5) & (UV[:, 1] <= 0.5))[0]
def pos_mold(x, y, k=6):
    """posição 3D média dos vértices da cabeça mais próximos de um ponto (x,y) da textura"""
    d = np.hypot(px[head_idx, 0] - x, px[head_idx, 1] - y); sel = head_idx[np.argsort(d)[:k]]
    return P[sel].mean(0)
# pontos do molde (textura 2048) e os pontos correspondentes na foto (MediaPipe)
def pt(ids): return Lm[ids].mean(0)
pares = [
    (pt([33, 133]), (410, 315)), (pt([362, 263]), (612, 315)),
    (pt([105, 66, 70]), (420, 288)), (pt([334, 296, 300]), (600, 288)),
    (Lm[2], (512, 432)), (pt([13, 14]), (512, 492)), (Lm[152], (512, 625)),
    (Lm[234], (300, 430)), (Lm[454], (724, 430)), (Lm[10], (512, 200)),
]
Pf = np.array([p for p, _ in pares]); Mt = np.array([m for _, m in pares], float)
# foto -> textura (mesma transformação do encaixe da textura)
X = np.hstack([Pf, np.ones((len(Pf), 1))]); sol, *_ = np.linalg.lstsq(X, Mt, rcond=None)
foto_para_tex = lambda p: np.hstack([p, 1]) @ sol
# pontos de controle: onde estão na malha (x,y) e para onde devem ir (x,y)
src_xy = np.array([pos_mold(x, y)[:2] for _, (x, y) in pares])
# transformação textura -> malha (mínimos quadrados sobre os mesmos pontos de controle)
tm = np.array([[x, y, 1] for _, (x, y) in pares]); Ac, *_ = np.linalg.lstsq(tm, src_xy, rcond=None)
tex_para_malha = lambda q: np.hstack([q, 1]) @ Ac
dst_xy = np.array([tex_para_malha(foto_para_tex(p)) for p, _ in pares])
disp = dst_xy - src_xy
print('deslocamento médio (m):', np.linalg.norm(disp, axis=1).mean().round(4), 'máx:', np.linalg.norm(disp, axis=1).max().round(4))
# thin-plate spline (2D) com regularização
def U(r): return np.where(r > 0, r * r * np.log(r + 1e-12), 0.0)
n = len(src_xy); K = U(np.linalg.norm(src_xy[:, None] - src_xy[None], axis=2)) + 1e-6 * np.eye(n)
Pm = np.hstack([np.ones((n, 1)), src_xy]); Lmat = np.zeros((n + 3, n + 3)); Lmat[:n, :n] = K; Lmat[:n, n:] = Pm; Lmat[n:, :n] = Pm.T
rhs = np.zeros((n + 3, 2)); rhs[:n] = disp
coef = np.linalg.solve(Lmat, rhs)
# aplica nos vértices da região do rosto (cabeça), com queda suave para não mexer no pescoço nem no cabelo de trás
centro = pos_mold(512, 420)[:2]
xy = P[head_idx, :2]
w_ = w_fall = np.exp(-(np.linalg.norm(px[head_idx] - [512, 420], axis=1) / 330.0) ** 2)
d_tps = (U(np.linalg.norm(xy[:, None] - src_xy[None], axis=2)) @ coef[:n]) + np.hstack([np.ones((len(xy), 1)), xy]) @ coef[n:]
dl = d_tps * w_fall[:, None]
np.save('deslocamento.npy', np.hstack([head_idx[:, None], dl]))
json.dump({'idx': head_idx.tolist(), 'd': dl.round(5).tolist()}, open('/home/user/role-city/modelos/rosto_morph_m.json', 'w'))
print('vértices alterados:', (np.abs(dl).sum(1) > 1e-5).sum(), 'de', len(head_idx))
