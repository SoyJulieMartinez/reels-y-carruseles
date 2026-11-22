# Sistema de diseño de carruseles

Este archivo es para Claude. Tiene las reglas, el catálogo de composiciones y la guía técnica para diseñar carruseles de Instagram con el estilo de la marca de este Proyecto.

**Solo diseño:** el texto lo pone la persona y no se toca.

El sistema tiene dos capas:

1. **Reglas fijas:** valen siempre.
2. **Ficha de estilo:** es el archivo `MI-FICHA-DE-ESTILO` de este Proyecto, en su parte común y su parte de carruseles. Manda en colores, tipografías, tono y composiciones.

El objetivo es un carrusel que **no parezca hecho por IA ni sea aburrido**: tiene que reconocerse como de esta marca aunque se tape el nombre.

---

## 1. Antes de diseñar

| Dato | Obligatorio | Si falta |
|---|---|---|
| Texto de cada placa | Sí | Pedirlo. No se escribe contenido |
| Ficha de estilo o brand kit | Sí | Proponer 2 colores y 1 par tipográfico, y que la persona elija |
| Objetivo (educar, vender, contar, anunciar) | No | Deducirlo del texto |
| Fotos o capturas | No | Diseñar sin fotos; nunca usar imágenes de internet |
| Referencias | No | Mostrar 3 opciones con `kit.opciones` y sugerir composiciones (ver `docs/referencias.md`) |

Antes de empezar, resumir en 2 o 3 líneas el sistema que se va a aplicar: fondos, tipografías y color de acento.

---

## 2. Reglas fijas

### 2.1 El texto no se toca
- No se reescribe, no se resume y no se agregan frases. Solo cambia la forma: cortes de línea, jerarquía y énfasis.
- Las indicaciones tipo "Placa 1 — Visual: …" son dirección de arte y nunca van escritas en la placa.
- Si algo no entra o no se lee, avisar y proponer una solución, sin recortar por cuenta propia.

### 2.2 Formato
- Lienzo de 1080 × 1350 px (4:5) con 90 px de margen.
- Todo el contenido de cada placa va centrado verticalmente.

### 2.3 Portada
- Es lo que se ve en el feed y lo que hace deslizar: título corto y grande (90–100 px), que se entienda en un segundo.
- Es la única placa con letra tan grande.

### 2.4 Legibilidad
- Títulos de 64 a 84 px, en 3 o 4 renglones como máximo, sin renglones de una sola palabra (`text-wrap: balance`).
- Texto de 31 a 38 px, **nunca menos de 30 px**.
- Párrafos de 3 renglones como máximo. Si hay más, se separan en frases cortas con aire.
- Contraste siempre: texto claro sobre fondo oscuro y oscuro sobre fondo claro.

### 2.5 Énfasis
- Una o dos cosas por placa: la tipografía de acento (cursiva o serif), el color de acento, una franja de color detrás de la frase o una palabra en negrita.

### 2.6 Ritmo
- Fondos alternados: nunca el mismo dos placas seguidas. El más oscuro, para el cierre.
- Después de una placa cargada, va una tranquila: solo texto y mucho aire.

### 2.7 Cierre
- Una sola acción, escrita: "Comentá GUÍA", "Guardalo", "Link en mi bio".
- Nunca un botón dibujado, porque en Instagram no se puede tocar.

### 2.8 Lo que ninguna placa lleva
- Numeración ("1/7").
- El @ o el logo en cada placa. El logo va como máximo una vez, en la portada o en el cierre.
- Puntitos que simulen un carrusel.
- Sobretítulos que no estén en el texto.
- Logos de marcas reales dibujados a mano (Instagram, Google, WhatsApp): se nombran en texto o se deja el lugar para el logo oficial.
- Relleno decorativo: stickers al azar, líneas sobre los títulos, celulares con apps inventadas.

### 2.9 Fotos de la persona
- Siempre con tratamiento, nunca pegadas sueltas: a sangre con un degradé hacia el color del fondo, en una mitad que se funde con el fondo, muy desenfocada como fondo, o completa con un velo oscuro.
- Nunca con texto sobre la cara.
- Si una foto es de baja resolución, avisar y pedir otra.

---

## 3. Para que no sea genérico ni aburrido

- **No repetir la misma composición** en placas seguidas. Usar el catálogo.
- **Un elemento gráfico entra solo si cuenta lo que dice la placa:** un chat cuando se habla de mensajes, un buscador cuando se habla de Google, un antes y después cuando se compara. Si no suma, no va.
- **Usar las composiciones favoritas de la ficha** como base y sumar 1 o 2 distintas por carrusel.
- **Prueba anti-genérico:** si se tapa el nombre, ¿se reconoce la marca? Si no, falta estilo.

### Catálogo de composiciones
- **A.** Texto grande solo, con mucho aire
- **B.** Texto + foto de la persona fundida con el fondo
- **C.** Cita destacada, con comillas grandes en la tipografía de acento
- **D.** Lista con íconos o números grandes
- **E.** Comparación: antes/después, mito/realidad, sí/no, en dos columnas o dos mitades
- **F.** Dato grande: un número o porcentaje protagonista con una frase corta
- **G.** Mockup de celular o laptop con una captura real adentro
- **H.** Mockup de chat (mensajes de WhatsApp o DM) cuando se habla de conversaciones
- **I.** Captura real enmarcada (reseña, comentario, resultado), con borde y sombra
- **J.** Franja de color detrás de la frase clave
- **K.** Paso a paso numerado
- **L.** Placa "respiro": una sola frase corta centrada
- **M.** Pregunta grande a la audiencia
- **N.** Foto de fondo desenfocada con el texto encima
- **O.** Checklist con tildes

**Según el objetivo:**
- **Educar:** D, K, O y L.
- **Vender:** F, I, E y un cierre claro.
- **Contar una historia:** B, C, N y L.
- **Anunciar:** G, F y J.

---

## 4. Proceso

1. Revisar qué falta (sección 1) y resumir el sistema que se va a aplicar.
2. **Planificar:** una tabla con placa → composición → qué se destaca → fondo, revisando que no se repitan composiciones ni fondos seguidos.
3. **Diseñar** (sección 6).
4. **Revisar** cada placa en una hoja de contacto:
   - textos cortados o superpuestos;
   - caras tapadas;
   - renglones con una sola palabra;
   - contenido no centrado;
   - textos de menos de 30 px;
   - fondos repetidos.
5. **Entregar:**
   - un PNG por placa y un PDF;
   - una lista corta de qué tiene cada placa;
   - qué se decidió sin preguntar.
6. **Cambios:** tocar solo la placa pedida y reenviar esa placa más el PDF. Si algo no gusta, simplificar antes que agregar.
7. **Aprender:** cuando la persona aprueba, pasarle la ficha de estilo actualizada (sección "Aprendizajes · Carruseles").

---

## 5. Cómo recibir pedidos de cambio

La persona va a pedir cambios con la fórmula "placa + qué + cómo + por qué". Ejemplo: "En la placa 3, la foto me tapa el título; ponela a la derecha porque el título es lo más importante".

---

## 6. Guía técnica (para Claude)

**Con este repositorio instalado, usar el motor `kit/carrusel.py`** (ver `docs/motor.md` y `ejemplos/carrusel-ejemplo.json`): arma el HTML, embebe tipografías y fotos, exporta PNG + PDF y revisa márgenes, textos chicos y fondos repetidos. Lo que sigue es cómo funciona por dentro.

**Estructura:** un HTML con una `<section>` de 1080 × 1350 por placa, con CSS propio.

**Tipografías:**
- Si Google Fonts está bloqueado, instalarlas con `npm i @fontsource/<fuente>` o bajarlas de `https://raw.githubusercontent.com/google/fonts/main/ofl/<familia>/`.
- Embeberlas en base64 con `@font-face` y verificar con `document.fonts.check` que cargaron.
- Si la marca usa una fuente que no es de Google Fonts, pedirle el archivo a la persona.

**Imágenes:** embebidas en base64 y redimensionadas a 1600 px como máximo.

**Exportación:**
- Con Playwright (Chromium): un PNG por placa (`locator.screenshot`) y un PDF con una página de 1080 × 1350 por placa.
- Si Playwright no está, instalarlo con `pip install playwright` y `playwright install chromium`.

**Referencias:** ver `docs/referencias.md`.
