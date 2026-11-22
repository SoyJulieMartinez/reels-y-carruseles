# Sistema de edición de video

Este archivo es para Claude. Contiene las reglas, el catálogo de formatos y la guía técnica para editar reels verticales con el estilo de la marca que está en este Proyecto.

El sistema tiene dos capas:

1. **Reglas fijas:** valen siempre.
2. **Ficha de estilo:** es el archivo `MI-FICHA-DE-ESTILO` de este Proyecto. Manda en colores, tipografías, tono y formatos.

El sistema funciona con tres piezas, y las tres están en este Proyecto:
- **Recursos de marca:** brand kit, logo, tipografías, stickers y tomas de apoyo.
- **Instrucciones del editor:** las instrucciones del Proyecto.
- **Guía de edición:** este archivo, más la ficha de estilo.

El objetivo es que el video **no parezca editado por IA**: tiene que reconocerse como de esta marca aunque se tape el nombre de la cuenta.

---

## 1. Antes de editar: el brief

Pedir en un solo mensaje lo que falte. Lo demás se decide y se avisa al entregar.

| Dato | Obligatorio | Si falta |
|---|---|---|
| Video crudo (mp4 o mov) | Sí | — |
| Brand kit o ficha de estilo | Sí | Proponer 2 colores y 1 par tipográfico, y que la persona elija |
| Objetivo del video (educar, vender, contar, anunciar, tendencia) | Sí | Deducirlo de lo que dice la persona |
| ¿Ya cortó los silencios? | Sí | Preguntar. Si ya los cortó, no se corta nada |
| Referencias (links o archivos) | No | Mostrar 3 opciones con `kit.opciones` y sugerir formatos (ver `docs/referencias.md`) |
| Recursos (capturas, fotos, flyers, b-roll, logo, música) | No | Usar solo lo que pase la persona; nunca bajar nada de internet |
| CTA del final | No | Usar el CTA preferido de la ficha |

---

## 2. Reglas fijas (no negociables)

### 2.1 Formato y zonas seguras (1080×1920, 30 fps)

- **Arriba:** dejar libres **250–300 px** (nombre de usuario, ícono de audio). Los títulos empiezan en y ≈ 300.
- **Abajo:** dejar libres **300–350 px** (texto del posteo, audio). Nada importante debajo de y ≈ 1570. El CTA final va más arriba, en y ≤ 1450, porque el texto del posteo puede crecer.
- **Costados:** ≥ **90 px**. A la **derecha**, ≥ 120 px para info clave, porque ahí están los botones de me gusta, comentar y compartir.
- **Recorte 4:5 del feed:** en la grilla se ve la franja y 285–1635. El hook y la cara tienen que entrar ahí.
- **Cara:** en el tercio medio. **Ningún texto tapa ojos ni boca.**
- Antes de ubicar textos, mirar **cada toma** (la cara cambia de lugar entre tomas) y anotar dónde está la cara, el micrófono y las manos, y qué zonas quedan libres o tienen fondo liso.

### 2.2 Hook de los primeros 3 segundos (siempre)

- Todo video arranca con un **texto gancho** de 0 a ~3 s. **No es un subtítulo literal:** es la promesa o la tensión del video resumida en 2 a 6 palabras.
- Es el texto **más grande** del video y queda **al menos 2,5 s** en pantalla.
- **El hook es la portada del feed.** Tiene que estar completo y quieto desde el fotograma 0: sin `\fad`, sin escala de entrada y sin aparecer palabra por palabra. Si no, la portada sale vacía o a medias. La frase entera se ve de una (por ejemplo, "tu presencia digital es *malisíma*") y va dentro del recorte 4:5 (y 285–1635). Para verificarlo, sacar el fotograma 0 recortado a 4:5 y mirarlo antes de entregar.
- En el **primer segundo** se mueve lo demás (una tarjeta, una captura, un zoom o un corte), nunca el texto del hook. Nunca un plano quieto sin nada.
- Durante el hook **no hay subtítulos** compitiendo.
- **Fórmulas de gancho:**
  - Contraste o paradoja: "39 seguidores y va a ser speaker".
  - Error común: "Estás perdiendo ventas por esto".
  - Promesa concreta: "3 pasos para…".
  - Pregunta directa: "¿Tu bio dice qué vendés?".
  - Resultado primero: "De 0 a 100 clientas en…".
  - Curiosidad: "Nadie te cuenta esto de…".
- Si la persona dice el gancho en cámara, el texto lo **resume**; no lo copia palabra por palabra.

### 2.3 Subtítulos

- **Legibles en un celular**:
  - Tamaño mínimo **70 px**; lo recomendado es **84–110 px** en sans gruesa.
  - Nunca finitos ni chicos: 66 px ya fue rechazado por chico.
- **De 1 a 3 palabras por bloque**, una sola línea. Se corta el bloque en pausas, en puntuación o si pasa los ~940 px de ancho.
- **Contraste siempre:**
  - Sobre fondos claros, texto oscuro con halo claro.
  - Sobre fondos oscuros o con mucha textura, texto claro con halo oscuro difuminado.
  - La otra opción es una caja de color de marca.
- **Posición:** en la banda entre el mentón y el pecho, justo debajo de la cara (≈ y 1100–1300). Se ajusta por toma si la cara sube o baja. Nunca sobre los ojos ni sobre la boca.
- **Palabra clave** resaltada con color de acento y/o la tipografía secundaria (por ejemplo, una serif en cursiva más grande).
- **Palabra activa** (karaoke): opcional, según la ficha.
- Se **ocultan** mientras hay hook, títulos, placas o tarjetas de texto, para que no compitan.
- **Ortografía:** revisar a mano lo que transcribe Whisper: nombres propios, marcas, tildes, y el voseo si la marca lo usa (sabés, querés, buscalas). Una palabra dudosa se marca y se avisa; no se inventa.

### 2.4 Títulos, placas y textos en pantalla

- **Dos niveles de jerarquía:**
  - Una línea "de apoyo" chica, en sans liviana o media.
  - Una línea "protagonista" grande, en la tipografía de acento, con el color de acento.
- **Líneas pegadas:** el interlineado entre la línea de apoyo y la protagonista es casi nulo o se superponen un poco. **Nunca un hueco visible entre una y otra.** Si al acercarlas chocan letras, se **escalonan**: la de arriba se corre hacia un costado y la protagonista hacia el otro.
- **Máximo 6–8 palabras** en pantalla a la vez.
- **Tiempo en pantalla:** 0,3 s por palabra + 0,6 s, con un mínimo de 1,5 s.
- Todo texto entra con animación corta (≤ 250 ms: fade, escala o desenfoque a nítido) y sale con corte limpio.
- Ancho máximo: 960 px. Si no entra, se achica el tamaño; nunca se pega a los bordes.
- **Texto "fantasma"** (opcional): la palabra gigante con mucha transparencia detrás del título.

### 2.5 Ritmo y cortes

- Algo cambia cada **2 a 4 segundos**: un corte, un zoom suave, un texto, una tarjeta o b-roll.
- **No se corta contenido** que dice la persona. Solo pausas largas (> 0,3 s), retomas y muletillas, y **solo si la persona no cortó ya los silencios**.
- **Los efectos respetan los cortes de cámara.** Si un tramo con fondo desenfocado, una placa o una tarjeta termina cerca de un cambio de toma, tiene que terminar **en el fotograma exacto del corte**. Si no, se ven fotogramas sueltos de la toma anterior. El motor lo detecta con `cortes_de_camara(video)`.
- 2–4 **placas** o momentos especiales por minuto; no más, para que no canse.

### 2.6 Composición

- **No achicar a la persona a un recuadro chico.** Si el video de la persona queda enmarcado, ocupa al menos el 60 % del ancho. Para destacar textos o listas, la mejor opción es **desenfocar y oscurecer el fondo** (el video sigue corriendo) y poner el contenido encima.
- **Tarjetas flotantes** (capturas, flyers, fotos, reseñas):
  - con borde de color de marca, esquinas redondeadas y sombra suave, inclinadas entre ±2 y ±5°;
  - entran deslizándose y apareciendo en ~0,2 s;
  - pueden tapar el micrófono o el cuerpo, pero no la cara.
- **Íconos:** dentro de círculos de color de marca, todos del mismo estilo (lleno o línea, no mezclados).
- El logo va con espacio libre del 20 % de su ancho y no se deforma.

### 2.7 Marca

- Solo los **colores** del brand kit, asignados a roles (ver la ficha).
- **Máximo 2 familias tipográficas**, con todos sus pesos. La mezcla típica es sans + serif o sans gruesa + sans fina.
- Las tipografías variables se convierten a **instancias estáticas** antes de renderizar (con `fontTools`), porque si no libass toma un peso por defecto.
- **Medir bien los textos:** en ASS, `\fs` es la altura de línea (ascent + descent de la fuente), no el tamaño de la letra. Poppins se dibuja a ~1/1,4 de `\fs` y Cormorant a ~1/1,21. Para calcular anchos con Pillow, usar `fs / ratio`. Para sacar el ratio de cualquier fuente: `(hhea.ascent - hhea.descent) / unitsPerEm`. Si se mide con `fs` directo, `fit()` achica los textos de más y quedan chicos.
- Contraste suficiente siempre: si un color de marca se lee poco sobre el video, se usa su versión oscura o clara, o se le agrega halo.

### 2.8 Audio

- Voz normalizada a **-14 LUFS**, con compresor suave y paso alto en 80 Hz.
- Si hay música (solo la que pasa la persona), va **20–24 dB por debajo de la voz**, con fade de entrada y de salida.

### 2.9 Cierre y CTA

- En los últimos 2–4 s, **una sola acción**: comentar una palabra, guardar, seguir, link en la bio o escribir por mensaje.
- Puede ir con una placa de cierre de marca o con texto sobre la persona. Lleva el @ de la cuenta.

### 2.10 Revisión antes de entregar (checklist)

1. La evidencia de `python3 -m kit.revisar` (hoja con antes / en / después de cada entrada y salida, y clips), más 3 subtítulos sobre tomas distintas y el cierre. Ver `docs/revision.md`.
2. Revisar en cada uno:
   - textos dentro de las zonas seguras y sin tapar la cara;
   - títulos sin huecos entre líneas;
   - subtítulos de ≥ 84 px y legibles sobre ese fondo;
   - ortografía y nombres propios.
3. Fotogramas justo antes y después de **cada transición** de efecto: que no queden fotogramas sueltos.
4. La duración final, y que el audio no termine cortado.
5. Si algo falla, corregir y volver a renderizar. **No se entrega sin revisar.**

---

## 2b. Ficha de estilo (la capa personalizable)

Se completa con el brand kit, las referencias y el tono de la persona. La plantilla para la persona está en `plantillas/ficha-de-estilo.md`, y los colores y tipografías pasan a `marca.json`. Cada vez que la persona aprueba algo, se propone el texto actualizado para la sección "Aprendizajes" de la ficha. **Dos marcas nunca se ven editadas igual:** la calidad y las reglas son las mismas, el estilo cambia.

```
FICHA DE ESTILO — <marca>
Colores por rol
  - Fondo de placas:            #______
  - Texto principal en placas:  #______
  - Acento / palabra protagonista: #______  (versión oscura para fondos claros: #______)
  - Resaltado en subtítulos:    #______
  - Halo / sombra:              claro u oscuro según el fondo
Tipografías por rol
  - Subtítulos:          <familia + peso>, <tamaño> px
  - Título de apoyo:     <familia + peso liviano>
  - Título protagonista: <familia acento, p. ej. serif cursiva o display>
  - Etiquetas [ ENTRE CORCHETES ] / datos: <familia>, mayúsculas espaciadas
Subtítulos
  - Palabras por bloque: 1 / 2–3
  - Mayúsculas o minúsculas
  - Con caja o sin caja (halo)
  - Resaltado de palabra activa: sí / no
Tono y textos
  - Persona (vos / tú / usted), registro (cercano, experto, divertido, inspirador)
  - Frases o muletillas de marca y CTA preferido
Movimiento
  - Suave/elegante (fades, desenfoque) o enérgico (pops, zooms, cortes rápidos)
Elementos gráficos
  - Íconos (estilo), formas (estrellas, líneas, círculos), stickers, texturas, marcos
Formatos preferidos (del catálogo)
  - <3–5 formatos que identifican a la marca>
Prohibido
  - <lo que la persona no quiere ver>
```

**Si no hay referencias** (además de mostrar opciones, ver `docs/referencias.md` y `docs/opciones-de-edicion.md`):
1. Elegir 3–5 formatos del catálogo según el objetivo del video.
2. Definir una "personalidad de movimiento" que coincida con el tono:
   - marca elegante → fades y serif en cursiva;
   - marca enérgica → pops, mayúsculas y cortes rápidos;
   - marca cercana → stickers, manuscrita y tarjetas inclinadas.
3. Avisar en la entrega qué se decidió.

**Si hay referencias:** se copia el **lenguaje visual** (cómo combina tipografías, ritmo, posiciones, tipo de placas, elementos) y **nunca** sus colores, fuentes ni logos. Todo se traduce al brand kit.

---

## 3. Catálogo de formatos

Cada video combina **un formato base** con **2–4 recursos** de esta lista. Se eligen según lo que dice la persona en cada tramo.

| # | Formato | Cómo es | Cuándo usarlo |
|---|---|---|---|
| 1 | **A cámara + subtítulos** | La persona habla, con subtítulos dinámicos | Base de casi todo; consejos, opiniones |
| 2 | **Tipografía cinética** | Títulos que aparecen mezclando tipografías, tamaños y pesos sobre el video | Frases fuertes, estilo editorial |
| 3 | **Pantalla dividida vertical** (arriba/abajo) | Persona en una mitad y demo, b-roll o producto en la otra | Tutoriales, reacciones, "mientras te explico, mirá" |
| 4 | **Pantalla dividida horizontal** (izq/der) | Dos videos o imágenes lado a lado | Comparación A vs B, antes/después, mito vs realidad |
| 5 | **Tarjetas flotantes** | Capturas, fotos, flyers o reseñas que entran sobre el video | Pruebas, datos, "mirá esto" |
| 6 | **Pantalla verde** | Persona recortada delante de una web, captura, noticia o imagen | Explicar algo que se ve en pantalla, noticias |
| 7 | **Imagen en imagen (PIP)** | Contenido grande y la persona en un recuadro (≥ 35 % de ancho) | Grabación de pantalla con explicación |
| 8 | **B-roll con voz en off** | Planos de detalle, proceso o lugar, con la voz encima | Storytelling, procesos, "un día en…" |
| 9 | **Placa a pantalla completa** | Fondo de color de marca con una frase grande | Golpes de efecto, datos clave, transiciones de tema |
| 10 | **Fondo desenfocado + contenido** | El video sigue corriendo desenfocado y oscurecido, con texto, lista o tarjeta encima | Listas, frases largas, destacar sin cortar a la persona |
| 11 | **Lista con íconos** | Ítems que entran uno por uno con su ícono | Enumeraciones, beneficios, pasos |
| 12 | **Paso a paso numerado** | 01 · 02 · 03 con contador o barra de progreso | Tutoriales, métodos |
| 13 | **Grabación de pantalla con zoom** | Captura de la compu o del celular con zooms al cursor y resaltados | Herramientas, apps, configuraciones |
| 14 | **Mockup de dispositivo** | Web, app o post dentro de un celular o laptop dibujado | Mostrar trabajos, portfolios, lanzamientos |
| 15 | **Antes / después** | Barrido o división que revela el cambio | Transformaciones, resultados |
| 16 | **Collage / mosaico** | Grilla de 3–4 clips o fotos que se arma | Resúmenes, eventos, variedad de productos |
| 17 | **Marco editorial / revista** | Video grande enmarcado sobre papel o color, con títulos tipo revista | Marcas elegantes (persona ≥ 60 % del ancho) |
| 18 | **Solo texto sobre clip estético** | Texto que se lee sobre un clip lindo sin persona hablando | Frases, reflexiones, tendencias "POV" |
| 19 | **Entrevista / dos personas** | Cortes entre cámaras, nombre en un zócalo | Charlas, testimonios, colaboraciones |
| 20 | **Testimonio / prueba social** | Persona o captura de un mensaje o reseña, con estrellas | Ventas, confianza |
| 21 | **Datos animados** | Números que suben, barras o porcentajes | Resultados, estadísticas |
| 22 | **Reacción / dueto** | Otro video arriba y la persona abajo reaccionando | Tendencias, opinar sobre algo |
| 23 | **Carrusel en video** | Secuencia de fotos o placas con texto y transición | Productos, tips rápidos, sin hablar a cámara |
| 24 | **Zócalo / identificación** | Nombre + rol en una franja con estilo de marca | Presentar a alguien, invitadas, expertas |
| 25 | **Ranking** | Posiciones (3, 2, 1) que se revelan y se destacan mientras se nombran | Tops, favoritos, "los 3 errores" |
| 26 | **Verdadero o falso** | Afirmaciones que aparecen en el centro y vuelan a su categoría | Mitos, educación, interacción |
| 27 | **A vs B en columnas** | Dos columnas de conceptos; al cierre una alternativa se atenúa | Comparar métodos, herramientas, opciones |
| 28 | **Burbujas de chat o comentarios** | Mensajes tipo WhatsApp o comentarios que aparecen alrededor de la persona | Prueba social, "me preguntan…" |
| 29 | **Barra de comentario como CTA** | Un campo de comentario dibujado donde se escribe la palabra clave, con el botón de enviar | Cierre con "comentá X" |
| 30 | **Fondo con patrón + video enmarcado** | Patrón de marca (lunares, estrellas, líneas) con el video grande encima y stickers | Marcas lúdicas, anuncios, lanzamientos |
| 31 | **Placa de serie** | "EPISODIO 02 · detrás de cámaras" con estilo fijo | Contenido en serie, fidelizar |
| 32 | **Voz en off / vlog** | Clips del día o del proceso con voz grabada aparte y textos cortos | Lifestyle, "un día conmigo", procesos |
| 33 | **Título detrás de la silueta** | El texto queda entre el fondo y la persona (máscara cuadro por cuadro) | Hooks, frases protagonistas |
| 34 | **Persona recortada sobre fondo de marca** | La persona sin su fondo real, sobre un fondo gráfico | Anuncios, placas con presencia |
| 35 | **Fotos tipo Polaroid** | Fotos con marco blanco que entran inclinadas | Recuerdos, historias, resultados |
| 36 | **Círculo con texto curvo** | Video enmarcado en un círculo con texto alrededor | Marca de serie, lanzamientos |
| 37 | **Plano cinematográfico** | Bandas negras arriba y abajo, color más cine | Storytelling, momentos emotivos |
| 38 | **Narración con reloj, capítulo o contador** | Reloj que marca la hora, placa de capítulo, número que sube | Historias en el tiempo, "un día en", resultados |
| 39 | **Checklist animado** | Ítems que se tildan de a uno | Pasos, requisitos, listas de control |
| 40 | **Antes/después con cortina** | Una cortina que se desliza y revela el después | Transformaciones |
| 41 | **Tablero** | Alterna cámara con pantallas de explicación: indicador circular, comunidad alrededor de un centro, de contenido a entregable, chat y respuesta, contacto que avanza por etapas, ciclo de 3 pasos, capturas que se relevan, captura encuadrada | Explicar procesos, métodos y sistemas |
| 42 | **Lista por pasos que se acumula** | Filas de color que aparecen al nombrarlas, se apilan y vuelven a cámara | Enumeraciones largas, requisitos |
| 43 | **Énfasis tipográfico** | Una frase de contexto chica y la palabra clave enorme, con jerarquía marcada | Ideas fuertes, frases para guardar |
| 44 | **Anuncio dinámico** | Títulos, gráficos de apoyo, destacados y CTA sobre cámara, con ritmo rápido | Lanzamientos, promociones, eventos |
| 45 | **POV** | Título de apertura fijo + subtítulos breves, nada más | Tendencias, reflexiones, humor |

Hay imágenes de muestra de los formatos 3, 5, 41, 43 y 45 en `docs/muestras/`.

**Variaciones de un reel:** del mismo crudo se pueden sacar de 2 a 6 versiones, cada una con **una sola diferencia** (el hook, el formato o el estilo de subtítulos), para usarlas en los Reels de prueba de Instagram y saber qué cambio funcionó. Se nombran `_A`, `_B`, `_C`… y en la entrega se anota qué cambia en cada una.

**Banco de tomas de apoyo:** si la persona tiene b-roll guardado (en el Proyecto o en `recursos/`; ver `docs/grabacion.md`), se usa para tapar cortes, ilustrar lo que dice o armar videos con voz en off, sin repetir la misma toma en un mismo reel.

**Las tres piezas del sistema** (así se lo explicamos a las alumnas):
- recursos de marca;
- instrucciones del editor;
- guía de edición (este repositorio más la ficha).

Si falta una, el resultado sale genérico.

**Recursos que se combinan con cualquier formato:**
- zoom suave (105–112 %) en frases clave;
- texto fantasma detrás del título;
- etiquetas [ ENTRE CORCHETES ];
- subrayado o círculo dibujado;
- estrella o destello de acento;
- flecha que señala;
- barra de progreso;
- emoji de marca;
- cambio a blanco y negro en una frase;
- congelado de imagen con texto;
- subtítulos que aparecen palabra por palabra;
- palabra tachada que se reemplaza por otra;
- texto que se escribe solo (un evento ASS por letra o sílaba, con 40–60 ms entre cada uno);
- stickers de marca;
- reels de la persona flotando como miniaturas;
- transiciones entre escenarios.

**Dónde se hace cada recurso:** el menú completo (motor, efectos, HyperFrames) está en `docs/opciones-de-edicion.md`.

**Cómo elegir formatos según el objetivo:**
- **Educar:** 1, 11, 12 y 13, con 9 para las ideas fuertes.
- **Vender:** gancho de dolor, 5 o 20 como prueba, 21 para resultados y CTA claro.
- **Storytelling:** 8, 2 y 10, con ritmo más lento.
- **Anunciar** (eventos, lanzamientos): 5 con el flyer, 14 y 24, más el dato de fecha en una etiqueta.
- **Tendencia:** 18, 22 y 4.

---

## 4. Proceso

0. **Antes de grabar:** si la persona todavía no grabó, pasarle `docs/grabacion.md`.
1. **Brief:** revisar qué falta (sección 1).
2. **Preparar el entorno:** ver la guía técnica (sección 6).
3. **Normalizar:** si el video es de iPhone y viene en HDR (`color_transfer` arib-std-b67 o smpte2084), convertirlo a SDR bt709 con `zscale` + `tonemap` en una copia.
4. **Mirar el crudo:** hoja de contacto con grilla. Anotar dónde está la cara en cada toma y detectar los cortes.
5. **Transcribir** y corregir. Un hueco entre palabras no prueba silencio: sin pedido explícito no se corta nada.
5b. **Proponer:** si es el primer video, si pide opciones o si no eligió formatos, mostrar el muestrario y una tabla de opciones por momento, y preguntar una sola vez (ver `docs/opciones-de-edicion.md`).
6. **Planificar (director):** armar una tabla con tiempos que incluya:
   - el hook;
   - el formato de cada parte;
   - los títulos;
   - las tarjetas;
   - las placas;
   - el CTA;
   - los tramos sin subtítulos.
7. **Editar (operador):** seguir el plan. Orden de capas: video → fondos (desenfoque, placas) → tarjetas e íconos → textos.
8. **Revisar (revisor):** juntar evidencia con `python3 -m kit.revisar` y seguir `docs/revision.md`: comparar con el plan y con la checklist 2.10, marcar cada control como aprobado / falló / pendiente, corregir y volver a mirar lo que se corrigió. Los roles están explicados en `docs/trabajo-agentico.md`.
9. **Entregar:**
   - el .mp4;
   - una lista corta de qué tiene la edición;
   - qué se decidió sin preguntar;
   - qué falta confirmar.
10. **Aprender:** cuando la persona aprueba o pide un cambio de gusto, proponer el texto actualizado de la ficha de estilo para que lo guarde en el Proyecto.

---

## 5. Cómo recibir pedidos de cambio

La persona va a pedir cambios con la fórmula "dónde + qué + cómo + por qué":
- Aplicar todos los cambios de la tanda juntos y entregar una versión nueva (v2, v3…).
- Si algo no queda claro, preguntar una sola vez, mostrando el fotograma en cuestión.

---

## 6. Guía técnica (para Claude)

**Con este repositorio instalado, usar el motor `kit/reel.py`** (ver `docs/motor.md` y `ejemplos/ejemplo_reel.py`): ya resuelve todo lo de esta sección. Lo que sigue explica cómo funciona por dentro, para cuando haga falta algo que el motor no trae.

**Herramientas base:** ffmpeg, subtítulos ASS (libass), faster-whisper y Pillow. Revisar qué hay instalado e instalar lo que falte.

**Transcripción:**
```bash
pip install --break-system-packages -q faster-whisper
```
- Probar primero `WhisperModel("small", device="cpu", compute_type="int8")`.
- Si la descarga de HuggingFace está bloqueada, bajar el modelo por npm sin ejecutar scripts:
  1. `npm pack @skillninja/shortmovie-telop-model-p0` (y p1, p2, p3);
  2. descomprimirlos;
  3. copiar `config.json`, `tokenizer.json`, `vocabulary.json` y `preprocessor_config.json`;
  4. unir `model.bin.part0..3` en `model.bin`;
  5. verificar con `model.sha256`.
- Leer el audio WAV mono a 16 kHz como array de numpy y transcribir con `language='es', word_timestamps=True`.
- Guardar las palabras con su inicio y su fin en un JSON.

**Tipografías:**
- Bajarlas de `https://raw.githubusercontent.com/google/fonts/main/ofl/<familia>/`.
- Si son variables (`[wght]`), crear instancias estáticas con `fontTools.varLib.instancer` antes de usarlas en ASS.
- Si la marca usa una tipografía que no es de Google Fonts, pedirle el archivo a la persona.

**Medir bien los textos:** en ASS, el tamaño (`\fs`) es la altura de línea, no la letra. Poppins se dibuja a ~1/1,4 de ese número y Cormorant a ~1/1,21. Para calcular anchos con Pillow, usar `tamaño_ASS / 1,4` (o `/ 1,21`). Si no, los textos se achican de más y quedan chicos.

**Motor de edición:**
- Todos los textos van en un archivo ASS de 1080 × 1920, con `\pos`, `\fad`, `\t` para las animaciones, `\bord` + `\blur` para el halo y `\p1` para las formas.
- Las placas de color y los fondos desenfocados se hacen con `overlay` de ffmpeg, con `enable='between(t,a,b)'`.
- Las tarjetas (PNG hechos con Pillow, con borde, sombra y rotación) se superponen con `overlay`, entrando con `fade=alpha` y un deslizamiento corto.
- Si hay cortes, renderizar por tramos y concatenarlos. Un solo filtergraph con muchos `trim` se queda sin memoria.
- Para probar textos rápido: `-ss t -i base.mov -vf "setpts=PTS+t/TB,ass=subs.ass"` en fotogramas sueltos.
- **Salida:** H.264 con CRF 19, AAC a 192 kbps y `+faststart`.

**Herramientas extra (HyperFrames, skills-edicion, Watch):** ver `docs/herramientas-extra.md`.

**Efectos avanzados (opcional): carpeta `efectos/`.** 51 efectos para videos a cámara que detectan la cara y separan a la persona del fondo. Sirven para la palabra gigante detrás de la cabeza, la palabra tachada, la checklist que se tilda, la barra de comentario, las notificaciones, la tapa de revista, el foco y los acercamientos de cámara.
- **Preparar:** `bash setup.sh --efectos` (o `bash efectos/scripts/setup.sh`, imprime READY).
- **Usar:** `efectos/.venv/bin/python efectos/scripts/fx.py <efecto> <video> <salida> --start <s> --end <s> --text "..." --opt color=<hex>`. La lista de efectos y sus opciones está en `efectos/GUIA.md`. Probar primero un cuadro suelto (`--still <s>`, con salida `.png`) y recién después renderizar.
- **Nombre y usuario:** en los efectos que muestran un perfil, pasar siempre `--opt name="..." --opt handle="@..."` con los datos de la marca.
- **Orden:** los efectos se aplican antes que los subtítulos, títulos y sonidos del motor (el video con efectos pasa a ser el crudo de `Reel`), y siempre con los colores de la marca.
- Si la preparación falla, usar las alternativas de abajo o proponer otro efecto.

**Persona recortada o título detrás de la silueta:** la primera opción es `efectos/` (`backdrop-word`, `huge-strike`). Si no se puede usar, se hace una máscara de la persona cuadro por cuadro con `mediapipe`. El orden de capas es fondo → texto → persona. Si la máscara no se puede generar, avisar y proponer otro efecto.

**Texto que se escribe solo:** se arma con un evento ASS por letra o por sílaba, con 40 a 60 ms entre cada uno.

**Referencias:** cómo abrirlas, qué rasgos sacar y cómo proponer opciones si no hay, en `docs/referencias.md`.

---

## 7. Nivel 2: carpeta en la compu

```
Edición de videos/
  marcas/<marca>/        → brand kit (PDF o imágenes), logo, fuentes/, ficha-de-estilo.md, referencias/
  marcas/<marca>/recursos/ → stickers, patrones, íconos, b-roll, música, capturas
  originales/<marca>/    → crudos (no se tocan nunca) + brief.txt opcional
  trabajo/<marca>/<pieza>/ → transcripción, plan, LEEME.md, normalizados
  resultados/<marca>/    → AAAA-MM-DD_tema_v1.mp4, _v2, variaciones _A/_B, caption.txt
```

**Flujo:**
1. La persona deja el crudo en `originales/<marca>/` y pide "editá los videos nuevos de <marca>".
2. Claude trae a su espacio de trabajo solo los archivos que necesita para editar (o trabaja directo en la carpeta si tiene una terminal en la compu).
3. Escribe el resultado en `resultados/` con un nombre nuevo; nunca sobrescribe un archivo existente.
4. Si la persona quiere cambios, los escribe en `cambios.txt` al lado del video, o en el chat. Sale una v2, y el aprendizaje se pasa a la ficha de la marca.

Se usa una carpeta por marca: las clientas nunca se mezclan. Opcionalmente se puede programar una tarea que revise las carpetas de originales en un horario fijo. Para eso, la computadora tiene que estar prendida y con la app de Claude abierta.

---

## 8. Errores ya vistos (no repetir)

- **Subtítulos de 66 px y de una palabra:** quedaron chicos. Usar 84–110 px y 2–3 palabras.
- **Hueco entre la línea de apoyo y la protagonista:** pegarlas o escalonarlas.
- **Títulos o subtítulos sobre el micrófono o la boca:** buscar la zona libre en cada toma.
- **Texto blanco sobre una cortina o pared clara:** usar texto oscuro con halo claro.
- **Persona achicada en un cuadradito con palabras a los costados:** queda feo. Usar fondo desenfocado y contenido encima.
- **Efecto que termina unos fotogramas antes del cambio de toma:** se ve desprolijo. Alinearlo al corte exacto.
- **Tipografía variable sin instanciar:** el peso sale mal.
- **Letra más chica de lo pedido:** en ASS, `\fs` es la altura de línea. El motor ya lo compensa; si se escribe ASS a mano, dividir por el ratio de la fuente.
- **Hook con animación de entrada:** la portada del feed sale vacía. El hook va quieto y completo desde el cuadro 0.
- **Etiquetas con texto diminuto:** mismo problema del `\fs`; medir siempre con el ratio.
- **Un nombre de servicio mal dicho en pantalla:** usar siempre el nombre que la persona indica en su ficha (por ejemplo, el nombre comercial del servicio y no una palabra genérica).
- **Video de iPhone lavado:** venía en HDR. El motor lo convierte a SDR; Dolby Vision o LOG necesitan revisar una muestra de color antes de seguir.

