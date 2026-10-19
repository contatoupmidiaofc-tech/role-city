# Real-ESRGAN x4plus (RRDBNet, BSD-3) rodando em numpy puro, sem torch. Uso: python3 esrgan_np.py pesos.pth entrada.png saida.png
import sys, zipfile, pickle, collections, time
import numpy as np
from PIL import Image

def load_pth(path):
    z = zipfile.ZipFile(path); root = z.namelist()[0].split('/')[0]
    dt = {'FloatStorage': np.float32, 'HalfStorage': np.float16, 'LongStorage': np.int64}
    class U(pickle.Unpickler):
        def find_class(self, mod, name):
            if name == '_rebuild_tensor_v2':
                return lambda st, off, size, stride, *a: np.lib.stride_tricks.as_strided(st[off:], shape=size, strides=[s * st.itemsize for s in stride]).copy()
            if name == 'OrderedDict': return collections.OrderedDict
            if mod.startswith('torch'): return type(name, (), {})
            return super().find_class(mod, name)
        def persistent_load(self, pid):
            _, typ, key, loc, n = pid; nm = typ.__name__ if hasattr(typ, '__name__') else str(typ)
            return np.frombuffer(z.read(f'{root}/data/{key}'), dtype=dt.get(nm, np.float32))
    return U(z.open(f'{root}/data.pkl')).load()

def conv(x, w, b):  # x (C,H,W), w (O,C,3,3)
    C, H, W = x.shape; p = np.pad(x, ((0, 0), (1, 1), (1, 1)))
    cols = np.lib.stride_tricks.sliding_window_view(p, (3, 3), axis=(1, 2))  # C,H,W,3,3
    cols = cols.transpose(1, 2, 0, 3, 4).reshape(H * W, C * 9)
    return (cols @ w.reshape(w.shape[0], -1).T + b).T.reshape(w.shape[0], H, W)

lr = lambda x: np.where(x > 0, x, 0.2 * x)

def net(P, x):
    g = lambda n: (P[n + '.weight'], P[n + '.bias'])
    fea = conv(x, *g('conv_first')); body = fea
    for i in range(23):
        r = body
        for k in (1, 2, 3):
            pre = f'body.{i}.rdb{k}.'; xs = [r]
            for c in range(1, 5): xs.append(lr(conv(np.concatenate(xs), *g(pre + f'conv{c}'))))
            r = conv(np.concatenate(xs), *g(pre + 'conv5')) * 0.2 + r
        body = r * 0.2 + body
    fea = fea + conv(body, *g('conv_body'))
    up = lambda f: f.repeat(2, axis=1).repeat(2, axis=2)
    fea = lr(conv(up(fea), *g('conv_up1'))); fea = lr(conv(up(fea), *g('conv_up2')))
    return conv(lr(conv(fea, *g('conv_hr'))), *g('conv_last'))

def run(P, img, tile=96, pad=12):
    a = np.asarray(img.convert('RGB'), dtype=np.float32).transpose(2, 0, 1) / 255.0
    C, H, W = a.shape; out = np.zeros((3, H * 4, W * 4), np.float32); t0 = time.time(); n = 0; tot = ((H + tile - 1) // tile) * ((W + tile - 1) // tile)
    for y in range(0, H, tile):
        for x in range(0, W, tile):
            y0, x0, y1, x1 = max(0, y - pad), max(0, x - pad), min(H, y + tile + pad), min(W, x + tile + pad)
            o = net(P, a[:, y0:y1, x0:x1])
            ty, tx = (y - y0) * 4, (x - x0) * 4; hh, ww = min(tile, H - y) * 4, min(tile, W - x) * 4
            out[:, y * 4:y * 4 + hh, x * 4:x * 4 + ww] = o[:, ty:ty + hh, tx:tx + ww]; n += 1
            print(f'bloco {n}/{tot} {time.time() - t0:.0f}s', flush=True)
    return Image.fromarray((np.clip(out, 0, 1).transpose(1, 2, 0) * 255 + 0.5).astype(np.uint8))

if __name__ == '__main__':
    sd = load_pth(sys.argv[1]); P = sd.get('params_ema', sd.get('params', sd))
    run(P, Image.open(sys.argv[2])).save(sys.argv[3])
