import json, struct, numpy as np
def ler(path):
    d = open(path, 'rb').read(); jl = struct.unpack('<I', d[12:16])[0]; j = json.loads(d[20:20 + jl]); binb = d[20 + jl + 8:]
    def acc(i):
        a = j['accessors'][i]; bv = j['bufferViews'][a['bufferView']]; off = bv.get('byteOffset', 0) + a.get('byteOffset', 0)
        comp = {5126: np.float32, 5123: np.uint16, 5125: np.uint32, 5121: np.uint8}[a['componentType']]
        n = {'SCALAR': 1, 'VEC2': 2, 'VEC3': 3, 'VEC4': 4, 'MAT4': 16}[a['type']]
        arr = np.frombuffer(binb, dtype=comp, count=a['count'] * n, offset=off)
        return arr.reshape(a['count'], n) if n > 1 else arr
    prim = j['meshes'][0]['primitives'][0]['attributes']
    P = acc(prim['POSITION']); UV = acc(prim['TEXCOORD_0']); J = acc(prim['JOINTS_0']); W = acc(prim['WEIGHTS_0'])
    I = acc(j['meshes'][0]['primitives'][0]['indices']).reshape(-1, 3)
    return j, P.astype(float), UV.astype(float), J, W.astype(float), I
if __name__ == '__main__':
    j, P, UV, J, W, I = ler('/home/user/role-city/modelos/rpm_m.glb')
    print('verts', len(P), 'tris', len(I), 'uv range', UV.min(0), UV.max(0))
    print('pos range', P.min(0).round(3), P.max(0).round(3))
    # quais vértices estão no bloco da cabeça (uv em [0,0.5]^2)
    head = (UV[:, 0] <= 0.5) & (UV[:, 1] <= 0.5)
    print('vertices da cabeça', head.sum())
