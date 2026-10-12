/* Rolê City: three.js r186 + GLTFLoader + SkeletonUtils num arquivo só, com o mesmo jeito de usar da r147
   (cores e luzes iguais às de antes). Gerado a partir do pacote "three" do npm. */
import * as T from 'three';
import { GLTFLoader } from 'three/addons/loaders/GLTFLoader.js';
import * as SkeletonUtils from 'three/addons/utils/SkeletonUtils.js';
const THREE = Object.assign({}, T, { GLTFLoader, SkeletonUtils: Object.assign({}, SkeletonUtils) });
// encoding (r147) -> colorSpace (atual)
THREE.LinearEncoding = 3000; THREE.sRGBEncoding = 3001;
Object.defineProperty(T.Texture.prototype, 'encoding', { configurable: true, get() { return this.colorSpace === T.SRGBColorSpace ? 3001 : 3000; }, set(v) { this.colorSpace = v === 3001 ? T.SRGBColorSpace : T.NoColorSpace; } });
Object.defineProperty(T.WebGLRenderer.prototype, 'outputEncoding', { configurable: true, get() { return this.outputColorSpace === T.SRGBColorSpace ? 3001 : 3000; }, set(v) { this.outputColorSpace = v === 3001 ? T.SRGBColorSpace : T.LinearSRGBColorSpace; } });
// luzes no modo antigo (intensidade x PI e queda com a distância da r147), para a cidade ficar com a mesma iluminação
{
  const C = T.ShaderChunk; let s = C.lights_pars_begin; const n0 = s.length;
  const rep = (a, b) => { if (!s.includes(a)) console.warn('three compat: trecho não achado', a); s = s.split(a).join(b); };
  rep('vec3 irradiance = ambientLightColor;', 'vec3 irradiance = ambientLightColor * PI;');
  rep('light.color = sunLight.color;', 'light.color = sunLight.color * PI;');
  rep('light.color = directionalLight.color;', 'light.color = directionalLight.color * PI;');
  rep('light.color = pointLight.color;', 'light.color = pointLight.color * PI;');
  rep('light.color = spotLight.color * spotAttenuation;', 'light.color = spotLight.color * spotAttenuation * PI;');
  rep('vec3 irradiance = mix( hemiLight.groundColor, hemiLight.skyColor, hemiDiffuseWeight );', 'vec3 irradiance = mix( hemiLight.groundColor, hemiLight.skyColor, hemiDiffuseWeight ) * PI;');
  s = s.replace(/float getDistanceAttenuation\([^)]*\) \{[\s\S]*?\n\}/, 'float getDistanceAttenuation( const in float lightDistance, const in float cutoffDistance, const in float decayExponent ) {\n\tif ( cutoffDistance > 0.0 && decayExponent > 0.0 ) return pow( saturate( - lightDistance / cutoffDistance + 1.0 ), decayExponent );\n\treturn 1.0;\n}');
  C.lights_pars_begin = s;
}
// a r186 removeu a sombra PCFSoft (e falha ao usar); a PCF nova já é suave
THREE.PCFSoftShadowMap = T.PCFShadowMap;
window.THREE = THREE;
