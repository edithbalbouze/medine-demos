# REGISTRO de demos — ledger de unicidad

Leer ANTES de diseñar cualquier demo nueva: arquetipos, firmas y componentes aquí listados
están QUEMADOS y no se repiten. Actualizar en el MISMO commit de cada demo publicada
(antes del push — ver "Publicar" en la skill `demo-landing`).
Base: `https://edithbalbouze.github.io/medine-demos/<slug>/`

| Negocio | Slug | Paleta | Tipografía / Densidad | Arquetipo | Técnica de firma | Nav / Footer | Tarjetas / CTAs | Fecha | Estado contacto |
|---|---|---|---|---|---|---|---|---|---|
| Laboratorio CETI | `ceti-demo` (repo aparte: `edithbalbouze/ceti-demo`) | Lavanda/rosa pastel `#fbf6fc` `#f6e8fa` `#eee2f1` + coral `#ff6f91` | Sans de sistema, densidad media, base clara | Hero split-grid con tarjeta flotante + pasos "1, 2, 3" | — (sin firma técnica; hero convencional) | Barra sticky clásica con `nav-links` / footer estándar | Tarjetas con sombra suave, CTA píldora | 2026-07-23 | enviado |
| Apamatte (Sophia Antonietta) | `apamatte` | Cereza `#B00434` · amarillo `#F8CB65` · coral `#C43C16` · rosa `#D4778D` · verde `#4E6136` sobre crema `#F7EFE7` — muestreados con PIL de su propio mockup de empaque | Fraunces variable (opsz/wght/SOFT/WONK) + Karla · densidad media con aire · base clara | Caja-vitrina con ventanas troqueladas (bento desigual dentro de un "panel de caja") | Apertura de caja: lazo que se desata + tapa que se levanta + foto enmascarada con la silueta del empaque + wordmark variable que gana peso al abrir | Píldora flotante superior centrada que se contrae al scroll / Footer-póster con display gigante + franja floral SVG propia | Fichas tipo etiqueta de caja con hairlines y chips cuadrados · CTA principal = **sello circular** con texto en trayectoria (eco de su sticker) · botón secundario = subrayado tipográfico | 2026-07-23 | por enviar |

## Notas de unicidad

- Los DIEZ campos de la fila importan: una demo nueva no puede repetir arquetipo, firma,
  nav, footer ni tratamiento de tarjetas de ninguna fila anterior (ejes de unicidad de
  `references/diseno.md` de la skill `demo-landing`).
- Anotar técnicas que se van quemando (ej. si `background-clip:text` ya se usó 2 veces,
  vetarlo) y alternar bases claras/oscuras y densidades entre demos consecutivas.
- **Deuda de contraste:** CETI y Apamatte son las dos de base CLARA. La próxima demo
  debe salir en base oscura (o al menos con un clima radicalmente distinto).
- Técnicas ya usadas en Apamatte y por tanto en cuenta: variable font animada
  (`font-variation-settings`), `mask-image` con SVG data-URI, `:has()`, texto en
  `textPath` circular, IntersectionObserver para reveals. Evitar repetir más de una
  de estas en la siguiente demo.
- La demo de CETI vive en un repo aparte (`edithbalbouze/ceti-demo`, anterior a este
  ledger) pero cuenta como demo previa: su arquetipo, nav, paleta pastel lavanda/rosa y
  sans de sistema están QUEMADOS igual que si estuviera en este repo.
