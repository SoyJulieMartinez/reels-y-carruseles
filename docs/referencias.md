# Referencias y opciones

Cada pedido puede venir con links de reels o carruseles que le gustan a la persona, sin ninguno, o con dudas. En los tres casos, Claude ayuda a decidir el estilo antes de producir.

## 1. Si manda links de referencia

**Abrirlos:**
- Reels de Instagram: desde el espacio de trabajo no se pueden descargar. Usar el navegador (integrado o Chrome) con la versión `https://www.instagram.com/reel/<ID>/embed/`, que se reproduce sin iniciar sesión. Pausar en 8 a 12 momentos y sacar capturas.
- Carruseles: abrir `https://www.instagram.com/p/<ID>/embed/` y recorrer las placas con las flechas.
- TikTok, YouTube u otros: igual, con el navegador.
- Si no hay navegador o no carga, pedir capturas o una grabación de pantalla. Si la referencia llega como archivo, usar Watch (`docs/herramientas-extra.md`).

**Sacar los rasgos, no el contenido.** Anotar en una lista corta:
- Reel: cuántas palabras de subtítulo por vez, tamaño y posición; tipografías (sans / serif / script, mayúsculas); dónde va el hook; placas, tarjetas, desenfoques; ritmo de cortes y zoom; cómo cierra.
- Carrusel: composición de portada, cantidad de texto por placa, uso de fotos, fondos, cómo destaca, cómo cierra.

**Confirmar en 3 líneas** qué se va a tomar de la referencia y qué se adapta a la marca. Nunca se copian colores, logos, tipografías ni medios de la referencia: se copia el lenguaje visual con la marca de la persona.

Si hay varias referencias que se contradicen, señalarlo y proponer una combinación.

## 2. Si no tiene referencias o duda

Primero, ofrecerle la **biblioteca de recursos** (`biblioteca/biblioteca-de-recursos.html`): elige por nombre el ritmo, el tipo de video, los efectos, los sonidos y el cierre, y pega el pedido con los códigos. Cada código está explicado en `docs/biblioteca-de-recursos.md`.

Si prefiere ver antes de elegir:

No preguntar "¿qué estilo querés?" en el aire. **Mostrar opciones:**

- **Reel:** 3 portadas del mismo hook sobre su propio video, en 3 estilos:
  ```bash
  python3 -m kit.opciones reel crudo.mp4 marca.json "frase de apoyo" "palabra protagonista" trabajo/<pieza>/opciones
  ```
  A · Editorial (serif en cursiva + palabra fantasma), B · Impacto (mayúsculas), C · Contraste (fondo desenfocado y texto claro).
- **Carrusel:** las 2 primeras placas, con su mismo texto, en 3 direcciones:
  ```bash
  python3 -m kit.opciones carrusel marca.json carrusel.json trabajo/<pieza>/opciones
  ```
  A · Luminosa, B · Intensa, C · Color de marca.

Junto con la imagen, sugerir **2 o 3 formatos del catálogo** que encajen con el objetivo y lo que dice (por ejemplo: "como enumerás 3 trabas, iría bien una lista con íconos (11) o etiquetas flotantes (5)"), con una línea de por qué.

La persona elige, mezcla ("A con los colores de C") o pide otra ronda. Si no responde y hay que avanzar, seguir con la opción que mejor cumple la ficha y decir cuál se eligió.

## 3. Guardar lo aprendido

Cuando elige, proponer el texto para la ficha de estilo ("Aprendizajes"): qué estilo eligió, para qué tipo de contenido y qué no le gustó. Así la próxima vez se arranca desde ahí y las opciones se acercan más a su gusto.

## Lo que no se hace

- No inventar links de cuentas o videos "de referencia": si se sugieren referencias, describir qué buscar (por ejemplo: "reels de marcas de bienestar con títulos en serif y fondo claro"), no direcciones que pueden no existir.
- No bajar música, fotos ni videos de las referencias.
