# Arranque: para Claude, cuando alguien llega sin leer nada

Este archivo cubre los dos casos más comunes:

- **A.** La persona escribe algo como *"instalá esto https://github.com/SoyJulieMartinez/reels-y-carruseles y decime cómo editar un reel"*.
- **B.** La persona sube el video (o las fotos, o el texto) directo al chat y dice *"editalo"*, sin ficha, sin carpetas y sin haber leído las instrucciones.

En los dos casos **el trabajo pesado lo hacés vos**. La persona no tiene que entender carpetas, códigos ni archivos: habla como le sale y vos traducís.

---

## 0. Instalar (siempre, en silencio)

```bash
git clone --depth 1 https://github.com/SoyJulieMartinez/reels-y-carruseles.git ~/kit-rc 2>/dev/null || (cd ~/kit-rc && git pull -q)
cd ~/kit-rc && bash setup.sh
```

Decí en una línea "Estoy preparando las herramientas, tarda un par de minutos la primera vez" y seguí. Si pide efectos especiales, sonidos realistas o animaciones, sumá `bash setup.sh --todo` (en segundo plano mientras charlás, si se puede).

Si `git clone` falla porque el entorno no tiene internet, decile que en Configuración de Claude tiene que estar activada la ejecución de código y la creación de archivos, y que vuelva a intentar. Si sigue fallando, pedile que descargue el ZIP desde GitHub (botón verde **Code → Download ZIP**) y te lo suba al chat; descomprimilo en `~/kit-rc`.

---

## A. Modo guiado ("decime paso a paso")

La persona quiere que la lleves de la mano. Reglas del modo guiado:

- **Un paso por mensaje.** Cada mensaje termina con una sola pregunta o una sola acción para ella.
- **Lenguaje simple.** Nada de "marca.json", "repositorio" o "renderizar": decí "tu estilo", "el sistema", "armar el video".
- **Preguntas con opciones para tocar** cuando el entorno lo permita; si no, opciones numeradas.
- Si en algún paso ya te dio la información (por ejemplo, subió el video de entrada), saltealo.

### Guion para un reel

1. **Bienvenida + qué vamos a hacer (una línea).** "Vamos a editar tu reel en 5 pasos. Primero tu estilo."
2. **Tu identidad visual.** Preguntá qué tiene, con opciones:
   - "Tengo brand kit o manual de marca" → que lo suba (PDF o imagen).
   - "Tengo logo o colores" → que suba el logo o escriba los colores.
   - "Tengo mi Instagram ordenado" → que suba 2 o 3 capturas de su feed (Instagram no se puede abrir desde acá).
   - "No tengo nada" → le proponés 3 paletas y 3 combinaciones de tipografías y elige.

   Con lo que suba: `python3 -m kit.marca paleta <imágenes>` propone los colores; las tipografías se preguntan o se proponen (`python3 -m kit.marca propuestas`). Armá la marca con `python3 -m kit.marca crear …` y mostrale la muestra (`python3 -m kit.marca muestra marca.json muestra.png`): "¿Así se ve tu marca?". Si el resultado trae `_aviso`, preguntale su color principal.
3. **Tu video.** "Subí tu video acá al chat." Si ya lo subió, pasá directo. Preguntá solo lo que no se ve en el video: el objetivo (vender, educar, contar una historia) y, si va a pedir comentarios, la palabra clave.
4. **El estilo de edición.** Ofrecé tres caminos:
   - "Tengo un video de referencia" → que pase el link o el archivo (ver `docs/referencias.md`).
   - "Quiero elegir yo" → pasale la biblioteca de recursos (`biblioteca/biblioteca-de-recursos.html`) para que copie su pedido.
   - "Elegí vos" → mostrale el muestrario sobre su video (`python3 -m kit.muestrario`) o decidí con los valores por defecto (sección C) y decile cuáles usaste.
5. **Editás.** Avisá cuánto tarda ("unos minutos"). Seguí `SKILL.md`: transcribir, plan, motor, revisión con `kit.revisar`. Entregá el video con una lista corta de qué hiciste.
6. **Cambios.** Enseñale la fórmula en una línea: *"Decime el segundo, qué querés cambiar y cómo. Ej.: en el segundo 12 el título me tapa la cara, subilo."* Aplicá todos los cambios juntos.
7. **Para la próxima (opcional, al final).** Ofrecé dejarle todo listo para que la próxima vez sea más rápido: armale su ficha de estilo (`plantillas/ficha-de-estilo.md` completada con lo que aprendiste) y el texto de `plantillas/instrucciones-del-proyecto.txt`, y explicale en 3 pasos cómo crear un Proyecto en Claude y pegarlos.

### Guion para un carrusel

1. Bienvenida + identidad visual (igual que el reel, pasos 1 y 2).
2. **Tu texto.** "Pegá el texto de tu carrusel, separado por placa (Placa 1: …, Placa 2: …)". Si no lo tiene separado, separalo vos sin cambiar las palabras y mostraselo para que confirme. Si no tiene texto pero tiene un reel, ofrecé "del reel a carruseles" (`docs/del-reel-a-carruseles.md`): es el único caso en que escribís el contenido, y solo si lo pide.
3. **Fotos (opcional).** "¿Querés usar fotos tuyas? Subilas acá."
4. **Estilo.** Las mismas tres opciones del reel (referencia, biblioteca, elegí vos → `python3 -m kit.opciones carrusel`).
5. **Diseñás** con `python3 -m kit.carrusel`, revisás `revision.jpg` y entregás los PNG + PDF.
6. Cambios con la fórmula: "placa + qué + cómo".
7. Para la próxima: igual que el reel.

---

## B. Modo "hacelo vos" (sube el material y listo)

La persona no quiere pasos: quiere el resultado. **No le pidas que ordene nada.**

1. **Encontrá el material.** Los archivos que sube al chat están en `/mnt/user-data/uploads/` (o en los archivos del Proyecto). Listalos y clasificalos solo: videos (crudos), imágenes (logo, brand kit, capturas, fotos), PDFs (brand kit o manual), textos.
2. **Ordenalo vos** en la estructura de `docs/trabajo-agentico.md`, en una carpeta de trabajo (nunca modifiques los originales):
   ```
   ~/trabajo/<marca>/originales/   copia de los crudos
   ~/trabajo/<marca>/marca/        marca.json, logo, brand kit
   ~/trabajo/<marca>/recursos/     capturas, fotos, flyers
   ~/trabajo/<marca>/trabajo/<pieza>/  transcripción, plan, editar.py, revisiones
   ~/trabajo/<marca>/resultados/   lo que se entrega
   ```
   Si hay varios videos, asumí que son piezas distintas salvo que digan lo contrario.
3. **La identidad visual es lo único obligatorio.**
   - Si hay ficha, brand kit o logo entre lo que subió → armá `marca.json` solo (`kit.marca`).
   - Si no hay nada → **una sola pregunta**, con opciones: "¿Me pasás tus colores o tu logo, o querés que te proponga una paleta?". No avances sin esto: un reel con colores inventados no es su marca.
4. **Todo lo demás lo decidís vos** con los valores por defecto (sección C), leyendo lo que dice en el video: objetivo, palabra clave del cierre, formatos que encajan.
5. **Editá, revisá y entregá.** Al entregar, una lista corta:
   - qué decidiste sin preguntar (ritmo, estilo de hook, recursos, sonidos);
   - qué conviene que confirme (nombres, palabra clave, datos);
   - "Si querés cambiar algo, decime el segundo y qué."
6. Si va a volver a usarlo, ofrecé al final armarle la ficha y las instrucciones del Proyecto (paso 7 del modo guiado).

---

## C. Valores por defecto (cuando nadie eligió)

| Qué | Por defecto |
|---|---|
| Ritmo | R2 Dinámico (un recurso cada 5–7 s). R3 si es una venta o un anuncio. R1 si es una historia personal o un tema sensible. |
| Hook | H1 Editorial con la frase más fuerte de los primeros 3 segundos, quieto desde el cuadro 0 |
| Subtítulos | S1 (2–3 palabras, la activa resaltada) + S4 (palabras clave en la tipografía de acento), bajo el mentón |
| Títulos | T01 escalonado en las 2–4 frases más fuertes; T03 etiquetas cuando enumera; T05/T06 lista cuando hay 3 o más ítems |
| Efectos | 1 cada 10–15 s, siempre terminando en un corte de cámara; nunca el mismo dos veces seguidas |
| Sonidos | Pop al aparecer elementos, swish en los cambios; nada sobre la voz |
| Cierre | C1 "comentá PALABRA" si dice una palabra clave; si no, C3 "guardalo" o el CTA que diga |
| No hacer | Cortar silencios o partes, cambiar lo que dice, bajar música o imágenes de internet |
| Carrusel | Portada con foto si hay; composiciones alternadas sin repetir; fondo oscuro para el cierre |

---

## Frases de la persona → qué hacer

| Si dice… | Hacé… |
|---|---|
| "instalá esto" + el link | Paso 0 y preguntá: "¿Querés editar un reel o diseñar un carrusel?" → modo guiado |
| "decime paso a paso" | Modo guiado (A) |
| "editalo", "hacelo vos", sube el video sin más | Modo "hacelo vos" (B) |
| "no tengo referencias", "no sé qué pedir" | Biblioteca o muestrario (`docs/referencias.md`) |
| Códigos como "R3, F03, SND-whoosh" | `docs/biblioteca-de-recursos.md` |
| "no tengo marca", "no sé mis colores" | Proponé 3 paletas + 3 pares de tipografías (`kit.marca propuestas`) |
| "me da miedo", "no soy técnica" | Tranquilizá en una línea ("Vos solo me contás; yo hago la parte técnica") y seguí con el modo guiado |
