# Herramientas extra

El motor de este repositorio alcanza para la mayoría de los reels. Para animaciones más complejas o para mirar videos de referencia, se suman tres herramientas gratuitas que se instalan desde sus repositorios oficiales:

```bash
bash setup.sh --todo
```

Quedan en `~/kit-rc-extras/` y sus skills en `~/.claude/skills/`. Si alguna no se instala, se sigue sin ella: el motor principal no las necesita.

## Cuándo usar cada una

| Necesidad | Herramienta |
|---|---|
| Reel con subtítulos, títulos, tarjetas, placas, checklist, CTA | Motor `kit/reel.py` (vía principal) |
| Texto detrás de la persona, recortes, widgets que siguen la cara | `efectos/` |
| Mirar un crudo o una referencia que llegó como archivo | **Watch** |
| Gráficos animados, tipografía cinética compleja, transiciones de catálogo, mockups animados, video armado desde una web | **HyperFrames** (`hyperframes` + `hyperframes-registry`) |
| Tarjetas animadas prehechas, beats de video, cortes de silencios y errores con revisión | **skills-edicion** (`style-library`, `hyperframes-video-beats`, `cut-silences`, `cut-mistakes`) |
| Diapositivas para una clase | `slideshow` (HyperFrames) |

## Watch

Saca cuadros del video con su minuto para poder mirarlo:

```bash
python3 ~/.claude/skills/watch/scripts/watch.py --engine local --no-whisper --detail balanced --out-dir trabajo/<pieza>/watch video.mp4
```

El texto se toma de `kit.transcribir` (Watch transcribe solo con claves de servicios pagos). Con links de Instagram no funciona: para referencias de Instagram, pedir el archivo o capturas.

## HyperFrames y skills-edicion

- Las skills de skills-edicion están en `~/kit-rc-extras/skills-edicion/.claude/skills/<nombre>/SKILL.md`: se leen y se trabaja desde esa carpeta (sus scripts usan rutas relativas).
- Su marca por defecto no es la de la persona: siempre reemplazarla por la de `marca.json` (colores y tipografías) en el `DESIGN.md` o `assets/brand-tokens.css` del proyecto.
- Para renderizar hace falta un navegador. `setup.sh --todo` imprime las variables `PRODUCER_HEADLESS_SHELL_PATH` y `HYPERFRAMES_BROWSER_PATH`: exportarlas en **cada** comando de render.
- Su transcripción usa un servicio pago: usar `palabras.json` de `kit.transcribir` y convertirlo al formato que pida la skill.
- Lo que dependa de servicios de HeyGen (avatares, voz generada) necesita cuenta y créditos propios.

## Cómo combinar con el motor

Renderizar la animación de HyperFrames como un clip aparte (1080 × 1920, 30 fps) y después:
- superponerla con `r.tarjeta(...)` si es un PNG o una captura, o
- insertarla en el crudo antes de pasarlo a `Reel`, en el tramo donde corresponde.

Después, como siempre: `kit.revisar` y la revisión de `docs/revision.md`.

## Servicios externos opcionales (con cuenta y saldo de la persona)

Nada de esto hace falta para el sistema. Se ofrece solo si la persona ya tiene la cuenta y lo pide.

| Servicio | Para qué | Cómo se usa |
|---|---|---|
| ElevenLabs | Transcripción con tiempos por palabra (alternativa a Whisper) | Con su propia clave en un archivo `.env` local. Antes de enviar el audio, decirle qué se sube y pedir permiso. Si Whisper falla, no se pasa a un servicio pago sin preguntar. |
| Higgsfield | Generar imágenes o clips de apoyo | Solo con su cuenta y por pedido explícito. Lo generado se guarda en `recursos/` anotando de dónde salió. |
| Magnific | Generar, editar o ampliar imágenes | Igual que Higgsfield. |

Reglas: nunca escribir claves en el código, el chat, las guías ni los archivos que se comparten (el `.gitignore` ya excluye `.env`). No generar imágenes, clips ni música solo porque haya una clave disponible. Explicar el consumo antes de usarlo.

## Normalizar el video antes de editar

El motor ya convierte los videos HDR de iPhone (HLG o PQ) a SDR BT.709, aplica la rotación, fija 30 fps constantes y pasa el audio a AAC 48 kHz, sobre una copia (el original no se toca). Además:

- Si hay varias pistas de audio o micrófonos, revisar primero cuál es la voz.
- **Dolby Vision o LOG** necesitan otra ruta: sacar una muestra de color, mostrarla y no seguir hasta que se vea bien.
- Si el ffmpeg de la computadora no tiene el filtro `zscale` (hace falta para HDR), se puede usar uno aislado: `pip install imageio-ffmpeg` y usar la ruta que devuelve `python3 -c "import imageio_ffmpeg; print(imageio_ffmpeg.get_ffmpeg_exe())"`.
- Nunca "marcar" un video HDR como SDR sin convertirlo: se ve lavado.
