# Monta modelos/rpm_{f,m}_hd.jpg (2048x2048): a textura do corpo aumentada 2x, com o rosto e o cabelo
# aumentados pelo Real-ESRGAN x4plus (BSD-3, github.com/xinntao/Real-ESRGAN) e o resto em Lanczos.
# Uso: baixe RealESRGAN_x4plus.pth (releases v0.1.0 do repositório acima) para esta pasta e rode
#   python3 rosto_hd.py
# A textura de origem é a PNG sem perda que estava no .glb original (commit 667559e).
import json, struct, io, subprocess, os
from PIL import Image
from esrgan_np import load_pth, run

AQUI = os.path.dirname(os.path.abspath(__file__)); RAIZ = os.path.dirname(AQUI)
P = load_pth(os.path.join(AQUI, 'RealESRGAN_x4plus.pth')); P = P.get('params_ema', P)

def textura_original(k):
    d = subprocess.run(['git', '-C', RAIZ, 'show', f'667559e:modelos/rpm_{k}.glb'], capture_output=True, check=True).stdout
    jl = struct.unpack('<I', d[12:16])[0]; j = json.loads(d[20:20 + jl]); binb = d[20 + jl + 8:]
    im = j['images'][j['textures'][j['materials'][0]['pbrMetallicRoughness']['baseColorTexture']['index']]['source']]
    bv = j['bufferViews'][im['bufferView']]; o = bv.get('byteOffset', 0)
    return Image.open(io.BytesIO(binb[o:o + bv['byteLength']])).convert('RGB')

for k in 'fm':
    src = textura_original(k); hd = src.resize((2048, 2048), Image.LANCZOS)
    # (área na textura 1024, com margem para não ter emenda) -> cabeça inteira e bloco do cabelo
    for box in [(0, 0, 528, 528), (752, 880, 1024, 1024)]:
        up = run(P, src.crop(box))  # 4x
        hd.paste(up.resize(((box[2] - box[0]) * 2, (box[3] - box[1]) * 2), Image.LANCZOS), (box[0] * 2, box[1] * 2))
    hd.save(os.path.join(RAIZ, 'modelos', f'rpm_{k}_hd.jpg'), quality=92, subsampling=0, optimize=True)
    print(k, 'ok')
