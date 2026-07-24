# REGISTRO de demos — ledger de unicidad

Leer ANTES de diseñar cualquier demo nueva: arquetipos, firmas y componentes aquí listados
están QUEMADOS y no se repiten. Actualizar en el MISMO commit de cada demo publicada
(antes del push — ver "Publicar" en la skill `demo-landing`).
Base: `https://edithbalbouze.github.io/medine-demos/<slug>/`

| Negocio | Slug | Paleta | Tipografía / Densidad | Arquetipo | Técnica de firma | Nav / Footer | Tarjetas / CTAs | Fecha | Estado contacto |
|---|---|---|---|---|---|---|---|---|---|
| Laboratorio CETI | `ceti-demo` (repo aparte: `edithbalbouze/ceti-demo`) | Lavanda/rosa pastel `#fbf6fc` `#f6e8fa` `#eee2f1` + coral `#ff6f91` | Sans de sistema, densidad media, base clara | Hero split-grid con tarjeta flotante + pasos "1, 2, 3" | — (sin firma técnica; hero convencional) | Barra sticky clásica con `nav-links` / footer estándar | Tarjetas con sombra suave, CTA píldora | 2026-07-23 | enviado |
| Amazonas Pole Academy | `amazonas-pole-academy` | Off-white frío `#F0F0F5` + navy `#12487D` + azul de marca `#03569F` + acero `#566E74`; cian `#36D4EB` con tope de 2 usos | Archivo Black + Yellowtail (script) + Jost · densidad media-alta · base clara high-key con UNA sola banda navy (Exotic) | "El tablero de horarios que no existe" — bandas editoriales numeradas 01–06, grilla filtrable como protagonista | **"El asta"** — línea SVG vertical que se dibuja con el scroll y remata en punta de lanza en el footer, con nodos por sección (tomada del asta real del isotipo) | Píldora flotante centrada / footer-póster con display gigante a sangre + barra de contacto azul full-width | Filas full-width con hairlines de 1px, sin sombra · CTA rectangular duro · píldora reservada SOLO a los chips de horario | 2026-07-23 | demo publicada — mensaje **NO enviado** |
| Apamatte (Sophia Antonietta) | `apamatte` | Cereza `#B00434` · amarillo `#F8CB65` · coral `#C43C16` · rosa `#D4778D` · verde `#4E6136` sobre crema `#F7EFE7` — muestreados con PIL de su propio mockup de empaque | Fraunces variable (opsz/wght/SOFT/WONK) + Karla · densidad media con aire · base clara | Caja-vitrina con ventanas troqueladas (bento desigual dentro de un "panel de caja") | Apertura de caja: lazo que se desata + tapa que se levanta + foto enmascarada con la silueta del empaque + wordmark variable que gana peso al abrir | Píldora flotante superior centrada que se contrae al scroll / Footer-póster con display gigante + franja floral SVG propia | Fichas tipo etiqueta de caja con hairlines y chips cuadrados · CTA principal = **sello circular** con texto en trayectoria (eco de su sticker) · botón secundario = subrayado tipográfico | 2026-07-23 | por enviar |

| NR Médico Fisiatra | `nr-medico-fisiatra` | _(reconstruir)_ | Sans, base clara | Bandas apiladas (`band-a/b/c`) | _(sin firma registrada)_ | _(reconstruir)_ | _(reconstruir)_ | _(retroactivo)_ | _(revisar)_ |
| Nativos CF | `nativoscf` | Verde `#25D366` dominante | Anton + Barlow Condensed, base clara | Bandas apiladas (`hero` + `band`) | _(sin firma registrada)_ | _(reconstruir)_ | _(reconstruir)_ | _(retroactivo)_ | _(revisar)_ |
| Dayrrig Duarte (Pure Glow Day) | `pureglowday` | Vino `#701A1B` (dominante) · crema `#DCDDD8` · rojo CTA `#931717` · oro `#A8946B` / `#C9B489` · tinta `#2A1416` — muestreados con PIL de su carrusel "QUIEN SOY" (el vino dio sd=0.0) | **Bodoni Moda** variable (opsz estático, sin animar ejes) + Instrument Sans · densidad editorial alta · **base OSCURA** | Dossier editorial por capítulos numerados (00–04), con bloque de respiro en crema | Swash SVG que se dibuja solo (`stroke-dashoffset`) bajo UNA palabra del H1 — calco de su subrayado a pincel; dialoga con el brochazo real de su foto | **Rail lateral fijo** con índice numerado + hilo de progreso vertical (móvil: barra de progreso de 2px con capítulo activo) / **Colofón editorial**: índice numerado repetido + datos + redes en hairlines | Filas full-width con hairlines de oro y numeración colgada — **cero cards, cero sombras** · CTA principal = rectángulo de esquina dura con filete oro · secundario = subrayado tipográfico | 2026-07-23 | por enviar |
| Amazonas Pole Academy | `amazonas-pole-academy` | **Marca real B&N**: tinta `#14141A` + magenta acento `#C21E63`/`#E0447F` + rosa `#FF7FB0` sobre papel `#F5F4F6` — su logo es blanco y negro puro (muestreado con PIL), el magenta viene de su identidad de app validada por la clienta | **Archivo Black** (display) + **Yellowtail** (script) + cuerpo en sans del sistema · densidad media · base clara con una banda oscura | Bandas numeradas apiladas (01–06) con hero split | Foto del estudio con `mask-image` + reveals scroll-driven + `:has()` para filtros de grilla | Nav en píldora flotante centrada / Footer con datos y sello | Filas y fichas con hairlines; CTA principal = rectángulo relleno magenta, secundario = subrayado | 2026-07-24 | por enviar |
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
  - **Fraunces**: 1 uso real (Apamatte). La fila retroactiva de Pure Glow Day la contaba por
    error: esa demo se reconstruyó a **Bodoni Moda** precisamente para no repetirla. Aun así
    se mantiene **vetada** — es la display por defecto a la que tiende todo constructor.
  - Anton, Barlow Condensed, Archivo Black, Jost, Yellowtail, Instrument Sans, Karla: usadas
    una vez cada una.
  - Máximo **2 familias** por demo (Amazonas usó 3 — incumple el BRIEF-COMUN).

- **Deuda de contraste:** CETI y Apamatte son las dos de base CLARA. Donde Patricio
  (2026-07-23) saldó esa deuda con base oscura → **la próxima vuelve a base clara**.
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

### Técnicas quemadas (contador)

| Técnica | Usos | Estado |
|---|---|---|
| Scroll-driven animation (`animation-timeline: scroll()`) | 1 (Amazonas) | libre |
| `:has()` para filtros sin JS | 1 (Amazonas) | libre |
| `mask-image` con gradiente sobre foto | 1 (Amazonas) | libre |
| Foto real del local como hero | 1 (Amazonas) | libre — pero variar el tratamiento |

Dos bases claras seguidas (CETI y Amazonas). **La próxima demo va en base oscura**, salvo
que la marca del negocio lo prohíba de plano.

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
