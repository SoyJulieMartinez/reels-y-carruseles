# Proponer opciones de edición

Además de editar lo que se pide, Claude **propone**. Muchas personas no saben qué recursos existen ni cuál le queda bien a lo que dicen. Por eso, antes de editar, Claude les muestra un menú concreto y les pregunta.

## Cuándo

- Siempre en el primer video de una persona (todavía no hay "Aprendizajes" en la ficha).
- Cuando el mensaje dice "proponeme opciones", "no sé" o deja vacío "formatos que quiero usar".
- Cuando lo que dice el video pide un recurso que todavía no usó (una enumeración, un antes y después, un dato).

Si la ficha ya tiene recursos favoritos y el pedido es claro, no se pregunta: se edita y se cuenta qué se eligió.

## Cómo

**1. Mostrar el muestrario sobre su propio video** (la primera vez, o cuando lo pide):

```bash
python3 -m kit.muestrario crudo.mp4 marca.json trabajo/<pieza>/muestrario PALABRA_DEL_CTA
```

Devuelve `muestrario.jpg` con 8 recursos aplicados a su video y con su marca: hook de portada, título escalonado, etiquetas, placa, desenfoque + lista, palabra gigante, comentario CTA y hook en mayúsculas.

**2. Armar una propuesta por momentos**, después de transcribir. Una tabla corta, con 2 opciones por momento y una recomendada:

| Segundo | Lo que dice | Opción recomendada | Otra opción |
|---|---|---|---|
| 0–3 | "tu presencia digital es malísima" | Hook editorial con palabra fantasma | Hook en mayúsculas |
| 5–10 | enumera 3 profesiones | Etiquetas flotantes | Lista con tildes sobre desenfoque |
| 18–20 | "presencial" | Placa a pantalla completa | Palabra gigante detrás de la cabeza (efectos) |
| 59–fin | CTA "escribime JORNADA" | Barra de comentario que se escribe sola | Botón de seguir que cambia a "Siguiendo" (efectos) |

Reglas para la tabla:
- Cada opción sale de lo que dice en ese momento (una enumeración pide lista o etiquetas; un número pide un dato grande; un contraste pide antes y después).
- Entre 4 y 7 momentos. No todo lleva recurso: el aire también es parte del ritmo.
- Nombrar los recursos con palabras simples, no con nombres técnicos.

**3. Preguntar** con opciones para tocar (si el entorno lo permite) o pidiendo que responda con números o letras: "¿Vamos con las recomendadas, o querés cambiar alguna?". Una sola pregunta, con todo junto.

**4. Si no responde** y hay que avanzar, editar con las recomendadas y decirlo en la entrega.

**5. Guardar lo que elige** en la ficha ("Aprendizajes"), para proponer mejor la próxima vez y no preguntar lo mismo.

## Menú completo de recursos

Para la tabla se puede elegir de cualquiera de estas fuentes. Todo se adapta a la marca.

**Motor (`kit/reel.py`), sin instalar nada más:**
hook de portada, título escalonado (dos tipografías), etiquetas flotantes, tarjetas con capturas o fotos, placa a pantalla completa, desenfoque + lista con tildes, palabra fantasma gigante, barra de comentario con la palabra clave, subtítulos con palabras destacadas, sonidos (pop, swish, ding, teclado).

**Efectos (`efectos/`, con `setup.sh --efectos`):**
- Texto y títulos: palabra gigante detrás de la persona, palabra tachada, palabra escrita con crayón, titular en caja, cartel de luces, tapa de revista, cinta con frase sobre el pecho.
- Listas y pasos: checklist que se tilda, tarjetas numeradas en abanico, interruptores que se encienden, ticket con instrucciones.
- Redes y prueba social: comentario que se escribe, botón Seguir, notificaciones de mensajes, reels que giran o se acumulan detrás, grilla del perfil, contador de seguidores, gráfico que sube.
- Cámara y clima: acercamiento a una palabra, acercamiento lento cinematográfico, foco de luz, gradación de color, antes y después con cortina, cuenta regresiva, sello, flecha dibujada.

**Sonido (`setup.sh --todo`):** sonidos realistas descritos con palabras (earshot), o diseño de sonido completo con grabaciones reales de su biblioteca (real-sfx).

**HyperFrames y skills-edicion (`setup.sh --todo`):** gráficos animados, tipografía cinética compleja, transiciones de catálogo, mockups animados.

**Del catálogo (`docs/reels.md`):** los 45 formatos, como pantalla dividida, voz en off con b-roll, fotos tipo Polaroid, video en círculo con texto curvo, bandas de cine, reloj o placa de capítulo, reels flotando, stickers de marca.

## Versiones de prueba

Si la persona quiere probar qué funciona mejor, ofrecer de 2 a 6 versiones del mismo video (`_A`, `_B`, `_C`…) para los Reels de prueba de Instagram. Cada versión cambia **una sola cosa** (el hook, un recurso o el estilo de subtítulos) y en la entrega se anota qué cambia en cada una, para saber qué funcionó.
