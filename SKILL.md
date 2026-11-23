---
name: reels-y-carruseles
description: Editar reels verticales y diseñar carruseles de Instagram con la marca de cada persona (ficha de estilo + marca.json), con un motor probado. Usar al pedir editar un video, armar un carrusel o pasar un reel a carruseles.
---

# Reels y carruseles con Claude

Este repositorio tiene **reglas** (en `docs/`) y un **motor** (en `kit/`) que ya resuelve lo técnico: tipografías, tamaños reales de letra, márgenes seguros, subtítulos, efectos, sonidos y exportación. Usá el motor en lugar de escribir todo desde cero: así el resultado sale parejo y sin los errores típicos.

## 0. Preparar (una vez por chat)

```bash
git clone --depth 1 https://github.com/SoyJulieMartinez/reels-y-carruseles.git ~/kit-rc 2>/dev/null || (cd ~/kit-rc && git pull -q)
cd ~/kit-rc && bash setup.sh
```

Avisá en una línea que estás preparando las herramientas (tarda unos minutos la primera vez).

## 1. Cómo se trabaja

Leé `docs/trabajo-agentico.md`: orquestador con **director, operador y revisor** (subagentes distintos si el entorno los tiene; si no, tres pasadas avisando), una carpeta por marca (`originales/`, `marca/`, `recursos/`, `trabajo/<pieza>/`, `resultados/`) y un `LEEME.md` por pieza para retomar sin volver a preguntar.

## 1b. Qué leer según el pedido

| Pedido | Leer | Motor |
|---|---|---|
| Editar un reel | `docs/reels.md` | `kit/reel.py` (ver `docs/motor.md`) |
| Diseñar un carrusel con su texto | `docs/carruseles.md` | `kit/carrusel.py` |
| Animaciones complejas, mirar referencias en archivo | `docs/herramientas-extra.md` (instalar con `bash setup.sh --todo`) | HyperFrames, skills-edicion, Watch |
| La persona no sabe qué recursos usar, o es su primer video | `docs/opciones-de-edicion.md` | `kit/muestrario.py` |
| Antes de grabar, o el crudo tiene problemas | `docs/grabacion.md` | — |
| La persona pide por códigos o nombres de la biblioteca (R3, F03, E-backdrop-word, SND-whoosh…), o no tiene referencias | `docs/biblioteca-de-recursos.md` (y ofrecerle `biblioteca/biblioteca-de-recursos.html`) | según cada código |
| Referencias en links, o la persona no tiene o duda | `docs/referencias.md` | `kit/opciones.py` |
| Pasar un reel a carruseles (solo si lo pide) | `docs/del-reel-a-carruseles.md` + `docs/carruseles.md` | `kit/carrusel.py` |

Siempre leer también la **ficha de estilo** de la persona (la sube al Proyecto, plantilla en `plantillas/ficha-de-estilo.md`).

## 2. La marca → `marca.json`

Pasá la ficha a un `marca.json` como `ejemplos/marca-ejemplo.json`:
- 6 colores: `claro`, `blanco`, `acento_suave`, `medio`, `acento`, `oscuro` (HEX).
- 2 tipografías de Google Fonts: `sans` (texto) y `acento` (énfasis, en general serif o script). Si la fuente no está en Google Fonts, pedir los archivos .ttf y pasarlos en `"sans_archivos": [...]` / `"acento_archivos": [...]`.
- Subtítulos: palabras por bloque (2–3), tamaño (84–110), altura `y`, mayúsculas sí/no.

## 3. Reel (resumen; detalle en `docs/reels.md`)

1. `python3 -m kit.transcribir crudo.mp4 palabras.json` → corregir errores con `corregir={índice: "texto"}`.
2. `from kit.reel import cortes_de_camara` → los efectos terminan **justo** en un corte de cámara.
3. Escribir un `editar.py` como `ejemplos/ejemplo_reel.py`:
   - `r.hook(...)` **completo desde el cuadro 0** (es la portada del feed).
   - Títulos, chips, placas, desenfoque + checklist, tarjetas con capturas, barra de comentario con la palabra clave, subtítulos.
4. `r.probar([...tiempos])` antes de renderizar; mirar la imagen.
5. `r.render("resultados/reel_v1.mp4")` (nombre nuevo en cada versión).
6. `python3 -m kit.revisar resultados/reel_v1.mp4 trabajo/<pieza>/revision-v1` y seguir `docs/revision.md`. Recién después se muestra.

No cortar silencios ni contenido salvo que la persona lo pida. No bajar música ni b-roll de internet: solo lo que ella pase.

## 4. Carrusel (resumen; detalle en `docs/carruseles.md`)

1. El texto **no se toca** (salvo en "del reel a carruseles").
2. Armar `carrusel.json` como `ejemplos/carrusel-ejemplo.json`, eligiendo un tipo de placa por composición del catálogo y sin repetir composiciones seguidas.
3. `python3 -m kit.carrusel marca.json carrusel.json salida/` → PNG por placa, PDF, `revision.jpg` y avisos automáticos (texto < 30 px, márgenes, fondos repetidos).
4. Mirar `revision.jpg`, corregir y entregar los PNG + PDF.

## 5. Antes de entregar

- Diferenciar producido, revisado técnicamente y aprobado por la persona. Lo que no se pudo mirar queda pendiente.
- Reel: hook visible en el cuadro 0, nada en zonas tapadas por Instagram, subtítulos legibles, efectos que cortan con la cámara, audio a −14 LUFS.
- Carrusel: ningún texto cortado ni < 30 px, fondos sin repetir, una sola acción en el cierre.
- Entregar con una lista corta de qué se decidió sin preguntar, y la ficha actualizada si la persona aprobó algo nuevo.
