# Reels y carruseles con Claude

Un sistema para que Claude edite tus reels y diseñe tus carruseles **con tu marca**, sin que parezcan hechos con inteligencia artificial.

> **Si sos Claude y te pasaron este link:** cloná el repositorio (`git clone --depth 1 https://github.com/SoyJulieMartinez/reels-y-carruseles.git ~/kit-rc`), corré `bash setup.sh` y seguí `docs/arranque.md`. Guiá a la persona de a un paso o, si subió su material sin explicar nada, hacé vos todo el trabajo y preguntale solo su identidad visual.

Creado por **Julie Martínez** · [@soyjuliemartinez](https://instagram.com/soyjuliemartinez)

---

## Empezá por acá

- **La forma más fácil:** abrí un chat en Claude y escribí: *"Instalá esto https://github.com/SoyJulieMartinez/reels-y-carruseles y decime paso a paso cómo editar un reel"* (o un carrusel). Claude instala todo y te guía. También podés subir tu video directo y decir *"editalo"*: Claude se encarga del resto y solo te pregunta tu identidad visual.
- **¿No sabés qué pedir?** Abrí la [biblioteca de recursos](biblioteca/biblioteca-de-recursos.html) (descargala y abrila en el navegador): elegís tipo de video, efectos, sonidos y cierre tocando, y te arma el pedido para copiar.
- **Si sos alumna:** leé [GUIA-ALUMNAS.md](GUIA-ALUMNAS.md).
- **Si vas a enseñarlo:** `clase/guia-para-ensenar.md` y las diapositivas `clase/clase-editar-reels-con-claude.html` (se abren en el navegador).

## Qué hay adentro

| Carpeta | Para qué sirve |
|---|---|
| `docs/reels.md` | Reglas fijas de edición (márgenes, hook, subtítulos) + catálogo de 45 formatos de reel |
| `docs/carruseles.md` | Reglas de diseño de carruseles + catálogo de composiciones A–O |
| `docs/del-reel-a-carruseles.md` | Cómo convertir un reel en 2 carruseles con objetivo, doble hook y llamado a la acción |
| `docs/trabajo-agentico.md` | Cómo trabaja Claude: director, operador y revisor, orden de carpetas y continuidad entre chats |
| `docs/revision.md` | Revisión interna antes de mostrarte un video |
| `docs/herramientas-extra.md` | Cuándo usar HyperFrames, skills-edicion y Watch |
| `docs/grabacion.md` | Cómo grabar para que la edición luzca: luz, fondo, encuadre, banco de tomas de apoyo |
| `docs/opciones-de-edicion.md` | Cómo te propone Claude recursos de edición para cada momento de tu video |
| `docs/referencias.md` | Cómo usa Claude tus links de referencia, y qué opciones te muestra si no tenés o dudás |
| `biblioteca/` | La biblioteca de recursos: todo lo que el sistema sabe hacer, para elegir por nombre (242 recursos) |
| `docs/biblioteca-de-recursos.md` | La misma biblioteca para Claude: qué es cada código y con qué se hace |
| `docs/motor.md` | Todas las funciones del motor |
| `kit/` | El motor: subtítulos, títulos, tarjetas, íconos, sonidos, opciones, muestrario, revisión y carruseles en PNG y PDF |
| `efectos/` | 51 efectos que siguen la cara: texto detrás de la persona, órbitas, widgets, cajas de comentario y más |
| `clase/` | Diapositivas de la clase de 2 horas y guía para enseñar (clase única o curso de 5 clases) |
| `docs/muestras/` | Imágenes de muestra de formatos, íconos y un carrusel |
| `plantillas/` | Tu ficha de estilo, las instrucciones del Proyecto y los mensajes para pedir cada cosa |
| `ejemplos/` | Una marca de ejemplo, un reel completo y dos carruseles de muestra |

## Cómo se usa (sin saber programar)

0. **Activá los archivos en Claude:** Configuración → Capacidades → "Ejecución de código y creación de archivos".
1. **Completá tu ficha de estilo:** descargá `plantillas/ficha-de-estilo.md` y llenala con tus colores, tipografías, tono y referencias.
2. **Creá un Proyecto en Claude** (claude.ai → Proyectos → Nuevo).
3. **Pegá las instrucciones:** copiá el contenido de `plantillas/instrucciones-del-proyecto.txt` en las instrucciones del Proyecto.
4. **Subí tu ficha** a los archivos del Proyecto.
5. **Abrí un chat nuevo** dentro del Proyecto, subí tu video y pegá el mensaje de `plantillas/mensaje-para-pedir-un-video.txt` completado.
   - Para un carrusel: `mensaje-para-pedir-un-carrusel.txt`.
   - Para sacar carruseles de un reel: `mensaje-del-reel-a-carruseles.txt`.
6. **Pedí cambios** con la fórmula: *momento o placa + qué + cómo + por qué*.
   Ejemplo: "En el segundo 12, el título tapa mi cara; subilo porque la cara tiene que verse".

Claude instala todo solo al empezar cada chat (la primera vez tarda unos minutos).

## Qué resuelve el motor por vos

- **Letra del tamaño real:** los subtítulos y títulos salen del tamaño que pedís, sin quedar "re chiquitos".
- **Zonas seguras de Instagram:** nada importante queda debajo de los botones ni fuera del recorte del feed.
- **Hook de portada:** completo desde el primer cuadro, para que se lea en el feed.
- **Efectos que terminan justo en los cortes de cámara**, así las transiciones quedan prolijas.
- **Tu tipografía:** se baja sola de Google Fonts, cualquier familia.
- **Sonidos:** pop, swish, ding y teclado listos para usar, y sonidos realistas de cualquier cosa con las herramientas extra.
- **Te propone recursos:** un muestrario con 8 recursos aplicados a tu propio video y una tabla con opciones para cada momento, para que elijas.
- **Opciones para elegir:** si no tenés referencias o dudás, te muestra 3 estilos aplicados a tu propio video o a tu propio texto.
- **Revisión antes de mostrarte nada:** cuadros antes y después de cada transición, clips cortos y una lista de controles.
- **Carruseles listos para subir:** PNG por placa + PDF, con revisión automática de textos chicos, márgenes y fondos repetidos.

## Para usarlo desde la terminal

```bash
git clone https://github.com/SoyJulieMartinez/reels-y-carruseles.git && cd reels-y-carruseles
bash setup.sh
python3 -m kit.transcribir mi-video.mp4 palabras.json
python3 ejemplos/ejemplo_reel.py mi-video.mp4 palabras.json final.mp4
python3 -m kit.carrusel ejemplos/marca-ejemplo.json ejemplos/carrusel-ejemplo.json salida/
```

Requiere Python 3.10+ y ffmpeg con libass.

## Extras opcionales

- `bash setup.sh --todo` suma además [HyperFrames](https://github.com/heygen-com/hyperframes), [skills-edicion](https://github.com/NexumAI-online/skills-edicion) y [Watch](https://github.com/bradautomates/claude-video), [earshot](https://github.com/Leonxlnx/earshot) (sonidos realistas) y [real-sfx](https://github.com/Clipwing/skills) (diseño de sonido con tu biblioteca), instalados desde sus repositorios oficiales (ver `docs/herramientas-extra.md`).
- `bash setup.sh --efectos` prepara la carpeta `efectos/`: texto detrás de la persona, recortes, marcos, widgets y 51 efectos en total (guía en `efectos/GUIA.md`).

## Licencia

MIT: podés usarlo, adaptarlo y compartirlo, manteniendo el aviso de autoría. Las tipografías (Google Fonts y las de `efectos/fonts`) tienen su propia licencia OFL, y los modelos de `efectos/models` las suyas (ver `efectos/models/NOTICE.md`).
