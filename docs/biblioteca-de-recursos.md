# Biblioteca de recursos (referencia para Claude)

Cada recurso tiene un código. Cuando la persona pide por código o por nombre (por ejemplo "R3, F03, E-backdrop-word, SND-whoosh"), buscalo acá: la última columna dice con qué se hace. La versión para elegir es `biblioteca/biblioteca-de-recursos.html`.

Reglas al usarla:
- Lo que elige la persona manda, pero si un recurso no encaja con lo que dice en ese momento, proponé una alternativa en una línea.
- Nunca repetir el mismo recurso dos veces seguidas. Los efectos terminan en un corte de cámara.
- "motor" = `kit/reel.py`; "efectos" = `efectos/scripts/fx.py`; "earshot", "real-sfx" y "HyperFrames" se instalan con `bash setup.sh --todo`.
- Si una herramienta extra no está instalada, usar lo más parecido del motor y decirlo en la entrega.

## Ritmo de la edición

Cuánto cambia la pantalla. Elegí una opción.

| Código | Nombre | Qué es | Cómo se hace |
|---|---|---|---|
| `R1` | Tranquilo | Subtítulos y 2 o 3 momentos destacados. Para historias, reflexiones y temas sensibles. | motor: subtítulos + 2–3 recursos en las frases más fuertes |
| `R2` | Dinámico | Un recurso cada 5 a 7 segundos. El equilibrio para la mayoría de los reels. | motor + 2–4 efectos |
| `R3` | Muy dinámico | Algo cambia cada 2 o 3 segundos: títulos, etiquetas, efectos, placas y sonidos. Para captar atención y vender. | motor + 8–12 efectos alternados, sin repetir el mismo recurso seguido (ejemplo: ejemplos/reel_dinamico.py) |
| `R4` | Solo subtítulos | Nada más que tus subtítulos con tu estilo. | motor: r.hook + r.subtitulos |

## Tipos de video

La estructura general del reel. Podés combinar 2 o 3.

| Código | Nombre | Qué es | Cómo se hace |
|---|---|---|---|
| `F01` | A cámara + subtítulos | Hablás a cámara con subtítulos dinámicos. La base de casi todo. | motor: r.subtitulos |
| `F02` | Tipografía cinética | Títulos que aparecen mezclando tipografías, tamaños y pesos. | motor: r.titulo / r.texto |
| `F03` | Pantalla dividida arriba/abajo | Vos en una mitad y la demo, el producto o el b-roll en la otra. | efectos: split-headline o broll-split; o ffmpeg vstack |
| `F04` | Pantalla dividida izquierda/derecha | Dos videos o imágenes lado a lado. | ffmpeg hstack + motor encima |
| `F05` | Tarjetas flotantes | Capturas, fotos, flyers o reseñas que entran sobre el video. | motor: r.tarjeta |
| `F06` | Pantalla verde | Vos recortada delante de una web, captura o noticia. | efectos (máscara mediapipe) + fondo |
| `F07` | Imagen en imagen | El contenido grande y vos en un recuadro (al menos 35 % del ancho). | ffmpeg overlay + motor |
| `F08` | B-roll con voz en off | Tomas de apoyo (manos, lugar, proceso) con tu voz encima. | cortes con ffmpeg + motor; necesita tus tomas |
| `F09` | Placa a pantalla completa | Fondo de color de tu marca con una frase grande. | motor: r.placa + r.texto |
| `F10` | Fondo desenfocado + contenido | El video sigue desenfocado y con texto, lista o tarjeta encima. | motor: r.desenfoque / r.checklist |
| `F11` | Lista con íconos | Ítems que entran uno por uno, cada uno con su ícono. | motor: r.checklist con íconos |
| `F12` | Paso a paso numerado | 01 · 02 · 03 mientras lo explicás. | motor: r.texto / efectos: lineup |
| `F13` | Grabación de pantalla con zoom | Tu compu o celular con acercamientos y resaltados. | HyperFrames (agent-cursor, browser-device-stage) o ffmpeg zoompan |
| `F14` | Mockup de dispositivo | Tu web, app o post dentro de un celular o laptop. | HyperFrames: browser-device-stage / app-showcase |
| `F15` | Antes y después | Un barrido que revela el cambio. | efectos: swipe / HyperFrames: before-after-wipe |
| `F16` | Collage o mosaico | Grilla de 3 o 4 clips o fotos que se arma. | ffmpeg xstack / HyperFrames |
| `F17` | Marco editorial o revista | Tu video enmarcado con títulos tipo revista. | efectos: cover-star (look=editorial) |
| `F18` | Solo texto sobre clip estético | Texto que se lee sobre un clip lindo, sin hablar a cámara. | motor sobre tu b-roll |
| `F19` | Entrevista o dos personas | Cortes entre cámaras y nombre en un zócalo. | cortes + motor: zócalo |
| `F20` | Testimonio o prueba social | Captura de un mensaje o reseña, con estrellas. | motor: r.tarjeta + íconos estrella |
| `F21` | Datos animados | Números que suben, barras o porcentajes. | efectos: liquid-glass-graph / HyperFrames: data-chart |
| `F22` | Reacción o dueto | Otro video arriba y vos abajo reaccionando. | ffmpeg vstack + motor |
| `F23` | Carrusel en video | Secuencia de fotos o placas con transición. | kit/carrusel.py + ffmpeg |
| `F24` | Zócalo de identificación | Tu nombre y rol en una franja con tu estilo. | motor: r.placa parcial + r.texto / HyperFrames: lt-clean-bar |
| `F25` | Ranking | Posiciones 3, 2, 1 que se revelan mientras las nombrás. | motor: r.texto / HyperFrames |
| `F26` | Verdadero o falso | Afirmaciones que aparecen y vuelan a su categoría. | HyperFrames |
| `F27` | A vs B en columnas | Dos columnas de conceptos; al final una se apaga. | motor: r.texto en dos columnas |
| `F28` | Burbujas de chat o comentarios | Mensajes tipo WhatsApp alrededor tuyo. | efectos: messages |
| `F29` | Caja de comentario como CTA | Un campo de comentario que escribe tu palabra clave y se envía. | motor: r.barra_comentario / efectos: comment-box |
| `F30` | Fondo con patrón + video enmarcado | Patrón de tu marca con el video grande encima. | ffmpeg overlay + motor |
| `F31` | Placa de serie | "EPISODIO 02" con estilo fijo, para contenido en serie. | motor: r.placa + r.texto |
| `F32` | Voz en off o vlog | Clips del día con tu voz grabada aparte y textos cortos. | cortes + motor |
| `F33` | Título detrás de tu silueta | El texto queda entre el fondo y vos. | efectos: backdrop-word / huge-strike |
| `F34` | Vos recortada sobre fondo de marca | Sin tu fondo real, sobre un fondo gráfico. | efectos (máscara) + placa |
| `F35` | Fotos tipo Polaroid | Fotos con marco blanco que entran inclinadas. | motor: r.tarjeta con rot |
| `F36` | Círculo con texto curvo | Tu video en un círculo con texto alrededor. | ffmpeg geq + ASS |
| `F37` | Plano cinematográfico | Bandas negras arriba y abajo, color de cine. | ffmpeg drawbox + efectos: moody |
| `F38` | Reloj, capítulo o contador | Hora que avanza, placa de capítulo o número que sube. | efectos: countdown-flip / motor |
| `F39` | Checklist animado | Ítems que se tildan de a uno. | motor: r.checklist / efectos: todo, checklist |
| `F40` | Antes y después con cortina | Una cortina que se desliza y revela el después. | HyperFrames: before-after-wipe |
| `F41` | Tablero | Alternás cámara con pantallas que explican un proceso. | HyperFrames + motor |
| `F42` | Lista por pasos que se acumula | Filas de color que se apilan a medida que las nombrás. | motor: r.texto / r.placa |
| `F43` | Énfasis tipográfico | Una frase chica de contexto y la palabra clave enorme. | motor: r.titulo |
| `F44` | Anuncio dinámico | Títulos, destacados y CTA con ritmo rápido. Para lanzamientos y promos. | motor + efectos |
| `F45` | POV | Un título de apertura fijo y subtítulos breves, nada más. | motor: r.hook + r.subtitulos |

## El hook (portada del reel)

Lo primero que se ve, completo desde el primer cuadro, porque también es la portada en tu feed.

### Cómo se ve

| Código | Nombre | Qué es | Cómo se hace |
|---|---|---|---|
| `H1` | Editorial | Frase chica + palabra protagonista en tu tipografía de acento, con la misma palabra gigante y transparente detrás. | motor: r.hook(..., fantasma=) |
| `H2` | Impacto | Palabra protagonista en mayúsculas, grande y contundente. | motor: r.hook(..., mayus=True) |
| `H3` | Contraste | Fondo desenfocado y oscuro con el texto claro encima. | motor: r.desenfoque + r.hook(modo='sobre_oscuro') |
| `H4` | Hook + acercamiento | El texto quieto y la cámara que se acerca de golpe en la palabra clave. | motor: r.hook + efectos: lean-in |
| `H5` | Detrás de vos | La palabra clave gigante detrás de tu cabeza. | efectos: backdrop-word desde el cuadro 0 (revisar la portada) |

### Qué dice (si no tenés hook)

| Código | Nombre | Qué es | Cómo se hace |
|---|---|---|---|
| `HF1` | Contraste | "Todos hacen X. Yo hago Y." | texto: proponer 3 hooks y que elija |
| `HF2` | Error común | "El error que hace que…" | texto |
| `HF3` | Promesa concreta | "En 30 segundos vas a saber…" | texto |
| `HF4` | Pregunta directa | "¿Te pasa que…?" | texto |
| `HF5` | Resultado primero | "Así pasé de X a Y." | texto |
| `HF6` | Curiosidad | "Nadie habla de esto…" | texto |

## Subtítulos

Siempre grandes y legibles. Elegí el estilo.

| Código | Nombre | Qué es | Cómo se hace |
|---|---|---|---|
| `S1` | 2 o 3 palabras, la que se dice resaltada | El estilo más usado: bloques cortos y la palabra activa en tu color. | motor: subtitulos (palabras=3, resaltar_activa=true) |
| `S2` | Palabra por palabra | Una palabra por vez, muy dinámico. | motor: subtitulos (palabras=1) |
| `S3` | En mayúsculas | Todo en mayúsculas, más contundente. | motor: subtitulos (mayusculas=true) |
| `S4` | Palabras clave en cursiva de acento | Las palabras importantes cambian a tu tipografía de acento y tu color. | motor: subtitulos(enfasis={...}) |
| `S5` | Bajo el mentón | Cerca de la cara, donde se mira. | motor: subtitulos y≈1250 |
| `S6` | En el pecho o más abajo | Para cuando hay muchos elementos arriba. | motor: subtitulos y≈1400 (sin pasar la zona segura) |
| `S7` | Sin subtítulos | Solo si hay títulos que cuentan todo. | no llamar a r.subtitulos |

## Títulos y textos en pantalla

Recursos del motor, siempre con tus tipografías y colores.

| Código | Nombre | Qué es | Cómo se hace |
|---|---|---|---|
| `T01` | Título escalonado | Dos líneas pegadas: una frase de apoyo y la palabra protagonista en otra tipografía, corrida a un costado. | motor: r.titulo |
| `T02` | Palabra fantasma | La palabra protagonista gigante y transparente detrás del título. | motor: r.titulo(fantasma=) / r.fantasma |
| `T03` | Etiquetas flotantes | Pastillas con texto que entran girando, una por cada cosa que nombrás. | motor: r.chip |
| `T04` | Placa a pantalla completa | Fondo liso de tu color con una frase grande. | motor: r.placa + r.texto |
| `T05` | Fondo desenfocado + lista | Tu video desenfocado con una lista que se tilda. | motor: r.checklist |
| `T06` | Lista con íconos | Cada ítem con su ícono (ver Íconos). | motor: r.checklist con íconos |
| `T07` | Tarjeta con captura o foto | Una captura, foto o flyer flotando con sombra. | motor: r.tarjeta |
| `T08` | Caja de comentario CTA | Un comentario que escribe tu palabra clave y se envía. | motor: r.barra_comentario |
| `T09` | Zócalo con tu nombre | Nombre y rol en una franja. | motor: r.placa parcial + r.texto |
| `T10` | Número o dato grande | Una cifra protagonista ("6 h", "+300"). | motor: r.texto en tipografía de acento |
| `T11` | Etiqueta de sección | "[ EJEMPLO ]", "[ PASO 2 ]" arriba de un bloque. | motor: r.checklist(etiqueta=) / r.texto |

## Efectos

Siguen tu cara y nunca la tapan. Se adaptan a tus colores cuando el efecto lo permite.

### Cámara y color

| Código | Nombre | Qué es | Cómo se hace |
|---|---|---|---|
| `E-lean-in` | Acercamiento de golpe | La cámara se acerca rápido en una palabra. | efectos: lean-in |
| `E-slow-push` | Acercamiento lento de cine | Se acerca despacio a tu cara mientras el fondo se desenfoca. | efectos: slow-push |
| `E-locked-on` | Esquinas de enfoque | Esquinas tipo cámara se enganchan a tu cara y te siguen. | efectos: locked-on |
| `E-over-the-shoulder-zoom` | Zoom a la esquina con gráfico | La cámara va a una esquina y aparece un gráfico que sube. | efectos: over-the-shoulder-zoom |
| `E-moody` | Color ambiente | Gradación de color: moody, blanco y negro, cálido, frío o pop. | efectos: moody |
| `E-spotlight` | Foco de luz | Se apagan las luces y quedás iluminada, con una palabra que brilla detrás. | efectos: spotlight |
| `E-glitter-spotlight` | Foco dorado con brillos | Rayos dorados detrás de tu cabeza y una palabra con brillo. | efectos: spotlight (look=sparkle) |
| `E-timeline` | Look de edición | Color rojo de cine con línea de tiempo y REC. | efectos: timeline |
| `E-rabbit-hole` | Túnel giratorio | La imagen se mete dentro de sí misma girando. | efectos: rabbit-hole |
| `E-dot-reveal` | Imagen de puntos | Tu imagen se arma con puntos de luz y después aparece completa. | efectos: dot-reveal |
| `E-swipe` | Antes y después deslizante | Una barra que pasa y cambia el look. | efectos: swipe |

### Texto detrás de vos

| Código | Nombre | Qué es | Cómo se hace |
|---|---|---|---|
| `E-backdrop-word` | Palabra gigante detrás de vos | Una palabra enorme cae detrás de tu cabeza. | efectos: backdrop-word |
| `E-huge-strike` | Palabra tachada | Una palabra gigante detrás tuyo y una línea roja que la tacha. | efectos: huge-strike |
| `E-crayon-write` | Palabra escrita con crayón | Un crayón escribe la palabra detrás tuyo y la subraya. | efectos: crayon-write |
| `E-led-sign` | Cartel de luces | Se baja la luz y un cartel luminoso se escribe detrás tuyo. | efectos: led-sign |
| `E-red-collage` | Collage rojo | Vos en blanco y negro, una palabra roja gigante y tres frases que golpean. | efectos: red-collage |
| `E-pastel-word` | Palabra en fondo pastel | Fondo lavanda, palabra gigante detrás y una tarjeta de perfil que te siguen. | efectos: pastel-word |
| `E-match-cut` | Recortes de noticias | Páginas de noticias que cortan sobre una palabra en un recuadro rojo. | efectos: match-cut |
| `E-cover-star` | Tapa de revista | Te convertís en la tapa de una revista, con título detrás tuyo. | efectos: cover-star |

### Títulos

| Código | Nombre | Qué es | Cómo se hace |
|---|---|---|---|
| `E-headline-box` | Titular en caja | Acercamiento con un titular de dos líneas, la segunda en una caja. | efectos: headline-box |
| `E-split-headline` | Titular que te empuja abajo | Una tarjeta con titular baja y te deja en la mitad de abajo. | efectos: split-headline |
| `E-tape-label` | Cinta con frase | Una cinta con tu frase sobre el pecho. | efectos: tape-label |
| `E-reject-stamp` | Sello | Un sello grande cae sobre la pantalla. | efectos: reject-stamp |
| `E-pause-point` | Pausa con flecha | Congela la imagen y te señala con una flecha dibujada. | efectos: pause-point |
| `E-scribble` | Garabatos de marcador | Dibujos de marcador alrededor tuyo. | efectos: scribble |
| `E-select-resize` | Número que se agranda | Un recuadro de selección agarra un número y lo agranda. | efectos: select-resize |
| `E-the-bill` | Ticket impreso | Tus instrucciones salen impresas como un ticket. | efectos: the-bill |

### Listas y pasos

| Código | Nombre | Qué es | Cómo se hace |
|---|---|---|---|
| `E-todo` | Tarjeta de tareas | Una tarjeta al costado que se va tildando mientras hablás. | efectos: todo |
| `E-checklist` | Lista que gira y se tilda | Cada paso gira y se pone en verde. | efectos: checklist |
| `E-apple-toggles` | Interruptores | Una tarjeta de ajustes que prende sus interruptores de a uno. | efectos: apple-toggles |
| `E-lineup` | Fichas numeradas en abanico | Fichas con números que se abren arriba de tu cabeza. | efectos: lineup |
| `E-countdown-flip` | Cuenta regresiva | Un reloj 3, 2, 1 arriba de tu cabeza. | efectos: countdown-flip |
| `E-tier-list` | Tabla de ranking | Una tabla S/A/B donde algo sube al primer puesto. | efectos: tier-list |
| `E-shortcut-rain` | Lluvia de teclas | Teclas de teclado que llueven detrás tuyo. | efectos: shortcut-rain |

### Redes y prueba social

| Código | Nombre | Qué es | Cómo se hace |
|---|---|---|---|
| `E-comment-box` | Comentario que se escribe | Una barra de comentario escribe una palabra y la publica. | efectos: comment-box |
| `E-tap` | Botón Seguir | Aparece un botón Seguir que cambia a Siguiendo. | efectos: tap |
| `E-messages` | Notificaciones de mensajes | Mensajes que aparecen uno tras otro. | efectos: messages |
| `E-liquid-glass-graph` | Gráfico que sube | Una tarjeta de vidrio con un gráfico y un número que crece. | efectos: liquid-glass-graph |
| `E-reel-frame` | Tu video como reel | El video se achica a una tarjeta de reel. | efectos: reel-frame |
| `E-noise` | Reels que se apilan | Tus reels se apilan detrás tuyo. | efectos: noise |
| `E-orbit` | Reels en órbita | Tus reels giran alrededor de tu cabeza. | efectos: orbit |
| `E-carousel-spin` | Carrusel 3D de reels | Tus reels giran a tu alrededor y se frenan. | efectos: carousel-spin |
| `E-phone-fan` | Celulares en abanico | Tus reels se abren como un abanico de celulares. | efectos: phone-fan |
| `E-fan-build` | Portadas en abanico | Las portadas de tus reels se reparten detrás tuyo. | efectos: fan-build |
| `E-profile-wall` | Pared de tu perfil | Tu grilla llena la pared mientras un contador sube. | efectos: profile-wall |
| `E-place-in-grid` | Vos en tu grilla | Te achicás al centro de tu grilla y aparecen tus reels alrededor. | efectos: place-in-grid |
| `E-headline-wall` | Pared de titulares | Titulares sobre vos que se apilan detrás. | efectos: headline-wall |
| `E-check-pills` | Pastillas que se marcan | Fondo cuadriculado con pastillas que un cursor marca. | efectos: check-pills |
| `E-broll-split` | Toma de apoyo arriba | B-roll arriba con una etiqueta de precio y vos abajo. | efectos: broll-split |
| `E-glass-widgets` | Widgets de vidrio | Widgets esmerilados que flotan alrededor de tu cabeza. | efectos: glass-widgets |
| `E-uninstall` | Desinstalar con glitch | Una barra de desinstalación que rompe la imagen. | efectos: uninstall |
| `E-wave-trim` | Onda de voz que se recorta | Un panel con tu voz donde se recortan los silencios. | efectos: wave-trim |

## Transiciones y movimiento

Cómo se pasa de un momento al otro.

| Código | Nombre | Qué es | Cómo se hace |
|---|---|---|---|
| `X01` | Corte seco | Sin transición: lo más limpio y profesional. | por defecto |
| `X02` | Acercamiento de golpe | La cámara salta hacia vos en el cambio. | efectos: lean-in |
| `X03` | Acercamiento lento | Empuje suave de cine. | efectos: slow-push |
| `X04` | Barrido | Una barra que pasa y cambia la imagen. | efectos: swipe / HyperFrames: before-after-wipe |
| `X05` | Flash editorial | Un destello blanco con aire de revista. | HyperFrames: editorial-flash-overlay |
| `X06` | Glitch | Un salto digital con interferencia. | HyperFrames (bloques de glitch) / efectos: uninstall |
| `X07` | Congelar en el golpe | La imagen se congela un instante en el momento justo. | HyperFrames: beat-freeze-cut |
| `X08` | Separación de color | Los colores se separan como un efecto óptico. | HyperFrames: chromatic-radial-split |
| `X09` | Zoom cinematográfico | Un zoom amplio que lleva a la siguiente escena. | HyperFrames: cinematic-zoom |
| `X10` | Entrada desenfocada | El texto o la imagen aparecen desde desenfocado. | HyperFrames: blur-in |
| `X11` | Letras que suben | Las letras entran de abajo hacia arriba. | HyperFrames: bottom-up-letters |
| `X12` | Sacudida de cámara | Un temblor corto para dar impacto. | HyperFrames: camera-shake |
| `X13` | Túnel giratorio | La imagen se mete en sí misma. | efectos: rabbit-hole |
| `X14` | Grano de película | Textura de cine encima de todo el video. | HyperFrames: grain-overlay |

## Sonidos

Se eligen por nombre. Con las herramientas extra suenan reales; también podés pedir cualquier otro describiéndolo.

### Aparición de elementos

| Código | Nombre | Qué es | Cómo se hace |
|---|---|---|---|
| `SND-pop` | Pop | Un pop corto cuando aparece algo. | motor: r.sonido(t, 'pop') |
| `SND-pop-suave` | Pop suave | Más delicado, para marcas tranquilas. | earshot: 'a soft pop' |
| `SND-burbuja` | Burbuja | Pop redondo, divertido. | earshot: 'a bubble pop' |
| `SND-brillo` | Brillo | Un destello que brilla, para algo especial. | earshot: 'a sparkle shine' |
| `SND-tap` | Toque | Un toque suave, como tocar la pantalla. | earshot: 'a soft tap' |

### Transiciones y movimiento

| Código | Nombre | Qué es | Cómo se hace |
|---|---|---|---|
| `SND-swish` | Swish | Paso rápido de aire. | motor: r.sonido(t, 'swish') |
| `SND-whoosh` | Whoosh | Un barrido de aire más largo. | earshot: 'a whoosh transition' |
| `SND-whoosh-grande` | Whoosh grande | Barrido potente, para cambios importantes. | earshot: 'a big cinematic whoosh' |
| `SND-subida` | Subida de tensión | Sonido que sube antes de algo importante. | earshot: 'a riser' |
| `SND-bajada` | Bajada | Sonido que baja, para cerrar o relajar. | earshot: 'a downlifter' |
| `SND-reversa` | Ola en reversa | Un sonido que crece hacia el corte. | earshot: 'a reverse swell' |
| `SND-deslizar` | Deslizar | Un dedo que desliza. | earshot: 'a swipe' |
| `SND-papel` | Papel | Hoja que se da vuelta. | earshot: 'a paper page turn' |

### Impacto y énfasis

| Código | Nombre | Qué es | Cómo se hace |
|---|---|---|---|
| `SND-golpe` | Golpe | Un golpe seco para remarcar una palabra. | earshot: 'a hit impact' |
| `SND-golpe-grave` | Golpe grave | Un golpe profundo que se siente. | earshot: 'a sub drop' |
| `SND-boom` | Boom | Impacto cinematográfico. | earshot: 'a cinematic boom' |
| `SND-corte` | Golpe de corte | Golpe corto para un cambio brusco. | earshot: 'a cut hit' |
| `SND-glitch` | Glitch | Interferencia digital corta. | earshot: 'a glitch' |
| `SND-sello` | Sello | Un sello que cae. | earshot: 'a stamp thump' |
| `SND-logo` | Firma de marca | Un sonido corto de cierre, tipo logo. | earshot: 'a short logo sting' |

### Interfaz y redes

| Código | Nombre | Qué es | Cómo se hace |
|---|---|---|---|
| `SND-click` | Clic | Clic de mouse o botón. | earshot: 'a mouse click' |
| `SND-interruptor` | Interruptor | Un switch que se prende. | earshot: 'a toggle switch on' |
| `SND-notificacion` | Notificación | Aviso de mensaje nuevo. | earshot: 'a notification' |
| `SND-exito` | Éxito | Notas que suben, algo salió bien. | earshot: 'a success sound' |
| `SND-ding` | Ding | Campanita clara. | motor: r.sonido(t, 'ding') |
| `SND-error` | Error | Dos notas que bajan, algo salió mal. | earshot: 'an error sound' |
| `SND-enviar` | Enviar | Mensaje que sale. | motor: r.sonido(t, 'enviar') |
| `SND-recibir` | Recibir | Mensaje que llega. | earshot: 'a message received' |
| `SND-like` | Me gusta | Tres notas rápidas y alegres. | earshot: 'a like twinkle' |
| `SND-moneda` | Moneda o caja registradora | Para ventas y precios. | earshot: 'a cash register' / 'a coin' |
| `SND-camara` | Obturador de cámara | Una foto que se saca. | earshot: 'a camera shutter click' |

### Escritura

| Código | Nombre | Qué es | Cómo se hace |
|---|---|---|---|
| `SND-tecla` | Tecla | Una tecla sola. | motor: r.sonido(t, 'tecla') |
| `SND-tecleo` | Tecleo | Alguien escribiendo en el teclado. | earshot: 'keyboard typing' |
| `SND-lapiz` | Lápiz o birome | Escritura a mano. | earshot: 'a pen writing' |

### Objetos y ambiente

| Código | Nombre | Qué es | Cómo se hace |
|---|---|---|---|
| `SND-vaso` | Toque de vidrio | Un toque suave en una copa. | earshot: 'a light tap on a glass' |
| `SND-puerta` | Puerta | Una puerta que se abre. | earshot: 'a door opening' |
| `SND-golpe-puerta` | Golpe en la puerta | Toc toc. | earshot: 'knocking on a door' |
| `SND-reloj` | Reloj | Tic tac. | earshot: 'a clock ticking' |
| `SND-pasos` | Pasos | Pasos que se acercan. | earshot: 'footsteps' |
| `SND-lluvia` | Lluvia | Lluvia de fondo, para un clima íntimo. | earshot: 'rain' |
| `SND-viento` | Viento | Viento suave de fondo. | earshot: 'wind' |
| `SND-agua` | Agua | Gotas o agua que corre. | earshot: 'water drip' |

### Otras opciones

| Código | Nombre | Qué es | Cómo se hace |
|---|---|---|---|
| `SND-descripto` | Un sonido que describo | Escribí cuál querés en el campo de notas ("una caja registradora", "aplausos"). | earshot: descripción traducida al inglés |
| `SND-biblioteca` | Mis propios sonidos | Diseño de sonido completo con sonidos grabados que tenés vos. | real-sfx sobre el video terminado |
| `SND-ninguno` | Sin efectos de sonido | Solo tu voz (y tu música, si la pasás). | no llamar a r.sonido |

## Íconos

Para listas en reels y carruseles. Se dibujan con tus colores.

| Código | Nombre | Qué es | Cómo se hace |
|---|---|---|---|
| `I-check` | Tilde |  | kit/iconos.py: 'check' |
| `I-estrella` | Estrella |  | kit/iconos.py: 'estrella' |
| `I-objetivo` | Objetivo |  | kit/iconos.py: 'objetivo' |
| `I-personas` | Personas |  | kit/iconos.py: 'personas' |
| `I-crecimiento` | Crecimiento |  | kit/iconos.py: 'crecimiento' |
| `I-corazon` | Corazón |  | kit/iconos.py: 'corazon' |
| `I-chat` | Chat |  | kit/iconos.py: 'chat' |
| `I-reloj` | Reloj |  | kit/iconos.py: 'reloj' |
| `I-casa` | Casa |  | kit/iconos.py: 'casa' |
| `I-idea` | Idea |  | kit/iconos.py: 'idea' |
| `I-dinero` | Dinero |  | kit/iconos.py: 'dinero' |
| `I-camara` | Cámara |  | kit/iconos.py: 'camara' |
| `I-calendario` | Calendario |  | kit/iconos.py: 'calendario' |
| `I-ubicacion` | Ubicación |  | kit/iconos.py: 'ubicacion' |
| `I-flecha` | Flecha |  | kit/iconos.py: 'flecha' |
| `I-rayo` | Rayo |  | kit/iconos.py: 'rayo' |
| `I-celular` | Celular |  | kit/iconos.py: 'celular' |
| `I-regalo` | Regalo |  | kit/iconos.py: 'regalo' |

## Color y look del video

El tono general de la imagen.

| Código | Nombre | Qué es | Cómo se hace |
|---|---|---|---|
| `L1` | Natural | Tu video tal cual, solo corregido. | sin gradación |
| `L2` | Cálido | Tonos más dorados y cercanos. | efectos: moody grade=warm |
| `L3` | Frío | Tonos más azulados y limpios. | efectos: moody grade=cool |
| `L4` | Blanco y negro | En momentos puntuales, para dramatizar. | efectos: moody grade=bw |
| `L5` | Moody | Contraste suave y oscuro, más íntimo. | efectos: moody grade=moody |
| `L6` | Pop | Colores más vivos y saturados. | efectos: moody grade=pop |
| `L7` | Cine | Bandas negras arriba y abajo. | ffmpeg drawbox + moody |

## Cierre y llamado a la acción

Siempre una sola acción.

| Código | Nombre | Qué es | Cómo se hace |
|---|---|---|---|
| `C1` | Comentá una palabra | "Escribime JORNADA" con la caja de comentario que se escribe sola. | motor: r.titulo + r.barra_comentario |
| `C2` | Seguime | El botón Seguir que cambia a Siguiendo. | efectos: tap |
| `C3` | Guardalo | "Guardalo para cuando…" | motor: r.titulo |
| `C4` | Compartilo | "Mandáselo a alguien que…" | motor: r.titulo |
| `C5` | Link en la bio | "Link en mi bio" con tu usuario. | motor: r.titulo + r.texto |
| `C6` | Escribime por mensaje | "Escribime al DM". | motor: r.titulo / efectos: messages |
| `C7` | Placa final de marca | Placa con tu color, tu nombre y tu usuario. | motor: r.placa + r.texto |

## Carruseles: composiciones

Para cada placa. Tu texto no se cambia: esto es solo diseño.

### Composiciones de placa

| Código | Nombre | Qué es | Cómo se hace |
|---|---|---|---|
| `CA` | Texto grande con aire | Una frase fuerte sola. | carrusel: tipo texto |
| `CB` | Texto + tu foto fundida | Para cercanía e historias. | carrusel: tipo foto |
| `CC` | Cita con comillas grandes | Frases tuyas o testimonios. | carrusel: tipo cita |
| `CD` | Lista con íconos o números | Consejos y beneficios. | carrusel: tipo lista (iconos) |
| `CE` | Comparación | Antes/después, así sí / así no. | carrusel: tipo comparacion |
| `CF` | Dato grande | Un número protagonista. | carrusel: tipo dato |
| `CG` | Mockup de celular o laptop | Para mostrar tu trabajo. | a mano en el HTML del carrusel |
| `CH` | Chat | Conversación tipo WhatsApp. | carrusel: tipo chat |
| `CI` | Captura enmarcada | Reseñas y comentarios reales. | a mano en el HTML del carrusel |
| `CJ` | Franja de color detrás de la frase | Para destacar una idea. | carrusel: ==frase== |
| `CK` | Paso a paso numerado | Tutoriales. | carrusel: tipo pasos |
| `CL` | Placa respiro | Una frase corta entre placas cargadas. | carrusel: tipo respiro |
| `CM` | Pregunta grande | Para generar comentarios. | carrusel: tipo pregunta |
| `CN` | Foto de fondo desenfocada | Portadas y cierres. | carrusel: tipo fondo_foto |
| `CO` | Checklist con tildes | Requisitos y listas. | carrusel: tipo lista (tildes) |

### Portada

| Código | Nombre | Qué es | Cómo se hace |
|---|---|---|---|
| `CP1` | Portada con tu foto | Título arriba y tu foto fundida abajo. | carrusel: portada con foto |
| `CP2` | Portada solo texto | Título grande sobre tu color. | carrusel: portada sin foto |
| `CP3` | Portada pregunta | Una pregunta directa como gancho. | carrusel: pregunta como placa 1 |

### Destacados dentro del texto

| Código | Nombre | Qué es | Cómo se hace |
|---|---|---|---|
| `CX1` | Palabra en cursiva de acento | Una palabra en tu tipografía de acento y tu color. | carrusel: *palabra* |
| `CX2` | Franja de color | Una frase con una franja detrás. | carrusel: ==frase== |
| `CX3` | Negrita | Una palabra más pesada. | carrusel: **palabra** |
