# REGISTRO de demos — ledger de unicidad

Leer ANTES de diseñar cualquier demo nueva: arquetipos, firmas y componentes aquí listados
están QUEMADOS y no se repiten. Actualizar en el MISMO commit de cada demo publicada
(antes del push — ver "Publicar" en la skill `demo-landing`).
Base: `https://edithbalbouze.github.io/medine-demos/<slug>/`

| Negocio | Slug | Paleta | Tipografía / Densidad | Arquetipo | Técnica de firma | Nav / Footer | Tarjetas / CTAs | Fecha | Estado contacto |
|---|---|---|---|---|---|---|---|---|---|
| Laboratorio CETI · **v1 (opción 1, viva)** | `ceti-demo` raíz (repo aparte: `edithbalbouze/ceti-demo`) | Lavanda/rosa pastel `#fbf6fc` `#f6e8fa` `#eee2f1` + coral `#ff6f91` | Sans de sistema, densidad media, base clara | Hero split-grid con tarjeta flotante + pasos "1, 2, 3" | — (sin firma técnica; hero convencional) | Barra sticky clásica con `nav-links` / footer estándar | Tarjetas con sombra suave, CTA píldora | 2026-07-23 | enviado — se mantiene como opción 1 |
| Laboratorio CETI · **v2 (opción 2, rediseño)** | `ceti-demo/v2/` → `https://edithbalbouze.github.io/ceti-demo/v2/` | Frambuesa real del logo `#A90D57`/`#7C0A41` (muestreada con PIL) + teal clínico `#0C8A81` («en rango») + rosa tint `#FBE7F1` sobre off-white cálido `#F6F5F2`; tinta `#1E1C21` | `Space Grotesk` (display/UI) + `IBM Plex Mono` (datos/eyebrows/rangos) · densidad media-técnica · base clara con un panel oscuro | Panel/expediente de laboratorio: hero-instrumento + **bento** de perfiles con medidores de rango de referencia | **Eje endocrino SVG** (hipotálamo→hipófisis→glándulas) con **señal viajando por `offset-path`** + medidores de rango que animan a «EN RANGO ✓» al revelar | Barra-instrumento fina con índice numérico mono (01·02·03) + chip horario / **footer «pie de informe»** mono oscuro (razón social, RIF, dirección) | Fichas «renglón de informe» con medidor de rango (banda teal) · CTA **rectángulo duro** con sombra sólida `#7C0A41` (sin píldora) · FAB IG cuadrado | 2026-07-24 | segunda opción publicada |
| Dra. Nuramí Rojas · Médico Fisiatra | `nr-medico-fisiatra` | Verde agua muestreado del logo: lienzo `#F3FAFC`, superficies `#C4DDD9`→`#94C0B8`→`#4BA18B`, acento/CTA `#32715C`, tinta `#171B1C`/`#344B46`, pétalos `#CAEAD7`/`#90CFB3`/`#65A98B` (base clara con acto oscuro verde bosque) | `Plus Jakarta Sans` (display 800) + `Cormorant Garamond` itálica (eyebrows/numeración/citas); densidad editorial minimal con mucho aire | Expediente clínico editorial en bandas de pétalo, dos actos, secciones numeradas 01–07 | Line-drawing SVG del loto (stroke-dashoffset) + retrato en clip-path de pétalo + barra `#32715C` de cierre (réplica de su firma de posts) | **Rail lateral vertical fijo** (desktop) → **overlay a pantalla completa** (móvil) / **footer-póster** verde bosque con claim gigante | **Hairlines editoriales** (filas full-width, sin sombra, sin radios) + CTA rectángulo duro `#32715C` + enlaces con subrayado tipográfico | 2026-07-24 | por enviar |
| Amazonas Pole Academy | `amazonas-pole-academy` | Off-white frío `#F0F0F5` + navy `#12487D` + azul de marca `#03569F` + acero `#566E74`; cian `#36D4EB` con tope de 2 usos | Archivo Black + Yellowtail (script) + Jost · densidad media-alta · base clara high-key con UNA sola banda navy (Exotic) | "El tablero de horarios que no existe" — bandas editoriales numeradas 01–06, grilla filtrable como protagonista | **"El asta"** — línea SVG vertical que se dibuja con el scroll y remata en punta de lanza en el footer, con nodos por sección (tomada del asta real del isotipo) | Píldora flotante centrada / footer-póster con display gigante a sangre + barra de contacto azul full-width | Filas full-width con hairlines de 1px, sin sombra · CTA rectangular duro · píldora reservada SOLO a los chips de horario | 2026-07-23 | demo publicada — mensaje **NO enviado** |
| Apamatte (Sophia Antonietta) | `apamatte` | Cereza `#B00434` · amarillo `#F8CB65` · coral `#C43C16` · rosa `#D4778D` · verde `#4E6136` sobre crema `#F7EFE7` — muestreados con PIL de su propio mockup de empaque | Fraunces variable (opsz/wght/SOFT/WONK) + Karla · densidad media con aire · base clara | Caja-vitrina con ventanas troqueladas (bento desigual dentro de un "panel de caja") | Apertura de caja: lazo que se desata + tapa que se levanta + foto enmascarada con la silueta del empaque + wordmark variable que gana peso al abrir | Píldora flotante superior centrada que se contrae al scroll / Footer-póster con display gigante + franja floral SVG propia | Fichas tipo etiqueta de caja con hairlines y chips cuadrados · CTA principal = **sello circular** con texto en trayectoria (eco de su sticker) · botón secundario = subrayado tipográfico | 2026-07-23 | por enviar |

| Nativos CrossFit | `nativoscf` | Negro `#0A0A0A` + carbón `#181818` · **amarillo de marca `#F8C40D`** (acento 10%, mismo color que la pintura real del rig) · blanco `#FBFBFC` · crema `#F3EFE9` (una sola sección) · rojo `#E50629` de alerta — muestreados con PIL del logo y el feed | **Anton** (display, solo mayúsculas) + **Barlow Condensed** (UI/datos) · densidad media-alta industrial · **base OSCURA** | **"La pizarra del box"** — bandas full-width numeradas 01–06 separadas por reglas de 1px amarillas, etiquetas uppercase con tracking; **cero grid de cards** | **Line-drawing SVG del isotipo** (punta de lanza en aro roto) dibujándose con `stroke-dashoffset` y rellenándose al terminar · corte de "barba de lanza" con `clip-path` entre secciones | **Píldora flotante centrada** / **Footer-póster** con display gigante ("CONTÁCTANOS HOY, TE ESPERAMOS") | **Cajas de borde amarillo 1px sobre negro** (calco de cómo maquetan sus horarios en IG) + filas full-width sin cards · CTA principal = rectángulo duro relleno `#F8C40D` texto negro · secundario = subrayado tipográfico amarillo | 2026-07-24 | demo publicada — **mensaje NO enviado** (Edith debe revisar) |
| Dayrrig Duarte (Pure Glow Day) | `pureglowday` | Vino `#701A1B` (dominante) · crema `#DCDDD8` · rojo CTA `#931717` · oro `#A8946B` / `#C9B489` · tinta `#2A1416` — muestreados con PIL de su carrusel "QUIEN SOY" (el vino dio sd=0.0) | **Newsreader** variable (opsz 6–72, roman + itálica en pullquotes; sin animar ejes) + Instrument Sans · densidad editorial alta · **base OSCURA** | Dossier editorial por capítulos numerados (00–04), con bloque de respiro en crema | Swash SVG que se dibuja solo (`stroke-dashoffset`) bajo UNA palabra del H1 — calco de su subrayado a pincel; dialoga con el brochazo real de su foto | **Rail lateral fijo** con índice numerado + hilo de progreso vertical (móvil: barra de progreso de 2px con capítulo activo) / **Colofón editorial**: índice numerado repetido + datos + redes en hairlines | Filas full-width con hairlines de oro y numeración colgada — **cero cards, cero sombras** · CTA principal = rectángulo de esquina dura con filete oro · secundario = subrayado tipográfico | 2026-07-23 | por enviar |
| Amazonas Pole Academy | `amazonas-pole-academy` | **Marca real B&N**: tinta `#14141A` + magenta acento `#C21E63`/`#E0447F` + rosa `#FF7FB0` sobre papel `#F5F4F6` — su logo es blanco y negro puro (muestreado con PIL), el magenta viene de su identidad de app validada por la clienta | **Archivo Black** (display) + **Yellowtail** (script) + cuerpo en sans del sistema · densidad media · base clara con una banda oscura | Bandas numeradas apiladas (01–06) con hero split | Foto del estudio con `mask-image` + reveals scroll-driven + `:has()` para filtros de grilla | Nav en píldora flotante centrada / Footer con datos y sello | Filas y fichas con hairlines; CTA principal = rectángulo relleno magenta, secundario = subrayado | 2026-07-24 | por enviar |
| Centro Integral de Danza (Academia de Ballet CID) | `centro-integral-de-danza` | **Negro `#000` (paga la deuda de contraste)** · blanco `#FFF` · magenta frambuesa `#9A1F53` (muestreado con PIL del script "de Danza" del logo, validado en 3 assets, sd±3) · rosa AA `#E36A93` · gris `#666` · oro `#A97843` solo en palmarés | **Playfair Display** (display alto contraste, roman + itálica) + **Jost** · densidad aireada, escala display bestial · **base oscura** | **Programa de mano de gala** — Actos I–IV con numeración romana, filetes finos y cartel de función; sin `<section class="band">` apiladas | **Cartel de función tipográfico puro (sin foto en el hero)** + **cinta de raso SVG que se dibuja con el scroll** (`stroke-dashoffset`) cosiendo hero y los cuatro actos | **Barra que se auto-oculta al bajar y reaparece al subir + drawer lateral deslizante desde la derecha** (con telón atenuador; NO overlay fullscreen) / **Marquesina** (letrero de marquesina en loop) sobre magenta + línea legal mínima | Fichas de programa con filete y numeración · **flip 3D** en las tarjetas de temporada · CTA principal = **botón-boleto troquelado** (borde perforado + muescas) · secundario = subrayado/enlace | 2026-07-24 | por enviar |
| Dra. Launic Jiménez (@gineco_lau) | `gineco-lau` | Fucsia `#D6157E`/`#FF5CAB` + menta `#3FBF9E` sobre blush `#FFF6FB`/`#FDEBF4` — muestreados de su feed de IG (scrubs magenta/lila + acento fucsia de sus artes) · base **clara** | **Hedvig Letters Serif** (display) + **Hanken Grotesk** (UI/cuerpo) · densidad media aireada | **"Consultorio de bolsillo"** — microsite cálido soft-UI con secciones numeradas 01–05, sin bandas apiladas ni grid de cards genérico | **`background-clip:text`** con relleno de gradiente fucsia→menta animado en palabra display del hero + retrato real en squircle orgánico con halo cónico | **Tab-bar inferior tipo app** (móvil, botón WhatsApp flotante central) → **barra slim superior** (desktop) / **footer = tarjeta-carné de contacto flotante** con filete de marca | **Soft-cards** redondeadas (radios 22–34px) en capas de sombra + **compositor de WhatsApp interactivo** (chips → mensaje en vivo) · CTA principal = píldora WhatsApp verde | 2026-07-24 | por enviar |
| Lcdo. Leonardo Bravo · Nutricionista Dietista | `leonardobravov` | Navy `#031D45` (60% tinta + acto) · blanco `#F5F7F8` (30%) · **verde menta de marca `#30D790`** (10% acento/CTA — su color de firma, el glow real de su feed) — muestreados con PIL de su plantilla "Transforma tu salud" | **Space Grotesk** (display, precisión científica) + **Figtree** (cuerpo) · densidad aireada minimal · **base CLARA con un acto navy** | **Split-screen sincronizado** — panel izquierdo sticky que se va llenando + columna derecha de especialidades (01–04) con scroll-snap; NO bandas apiladas | **Spotlight menta que sigue el cursor** sobre el acto navy con retícula blueprint (recrea el glow de silueta de su marca) + panel sticky que sincroniza la especialidad activa | **Dock inferior tipo tab-bar de app de salud** (Inicio/Áreas/Agendar) + wordmark superior / **Footer-tarjeta flotante** sobre bloque navy | **Pastillas de dato redondeadas + control segmentado** (selector de área + horario que arma un `wa.me` en vivo) · CTA píldora menta ancha con icono · secundario ghost | 2026-07-24 | demo publicada — **mensaje NO enviado** (Edith revisa ciudad + entrega del WhatsApp) |
| Donde Patricio (Beer &amp; Food) | `dondepatricio` | Verde `#3D7038` · verde vivo `#4D9146` · verde claro `#87B870` · dorado `#CB9C34` · azul noche `#475691` · arena `#D0C184` sobre casi-negro `#0F1410` — muestreados con PIL del logo real (insignia del duende) | Bricolage Grotesque variable (`wdth` 76–100) + DM Sans · **densa** · **base oscura** | **Menú-mural nocturno**: bento asimétrico de conceptos + carta en filas de líder punteado + banda full-bleed de la orilla. Sin una sola `<section class="band">` apilada | **Interruptor Día/Noche que reescribe la página**: se autoselecciona con la hora real del visitante (11:30–19h = día) y cambia foto del hero, duotono, acento, copy y las líneas de la carta | **Wordmark suelto sin barra + overlay a pantalla completa** (verde, tipografía display gigante numerada) / **Footer-póster** con display gigante + marquee de contacto | **Filas de carta con líder punteado** (sin cards) — cada fila abre un wa.me con la pregunta escrita · CTA principal = **sello circular** «Abrir en el mapa» · CTA secundario = rectángulo duro | 2026-07-23 | por enviar |

## Notas de unicidad

- Los DIEZ campos de la fila importan: una demo nueva no puede repetir arquetipo, firma,
  nav, footer ni tratamiento de tarjetas de ninguna fila anterior (ejes de unicidad de
  `references/diseno.md` de la skill `demo-landing`).
- Anotar técnicas que se van quemando (ej. si `background-clip:text` ya se usó 2 veces,
  vetarlo) y alternar bases claras/oscuras y densidades entre demos consecutivas.
- ⚠️ **Filas retroactivas (2026-07-23):** las 4 últimas filas se reconstruyeron leyendo el
  HTML publicado porque se publicaron SIN registrarse. Ese fue el fallo que hizo que varias
  demos se parecieran: sin ledger, cada constructor creía que nada estaba quemado. Completar
  los campos `_(reconstruir)_` la próxima vez que se toque cada demo.

- 🚫 **QUEMADO — no repetir:**
  - **Andamiaje de "bandas"** (`<section class="band...">` apiladas): usado en **4 de 5**
    demos. La próxima NO puede ser bandas apiladas — usar bento, scroll horizontal,
    split-screen, capítulos sticky, póster de una pantalla, etc.
  - **Fraunces**: 1 uso real (Apamatte). Se mantiene **vetada** — es la display por defecto a
    la que tiende todo constructor.
  - **Bodoni Moda**: probada en Pure Glow Day y descartada — la clienta la halló difícil de
    leer (Didone de contraste extremo: los trazos finos se pierden en pantalla). Evitar
    Didones puras para textos largos o sobre fondo de color.
  - **Newsreader**: 1 uso (Pure Glow Day) — serif editorial de óptica variable, legible; la
    reemplazó.
  - Anton, Barlow Condensed, Archivo Black, Jost, Yellowtail, Instrument Sans, Karla,
    Playfair Display: usadas una vez cada una (Playfair estrena en Centro Integral de Danza).
  - Máximo **2 familias** por demo (Amazonas usó 3 — incumple el BRIEF-COMUN).
  - **`stroke-dashoffset` (SVG line-drawing)**: 2 usos (Pure Glow Day = swash bajo el H1;
    Centro Integral de Danza = cinta de raso que cose los actos) → **VETADO** para la próxima.
  - **Overlay/menú a pantalla completa**: usado en Donde Patricio → evitar. Centro Integral de
    Danza usó **drawer lateral + barra auto-oculta** en su lugar.

- **Deuda de contraste / alternancia:** el orden reciente fue Apamatte (clara) → Amazonas
  (clara) → **Centro Integral de Danza (OSCURA, 2026-07-24)**. La próxima **vuelve a base clara**
  y no puede ser negra editorial.
- Técnicas ya usadas en Apamatte y por tanto en cuenta: variable font animada
  (`font-variation-settings`), `mask-image` con SVG data-URI, `:has()`, texto en
  `textPath` circular, IntersectionObserver para reveals. Evitar repetir más de una
  de estas en la siguiente demo.
- Técnicas de Donde Patricio (cuentan 1 uso cada una): **scroll-driven animations**
  (`animation-timeline: view()` para reveals + `scroll(root)` para la barra de progreso,
  con fallback rAF y sin IntersectionObserver), **duotono con `background-blend-mode:
  luminosity`** + realce `color-dodge`, **`clip-path`/ola SVG animada con `d:path()`**,
  y el patrón **tema conmutable por `data-turno` en `<html>`** (sin `:has()`).
- ⚠️ `:has()` va por **1 uso real** (Apamatte). La fila retroactiva se lo atribuía también a
  Pure Glow Day, pero esa demo lo eliminó en la reconstrucción: hoy el antes/después conmuta
  con un toggle JS de `aria-pressed`. Se mantiene **vetado** igualmente.
- `IntersectionObserver` queda **prohibido como efecto principal**; se acepta solo como
  *fallback* de un scroll-driven timeline o como plomería (capítulo activo de un nav). Así
  está en Pure Glow Day.
- Técnicas de Pure Glow Day (1 uso cada una): **line-drawing SVG con `stroke-dashoffset`**
  (el swash del hero) y **duotono con `mix-blend-mode: luminosity`** sobre base de color.
  ⚠️ Coincide con Donde Patricio en *scroll-driven animations* y en la idea de duotono
  (allí con `background-blend-mode`) — ambas se publicaron el mismo día en paralelo, sin
  verse. No afecta al parecido visual (son técnicas invisibles para el prospecto: los dos
  sitios no se parecen en nada), pero **scroll-driven animations queda ya en 2 usos →
  vetado** para la próxima, que debe buscar otro motor de reveal.
- Contadores de tipografía tras Donde Patricio: Bricolage Grotesque y DM Sans, 1 uso cada una.
- La demo de CETI vive en un repo aparte (`edithbalbouze/ceti-demo`, anterior a este
  ledger) pero cuenta como demo previa: su arquetipo, nav, paleta pastel lavanda/rosa y
  sans de sistema están QUEMADOS igual que si estuviera en este repo.
- ⚠️ **NR Médico Fisiatra (2026-07-24) — colisión de ola paralela.** Su brief se despachó
  antes de que existieran los vetos de arriba, así que reincide sin verlos en tres técnicas
  ya quemadas: **line-drawing SVG `stroke-dashoffset`** (2º uso tras Pure Glow Day → ahora
  **vetada de verdad**), **`:has()`** (2º uso tras Apamatte, seguía vetado) y **scroll-driven
  `animation-timeline: view()`** (3er uso). No afecta al parecido *visual* (rail lateral +
  clip-path de pétalo + expediente clínico verde agua no se parecen a ninguna otra demo —
  igual que la coincidencia Pure Glow Day/Donde Patricio, son técnicas invisibles para el
  prospecto). Lección: en una ola paralela, congelar el estado del ledger y repartir técnicas
  ANTES de lanzar los constructores. Contadores tras esta demo: `stroke-dashoffset` 2 · `:has()`
  2 · scroll-driven 3 — las tres **vetadas**. Tipografías: `Plus Jakarta Sans` y `Cormorant
  Garamond`, 1 uso cada una. **Rail lateral** ahora en 2 usos (Pure Glow Day + esta) → la
  próxima usa otro nav (píldora ya en 2, así que: hamburguesa-overlay, wordmark suelto o
  nav-que-aparece-al-subir). Base clara: van CETI, Apamatte, Amazonas y esta → **toca oscura**.

### Técnicas quemadas (contador)

| Técnica | Usos | Estado |
|---|---|---|
| Scroll-driven animation (`animation-timeline: scroll()`/`view()`) | 2 (Amazonas, Pure Glow Day + Donde Patricio) | **vetado** |
| `:has()` (filtros/estado sin JS) | **2** (Apamatte, **Nativos**) | **vetado** — reincidencia, ver gotcha 2026-07-24 |
| Line-drawing SVG (`stroke-dashoffset`) | **2** (Pure Glow Day, **Nativos**) | **vetado** para la próxima |
| `clip-path` animado / troquelado | **2** (Donde Patricio, **Nativos**) | **vetado** para la próxima |
| IntersectionObserver como reveal principal | **1** (**Nativos**) | **prohibido** — solo fallback/plomería (ya estaba en la norma) |
| `mask-image` con gradiente sobre foto | 1 (Amazonas) | libre |
| Foto real del local como hero | 1 (Amazonas) | libre — pero variar el tratamiento |
| Cursor spotlight (glow radial que sigue el puntero) | 1 (**Leonardo Bravo**) | libre — 1 uso |
| Split-screen sincronizado + `scroll-snap` (panel sticky que sigue la sección activa) | 1 (**Leonardo Bravo**) | libre — 1 uso; el reveal es rect-based en scroll (no IO como efecto principal) |
| Control segmentado que arma un `wa.me` en vivo | 1 (**Leonardo Bravo**) | libre — 1 uso |
| Dock inferior tipo tab-bar (nav) | 1 (**Leonardo Bravo**) | libre — 1 uso |
| Footer-tarjeta flotante sobre bloque de marca | 1 (**Leonardo Bravo**) | libre — 1 uso |

Dos bases claras seguidas (CETI y Amazonas). **La próxima demo va en base oscura**, salvo
que la marca del negocio lo prohíba de plano.

Contador de bases tras Nativos (base oscura, 2026-07-24): oscura ya van varias seguidas
(Pure Glow Day, Donde Patricio, Nativos) → **la próxima demo debe ir en base clara** salvo
que la marca la prohíba.

Tras **Leonardo Bravo** (2026-07-24, **base CLARA con un acto navy** — cumple la alternancia
sin traicionar su marca navy-dominante): la próxima demo **puede volver a base oscura**.
Tipografías: `Space Grotesk` y `Figtree`, 1 uso cada una. Nav **dock inferior** y **footer-
tarjeta flotante** estrenan (1 uso). Ninguna técnica vetada se usó: el reveal es rect-based en
scroll (no `animation-timeline`, no IO como efecto principal), sin `:has()`, sin
`stroke-dashoffset`, sin `clip-path` animado, sin bandas apiladas.

### Gotcha de proceso (2026-07-24) — construir contra el ledger REAL, no el bootstrap

La demo de **Nativos** repitió `:has()` (vetado), line-drawing SVG y `clip-path` porque su
brief se diseñó contra una copia local recién bootstrapeada de `REGISTRO.md` (la plantilla
vacía de la skill), sin ver este ledger compartido —el repo `medine-demos` ya existía en
remoto con seis demos y un proceso concurrente lo estaba sincronizando. **Antes de escribir
el brief de una demo, hacer `git pull` del repo de demos y leer el `REGISTRO.md` del HEAD
remoto, no una plantilla local.** La unicidad visible al prospecto (arquetipo pizarra +
isotipo de lanza + negro/amarillo) no se vio comprometida —esas tres técnicas son plomería
invisible—, pero el contador quedó tocado: `:has()`, line-drawing y `clip-path` pasan a
vetados.

### Gotcha técnico aprendido (2026-07-23)

**No dejar la interacción central dependiendo solo de `:has()`.** En la demo de Amazonas el
filtro de la grilla funcionaba al filtrar por día pero NO al filtrar solo por disciplina:
el motor no reinvalidaba el estilo de las filas ante ese cambio, aunque `element.matches()`
devolvía `true` y `CSS.supports('selector(:has(a))')` daba soporte. Patrón correcto:

- JS es la fuente de verdad y togglea una clase (`.is-off`) sobre cada fila.
- Las reglas `:has()` se scopean a `html:not(.js)` para que sean la base sin JS y no
  compitan con el JS.

Y al verificar filtros desde la consola: `input.checked = true` por propiedad **no**
dispara la invalidación de `:has()`; hay que usar `label.click()`. Además, si el estado
oculto lleva `transition: visibility 0s linear .42s`, una lectura inmediata de
`getComputedStyle` todavía devuelve `visible` — medir por la clase, no por el estilo.
