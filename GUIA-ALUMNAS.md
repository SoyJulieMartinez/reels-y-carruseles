# Guía para alumnas: tu editora de reels y diseñadora de carruseles con Claude

Al terminar vas a tener, en Claude, tu propia editora de reels y diseñadora de carruseles: le pasás tu video o tu texto, le escribís un mensaje corto y te lo devuelve con tus colores, tus tipografías y tu estilo. No hace falta saber editar ni programar.

**Vos no editás: dirigís.** Claude hace el trabajo y vos decidís cómo se ve tu marca, revisás y pedís cambios.

## La forma más fácil (sin leer nada)

Abrí un chat en Claude y escribí:

> Instalá esto https://github.com/SoyJulieMartinez/reels-y-carruseles y decime paso a paso cómo editar un reel

(o "diseñar un carrusel"). Claude instala todo y te va guiando de a un paso. Si preferís no hacer nada de pasos, subí tu video al chat, escribí "editalo con este sistema" y pasale tu logo o tus colores cuando te los pida.

El resto de esta guía es para cuando quieras dejar todo armado en un Proyecto y que salga todavía mejor.

## Qué necesitás

- [ ] Una cuenta de Claude (sirve la gratuita; con un plan pago podés hacer más videos por día).
- [ ] La compu, o el celular si no tenés compu.
- [ ] Un video vertical tuyo hablando a cámara, de 30 a 60 segundos.
- [ ] Tus colores (en código HEX, por ejemplo #F8568D) y el nombre de tus tipografías. Si tenés brand kit o logo, también.
- [ ] Si querés, los links de 2 o 3 reels o carruseles de otras cuentas que te gusten. Si no tenés, Claude te muestra opciones.

## Antes de grabar

Un buen video empieza en la grabación (más detalle en `docs/grabacion.md`):

1. **Luz:** natural, de frente o de costado. Nunca de espaldas a la ventana.
2. **Fondo:** con algo de interés (una planta, un cuadro), pero ordenado.
3. **Encuadre:** vertical, con la grilla activada, tus ojos en el tercio de arriba y aire sobre tu cabeza para el título.
4. **Lente limpia** y, en iPhone, el video HDR apagado.
5. **Un segundo de silencio** antes de empezar y al terminar.
6. **Banco de tomas de apoyo:** una vez al mes, una hora grabando 30 clips cortos (tus manos trabajando, tu escritorio, un café). Subilos a tu Proyecto.

## Paso a paso: armá tu Proyecto (una sola vez)

1. **Activá los archivos.** En Configuración → Capacidades, prendé "Ejecución de código y creación de archivos" (en algunas versiones se llama "Crear y editar archivos"). Sin esto, Claude no puede editar video.
2. **Creá tu Proyecto.** Proyectos → Nuevo proyecto → "Mi editora de reels y carruseles".
3. **Completá tu ficha de estilo.** Descargá `plantillas/ficha-de-estilo.md` de este repositorio y llenala: colores, tipografías, tono, subtítulos, formatos favoritos y lo que no querés ver nunca. Lo que no sepas, dejalo vacío.
4. **Subí al Proyecto** tu ficha completa, tu brand kit y tu logo (si los tenés) y tus tipografías si no son de Google Fonts.
5. **Pegá las instrucciones.** Copiá todo el texto de `plantillas/instrucciones-del-proyecto.txt` y pegalo en "Instrucciones del proyecto". En cada chat, Claude descarga este sistema solo.

Todo se pide dentro de este Proyecto. En un chat suelto, Claude no conoce tu estilo.

## La biblioteca de recursos

Si no tenés referencias o no sabés qué pedir, abrí `biblioteca/biblioteca-de-recursos.html` del repositorio (descargalo y abrilo en tu navegador). Tiene todo lo que el sistema sabe hacer, por nombre: ritmo, tipos de video, estilos de hook y subtítulos, títulos, 51 efectos, transiciones, sonidos, colores, cierres, íconos y composiciones de carrusel. Tocás lo que te gusta, agregás una nota y copiás el pedido para pegarlo con tu video.

## Tu primer reel

Abrí un chat nuevo dentro del Proyecto, adjuntá el video y pegá el mensaje de `plantillas/mensaje-para-pedir-un-video.txt`, completando lo que corresponda. Si no sabés qué recursos usar, escribí "no sé: proponeme opciones": Claude te muestra un muestrario con recursos aplicados a tu propio video y una tabla con opciones para cada momento.

**Tip para el hook:** si no se te ocurre, pedí "Proponeme 3 hooks para este video" y elegí uno. Fórmulas que funcionan: contraste, error común, promesa concreta, pregunta directa, resultado primero y curiosidad.

## Tu primer carrusel

En un chat nuevo del mismo Proyecto, adjuntá tus fotos o capturas y pegá el mensaje de `plantillas/mensaje-para-pedir-un-carrusel.txt` con tu texto separado por placa. **Claude solo hace el diseño: tu texto no se cambia.** Te devuelve un PNG por placa y un PDF.

Composiciones del catálogo (podés elegir tus favoritas por letra en la ficha):

| Letra | Composición | Sirve para |
|---|---|---|
| A | Texto grande solo, con mucho aire | Frases fuertes |
| B | Texto + tu foto fundida con el fondo | Cercanía, historias |
| C | Cita destacada con comillas grandes | Frases tuyas, testimonios |
| D | Lista con íconos o números grandes | Consejos, beneficios |
| E | Comparación: antes/después, mito/realidad | Mostrar un cambio |
| F | Dato grande: un número protagonista | Resultados |
| G | Mockup de celular o laptop con una captura real | Mostrar tu trabajo |
| H | Mockup de chat | Hablar de conversaciones |
| I | Captura real enmarcada | Reseñas, comentarios |
| J | Franja de color detrás de la frase clave | Destacar una idea |
| K | Paso a paso numerado | Tutoriales |
| L | Placa "respiro": una frase corta | Pausa entre placas cargadas |
| M | Pregunta grande a tu audiencia | Generar comentarios |
| N | Foto de fondo desenfocada con texto encima | Portadas, cierres |
| O | Checklist con tildes | Requisitos, listas de control |

## Extra: del reel a 2 carruseles

Un reel que ya grabaste puede convertirse en dos carruseles nuevos. Es el **único caso en que Claude escribe el contenido**, y solo cuando se lo pedís con `plantillas/mensaje-del-reel-a-carruseles.txt`. Cada carrusel tiene un objetivo, un hook en la placa 1, un segundo hook en la placa 2 (Instagram suele volver a mostrar el carrusel desde ahí) y un llamado a la acción alineado con el objetivo. Primero te muestra el texto; lo diseña cuando lo aprobás.

## Revisar y pedir cambios

Claude revisa todo antes de mostrártelo, pero el ojo final es tuyo. Mirá el resultado en el celular, como lo va a ver tu audiencia, y tildá:

- [ ] El hook se ve completo desde el primer cuadro (es la portada en tu feed) y se entiende sin audio.
- [ ] Ningún texto queda debajo de los botones, del nombre de usuario ni del texto del posteo.
- [ ] Ningún texto tapa tu cara.
- [ ] Los subtítulos se leen bien en todo el video.
- [ ] Los títulos de dos líneas no tienen hueco en el medio.
- [ ] Los nombres y las palabras están bien escritos.
- [ ] Solo hay colores y tipografías de tu marca.
- [ ] El cierre pide una sola acción y el audio no se corta.
- [ ] **Prueba anti-genérico:** si tapás tu @, ¿se nota que es tuyo?

**Para pedir cambios, usá la fórmula: dónde + qué + cómo lo querés + por qué.**

| En vez de… | Pedí… |
|---|---|
| "No me gusta" | "En el segundo 2, el hook se ve chico; hacelo el doble de grande porque es lo primero que leen." |
| "Cambiale los subtítulos" | "Los subtítulos tapan mi boca en el segundo 14; bajalos al pecho." |
| "Hacelo más lindo" | "En la parte de la lista, desenfocá el fondo y poné íconos al lado de cada punto." |
| "Está muy cargado" | "Sacá la placa del segundo 30 y dejá solo los subtítulos." |
| En un carrusel | "En la placa 3, la foto me tapa el título; ponela a la derecha porque el título es lo más importante." |

Mandá todos los cambios juntos en un solo mensaje. Cuando te guste, escribí "Aprobado, actualizá mi ficha con lo que aprendiste" y reemplazá la ficha de tu Proyecto por la versión nueva.

## Preguntas frecuentes

- **¿Tengo que instalar algo?** No. Claude descarga e instala el sistema solo en su espacio de trabajo; vos subís el video y descargás el resultado.
- **¿Sirve la cuenta gratuita?** Sí: los Proyectos y la creación de archivos están en todos los planes. Con la gratuita vas a poder hacer menos videos por día y crear hasta 5 Proyectos.
- **¿Y si no sé mis colores o tipografías?** Pedí "Proponeme 3 paletas y 3 combinaciones de tipografías para mi marca" y elegí.
- **No sé qué estilo quiero.** Escribí "proponeme opciones": te muestra 3 estilos y un muestrario de recursos aplicados a tu propio video.
- **Mi video de iPhone sale lavado.** Claude lo corrige solo; para la próxima, grabá con el HDR apagado.
- **¿Puedo usar música?** Sí, si se la pasás vos. Claude no baja música de internet.
- **Claude no puede abrir el link de mi referencia.** Mandale una grabación de pantalla o capturas.
- **Tardó mucho o se cortó.** Escribí "Seguí desde donde quedaste" en el mismo chat.
