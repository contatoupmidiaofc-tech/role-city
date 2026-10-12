import * as esbuild from 'esbuild'; import fs from 'fs';
// r147: só o MeshStandardMaterial usava scene.environment; as versões novas passaram a aplicar também no Lambert/Phong
const envFix = { name: 'env-fix', setup(b) { b.onLoad({ filter: /three[\\/]build[\\/]three\.module\.js$/ }, a => {
  let s = fs.readFileSync(a.path, 'utf8'); const k = 'material.isMeshStandardMaterial || material.isMeshLambertMaterial || material.isMeshPhongMaterial'; const n = s.split(k).length - 1;
  if (!n) throw new Error('env-fix: trecho não achado em ' + a.path); console.log('env-fix', a.path.split('/').pop(), n);
  s = s.split(k).join('material.isMeshStandardMaterial');
  // r147 dava erro ao desenhar um material com "textura" inválida (o jogo conserta no catch do safeRender); a nova só quebrava o shader
  const g = 'function getChannel( value ) {'; if (!s.includes(g)) throw new Error('getChannel não achado'); s = s.replace(g, g + " if ( value === undefined ) throw new Error( 'textura inválida' );");
  // r186: a textura de sombra vazia usada nas listas de luzes subia sem o modo de comparação (erro de "sampler" e quadro sem desenho)
  const e = 'const emptyShadowTexture = /*@__PURE__*/ new DepthTexture( 1, 1 );'; if (!s.includes(e)) throw new Error('emptyShadowTexture não achado'); s = s.replace(e, e + ' emptyShadowTexture.compareFunction = LessEqualCompare; emptyShadowTexture.needsUpdate = true;');
  return { contents: s, loader: 'js' }; }); } };
await esbuild.build({ entryPoints: ['entry.js'], bundle: true, minify: true, format: 'iife', target: 'es2019', legalComments: 'none', banner: { js: '/* three.js r186 (+ GLTFLoader, SkeletonUtils) | MIT License | Copyright 2010-2025 three.js authors | https://github.com/mrdoob/three.js/blob/dev/LICENSE | ajustes de compatibilidade do Rolê City: ferramentas/three/ */' }, outfile: 'three-r186.min.js', plugins: [envFix] });

