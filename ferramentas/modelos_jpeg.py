# troca as texturas PNG dos .glb por JPEG (qualidade 95, sem subamostragem de cor); o resto do arquivo fica igual
import json, struct, io, sys
from PIL import Image
def conv(src, dst):
    d = open(src, 'rb').read(); assert d[:4] == b'glTF'
    jl = struct.unpack('<I', d[12:16])[0]; j = json.loads(d[20:20 + jl]); o = 20 + jl
    bl = struct.unpack('<I', d[o:o + 4])[0]; assert d[o + 4:o + 8] == b'BIN\x00'; binb = d[o + 8:o + 8 + bl]
    imgv = {im['bufferView']: i for i, im in enumerate(j['images'])}
    out = bytearray(); views = j['bufferViews']
    for vi, bv in enumerate(views):
        b = binb[bv.get('byteOffset', 0): bv.get('byteOffset', 0) + bv['byteLength']]
        if vi in imgv:
            I = Image.open(io.BytesIO(b)).convert('RGB'); q = io.BytesIO(); I.save(q, 'JPEG', quality=95, subsampling=0, optimize=True); b = q.getvalue()
            j['images'][imgv[vi]]['mimeType'] = 'image/jpeg'
            if 'name' in j['images'][imgv[vi]]: j['images'][imgv[vi]]['name'] = j['images'][imgv[vi]]['name'].replace('.png', '.jpg')
        while len(out) % 4: out.append(0)
        bv['byteOffset'] = len(out); bv['byteLength'] = len(b); out += b
    while len(out) % 4: out.append(0)
    j['buffers'][0]['byteLength'] = len(out)
    js = json.dumps(j, separators=(',', ':')).encode()
    while len(js) % 4: js += b' '
    tot = 12 + 8 + len(js) + 8 + len(out)
    open(dst, 'wb').write(b'glTF' + struct.pack('<II', 2, tot) + struct.pack('<I', len(js)) + b'JSON' + js + struct.pack('<I', len(out)) + b'BIN\x00' + bytes(out))
    print(src, len(d), '->', tot)
for k in 'fm': conv(f'/home/user/role-city/modelos/rpm_{k}.glb', f'rpm_{k}.glb')
