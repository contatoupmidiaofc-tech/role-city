# Pinta um rosto em estilo de desenho (cel-shading) na cabeça do modelo masculino, com proporções medidas nas fotos.
import numpy as np
from PIL import Image, ImageDraw, ImageFilter
base = Image.open('/home/user/role-city/modelos/rpm_m_hd.jpg').convert('RGB')
W = 2048
skin = np.asarray(base)[1536:1792, 1536:1792].reshape(-1, 3).mean(0)     # tom do corpo
SK = tuple(int(v) for v in skin)
L = Image.new('RGB', (W, W), SK); d = ImageDraw.Draw(L)
def sh(c, f): return tuple(int(max(0, min(255, v * f))) for v in c)
# sombras e luz (cel): contorno do rosto mais escuro, testa e bochechas mais claras
for (cx, cy, rx, ry, f, a) in [(512, 640, 300, 120, 0.82, 1), (330, 430, 60, 150, 0.9, 1), (694, 430, 60, 150, 0.9, 1)]:
    lay = Image.new('RGB', (W, W), sh(SK, f)); m = Image.new('L', (W, W), 0); ImageDraw.Draw(m).ellipse([cx - rx, cy - ry, cx + rx, cy + ry], fill=255)
    L.paste(lay, (0, 0), m.filter(ImageFilter.GaussianBlur(40)))
for (cx, cy) in [(420, 400), (604, 400)]:
    hl = Image.new('RGB', (W, W), sh(SK, 1.12)); m = Image.new('L', (W, W), 0); ImageDraw.Draw(m).ellipse([cx - 70, cy - 40, cx + 70, cy + 40], fill=120)
    L.paste(hl, (0, 0), m.filter(ImageFilter.GaussianBlur(35)))
d = ImageDraw.Draw(L)
# nariz: lado de sombra e base com narinas
d.polygon([(486, 360), (500, 360), (494, 430), (478, 436)], fill=sh(SK, 0.9))
d.ellipse([472, 428, 492, 442], fill=(110, 62, 50)); d.ellipse([532, 428, 552, 442], fill=(110, 62, 50))
d.ellipse([506, 398, 518, 408], fill=sh(SK, 1.2))
# olhos em amêndoa, íris, pupila e brilho
IRIS, PUP = (72, 46, 34), (22, 16, 12)
for (cx, cy) in [(410, 315), (612, 315)]:
    d.ellipse([cx - 40, cy - 17, cx + 40, cy + 17], fill=(236, 226, 218))
    d.ellipse([cx - 18, cy - 17, cx + 18, cy + 17], fill=IRIS)
    d.ellipse([cx - 8, cy - 8, cx + 8, cy + 8], fill=PUP)
    d.ellipse([cx - 9, cy - 9, cx - 3, cy - 3], fill=(255, 255, 255))
    d.arc([cx - 44, cy - 24, cx + 44, cy + 14], 200, 340, fill=(48, 32, 26), width=7)   # pálpebra superior
    d.arc([cx - 40, cy - 18, cx + 40, cy + 18], 20, 160, fill=(170, 120, 100), width=3)  # pálpebra inferior suave
# sobrancelhas (traço grosso que afina)
for pts in [[(356, 300), (410, 288), (470, 282)], [(556, 282), (614, 288), (668, 300)]]:
    for k in range(len(pts) - 1):
        (x0, y0), (x1, y1) = pts[k], pts[k + 1]
        for t in range(0, 40):
            x = x0 + (x1 - x0) * t / 40; y = y0 + (y1 - y0) * t / 40; r = 12 - 6 * t / 40
            d.ellipse([x - r, y - r, x + r, y + r], fill=(36, 25, 22))
# boca: lábios e linha
d.ellipse([430, 474, 594, 506], fill=(176, 100, 90))
d.ellipse([444, 482, 580, 500], fill=(190, 116, 106))
d.line([(440, 492), (512, 496), (584, 492)], fill=(104, 58, 50), width=5)
d.polygon([(468, 452), (512, 462), (556, 452), (556, 466), (512, 468), (468, 466)], fill=(44, 30, 26))  # bigode
# barba (estilo desenho) e contorno do queixo
beard = Image.new('L', (W, W), 0); bd = ImageDraw.Draw(beard)
bd.polygon([(352, 440), (366, 500), (400, 556), (450, 606), (512, 636), (574, 606), (624, 556), (658, 500), (672, 440), (644, 468), (600, 492), (512, 500), (424, 492), (380, 468)], fill=255)
bd.polygon([(470, 452), (512, 462), (554, 452), (560, 470), (512, 466), (464, 470)], fill=255)  # bigode
beard = beard.filter(ImageFilter.GaussianBlur(6))
noise = np.random.default_rng(3).random((W, W)) * 0.4 + 0.6
beard_arr = np.asarray(beard).astype(float) / 255 * noise
L_arr = np.asarray(L).astype(float)
L_arr = L_arr * (1 - beard_arr[..., None] * 0.92) + np.array([40, 26, 22]) * beard_arr[..., None] * 0.92
L = Image.fromarray(L_arr.clip(0, 255).astype(np.uint8))
# suaviza (cel) e mistura com o molde: só no rosto
L = L.filter(ImageFilter.GaussianBlur(1.6))
yy, xx = np.mgrid[0:W, 0:W]
el = np.clip(1 - (((xx - 512) / 300.0) ** 2 + ((yy - 430) / 250.0) ** 2), 0, 1)
bb = np.asarray(base).astype(float); la = np.asarray(L).astype(float)
mask = np.clip(el * 4, 0, 1)
mask = np.array(Image.fromarray((mask * 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(24))).astype(float) / 255
out = bb * (1 - mask[..., None]) + la * mask[..., None]
Image.fromarray(out.clip(0, 255).astype(np.uint8)).save('desenho_m.jpg', quality=92, subsampling=0, optimize=True)
Image.fromarray(out.clip(0, 255).astype(np.uint8)).crop((0, 0, 1024, 1024)).save('desenho_cabeca.png')
print('ok')
