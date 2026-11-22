# El motor, función por función

Todo en tiempos del video **original** (en segundos). Si se usan `cortes`, el motor recalcula solo.

## Reel

```python
from kit.reel import Reel, cortes_de_camara, hoja_de_contacto, portada
r = Reel("crudo.mp4", "marca.json", fin=None, cortes=None)   # cortes=[(ini, fin), ...] solo si la persona pide cortar
```

| Función | Qué hace |
|---|---|
| `r.hook(apoyo, protagonista, hasta=3.6, fantasma=None)` | Hook de portada: dos líneas pegadas y escalonadas, **sin animación** (visible en el cuadro 0). |
| `r.titulo(t0, t0b, t1, apoyo, protagonista, y=300, tam_apoyo=84, tam_prot=190, fantasma=None, mayus=False)` | Título de dos líneas: aparece el apoyo en `t0`, la palabra protagonista en `t0b`, se van en `t1`. Oculta los subtítulos mientras tanto. |
| `r.texto(t0, t1, x, y, texto, rol, peso, tam, color, italica=False, modo=...)` | Texto suelto. `rol` = `"sans"` o `"acento"`. `tam` es el tamaño **real** de la letra. |
| `r.fantasma(t0, t1, x, y, texto, tam=300, color, alfa)` | Palabra gigante y transparente detrás de un título. |
| `r.chip(t0, t1, cx, cy, texto, rot=0, tam=46)` | Etiqueta tipo pastilla (con sonido "pop"). |
| `r.tarjeta(imagen, t0, t1, cx, cy, ancho=640, rot=-3)` | Captura o foto flotante con borde y sombra. |
| `r.placa(t0, t1, color="oscuro")` | Fondo liso a pantalla completa. |
| `r.desenfoque(t0, t1)` | Fondo desenfocado (para listas o textos largos). |
| `r.checklist(t1, [(t, texto), ...], titulo=(t, texto), etiqueta=(t, texto))` | Lista con tildes sobre fondo desenfocado. Con `(t, texto, "objetivo")` cada ítem lleva su ícono (formato 11). |
| `r.icono(nombre, t0, t1, cx, cy, radio=58)` | Ícono suelto con los colores de la marca. 18 íconos: check, estrella, objetivo, personas, crecimiento, corazon, chat, reloj, casa, idea, dinero, camara, calendario, ubicacion, flecha, rayo, celular, regalo (`python3 -m kit.iconos iconos.png` los muestra). |
| `r.barra_comentario(t0, palabra, t_escribe, t1=None)` | Caja de comentario que se "escribe" sola con la palabra clave del CTA. |
| `r.subtitulos(palabras_json, corregir={}, enfasis=set(), mantener=set())` | Subtítulos por bloques; `enfasis` va en la tipografía de acento; `mantener` respeta mayúsculas. |
| `r.sonido(t, tipo)` | `pop`, `swish`, `ding`, `tecla`, `enviar` (sintetizados, sin derechos de autor). |
| `r.probar([t, ...])` | Imagen de prueba rápida en esos segundos, sin renderizar todo. |
| `r.render("final.mp4")` | Render final 1080×1920, 30 fps, audio normalizado a −14 LUFS. Normaliza videos HDR de iPhone. |

Utilidades: `r.puntos_de_revision()` (lo usa `kit.revisar`; el render lo guarda en `<salida>.puntos.json`), `cortes_de_camara(video)`, `hoja_de_contacto(video, tiempos, salida)`, `portada(video, salida)` (cuadro 0 recortado 4:5, como se ve en el feed).

### Zonas seguras (ya respetadas por las posiciones por defecto)
- Arriba libre 250–300 px, abajo libre 300–350 px, costados ≥ 90 px (derecha ≥ 120).
- Lo clave entre y = 285 y y = 1635 (lo que se ve en el recorte 4:5 del feed).

### Por qué no escribir el ASS a mano
En libass, `\fs` es la **altura de línea**, no la de la letra. Con Poppins la letra sale ~30 % más chica de lo pedido. El motor mide cada fuente y lo compensa: `tam=100` es una letra de 100 px de verdad.

## Muestrario de recursos

```bash
python3 -m kit.muestrario crudo.mp4 marca.json salida/ PALABRA_CTA
```

`salida/muestrario.jpg` con 8 recursos aplicados al video de la persona (necesita al menos 16 s de video). Ver `docs/opciones-de-edicion.md`.

## Opciones de estilo

```bash
python3 -m kit.opciones reel crudo.mp4 marca.json "apoyo" "protagonista" salida/
python3 -m kit.opciones carrusel marca.json carrusel.json salida/
```

`salida/opciones.jpg` con 3 variantes rotuladas A, B y C para elegir. Ver `docs/referencias.md`.

## Revisión

```bash
python3 -m kit.revisar final.mp4 trabajo/pieza/revision-v1 [puntos.json]
```

Hoja con los cuadros antes / en / después de cada entrada y salida, clips de 1 s e `informe.json` con controles pendientes. Ver `docs/revision.md`.

## Carrusel

```bash
python3 -m kit.carrusel marca.json carrusel.json salida/
```

Énfasis dentro de los textos: `*palabra*` (acento en cursiva), `==frase==` (franja de color), `**palabra**` (negrita).

| Tipo | Campos | Catálogo |
|---|---|---|
| `portada` | `titulo`, `apoyo`, `foto` | portada |
| `texto` | `titulo`, `texto` | A |
| `foto` | `titulo`, `texto`, `foto`, `lado` | B |
| `cita` | `texto`, `autor` | C |
| `lista` | `titulo`, `items`, `tildes`, `iconos` (un nombre por ítem) | D / O |
| `comparacion` | `izq{titulo,items}`, `der{titulo,items}` | E |
| `dato` | `numero`, `texto` | F |
| `chat` | `titulo`, `mensajes[{de: ella/yo, texto}]` | H |
| `pasos` | `titulo`, `items` | K |
| `respiro` | `texto` | L |
| `pregunta` | `texto` | M |
| `fondo_foto` | `foto`, `titulo`, `texto` | N |
| `cierre` | `texto`, `accion` | cierre |

Cualquier placa acepta `"fondo"`. Si no se pone, el motor alterna sin repetir y usa el oscuro para el cierre. Los mockups de celular (G) y capturas enmarcadas (I) se agregan a mano en `salida/carrusel.html` cuando hacen falta.
