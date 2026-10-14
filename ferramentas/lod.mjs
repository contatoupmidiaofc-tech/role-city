// Gera as versões leves dos personagens (modelos/rpm_*_lod1.bin e _lod2.bin). Uso: npm i meshoptimizer@1.3.0 @gltf-transform/core@4.5.1 @gltf-transform/extensions@4.5.1 && node lod.mjs
import { NodeIO } from '@gltf-transform/core';
import { ALL_EXTENSIONS } from '@gltf-transform/extensions';
import { MeshoptSimplifier } from 'meshoptimizer';
import fs from 'fs';
await MeshoptSimplifier.ready;
const io = new NodeIO().registerExtensions(ALL_EXTENSIONS);
for (const k of ['m', 'f']) {
  const doc = await io.read(`/home/user/role-city/modelos/rpm_${k}.glb`);
  for (const mesh of doc.getRoot().listMeshes()) for (const prim of mesh.listPrimitives()) {
    const mat = prim.getMaterial(); const name = mat ? mat.getName() : '';
    const pos = prim.getAttribute('POSITION').getArray(), idx = prim.getIndices().getArray(), uv = prim.getAttribute('TEXCOORD_0')?.getArray();
    console.log(k, mesh.getName(), name, 'verts', pos.length / 3, 'tris', idx.length / 3);
    if (!/Wolf3D_Avatar/.test(name)) continue;
    const P = new Float32Array(pos), I = new Uint32Array(idx);
    for (const [tag, ratio, err] of [['lod1', 0.35, 0.01], ['lod2', 0.15, 0.03]]) {
      const target = Math.floor(I.length * ratio / 3) * 3;
      const [out, e] = MeshoptSimplifier.simplifyWithAttributes(I, P, 3, new Float32Array(uv), 2, [1.5, 1.5], null, target, err, ['LockBorder']);
      console.log('  ', tag, 'tris', out.length / 3, 'erro', e.toFixed(4));
      fs.writeFileSync(`/home/user/role-city/modelos/rpm_${k}_${tag}.bin`, Buffer.from(new Uint16Array(out).buffer));
    }
  }
}
