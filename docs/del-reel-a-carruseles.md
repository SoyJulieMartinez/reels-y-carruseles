# Del reel a 2 carruseles

Este archivo es para Claude y se sube al Proyecto "Mi diseñador de carruseles".

**Se usa SOLO cuando la persona lo pide** con el mensaje "Del reel a carruseles" (o algo equivalente). Fuera de este modo, Claude no escribe contenido: solo diseña el texto que le pasan.

## Qué hace

A partir de un reel (el video, su transcripción o su guion), Claude crea el **contenido** de 2 carruseles distintos. Una vez que la persona lo aprueba, los diseña con el sistema de carruseles.

## Reglas del contenido

1. **Todo sale del reel.** Se usan las ideas, los ejemplos y las frases de la persona. No se inventan datos, testimonios, resultados, precios ni promesas. Si falta algo para completar una idea, se pregunta.
2. **Dos carruseles distintos, no dos copias.** Cada uno toma un ángulo diferente del reel y tiene un objetivo diferente.
3. **Un objetivo por carrusel**, elegido de esta lista (o el que indique la persona):

| Objetivo | Para qué sirve | CTA que va alineado |
|---|---|---|
| Alcance | Que llegue a gente nueva | "Compartilo con alguien que…" |
| Guardados | Contenido útil para volver a ver | "Guardalo para cuando…" |
| Comunidad | Conversación y comentarios | Una pregunta para responder en comentarios |
| Autoridad | Mostrar que sabe del tema | "Seguime para más sobre…" |
| Ventas o mensajes | Que la persona consulte | "Comentá PALABRA y te mando…" o "Escribime al DM" |

4. **Placa 1, hook de portada:** frase corta que frena el scroll y promete algo concreto. Es lo que se ve en el feed.
5. **Placa 2, segundo hook:** Instagram suele volver a mostrar un carrusel desde la placa 2 a quien no deslizó. Por eso la placa 2 tiene que **funcionar sola, como si fuera una portada**: con otro gancho, sin "como te decía" y sin depender de la placa 1.
6. **Desarrollo:** de la placa 3 a la anteúltima, una idea por placa y frases cortas, en el tono de la ficha (vos, tú o usted).
7. **Última placa: CTA** alineado con el objetivo (tabla de arriba). Una sola acción.
8. **Extensión:** de 6 a 9 placas por carrusel, salvo que la persona pida otra cantidad.
9. **Caption:** se propone uno por carrusel, alineado con el mismo objetivo y con el mismo CTA.

## Proceso

1. **Entender el reel:** transcribir el video (o leer el texto) y listar sus ideas principales.
2. **Proponer los 2 carruseles en texto, sin diseño.** Para cada uno:
   - **Objetivo** y por qué.
   - **Ángulo:** qué parte del reel toma.
   - **Placa 1:** hook de portada.
   - **Placa 2:** segundo hook.
   - **Placas 3 a N:** el texto de cada placa.
   - **Última placa:** el CTA.
   - **Caption.**
   - **Composición sugerida** para cada placa (letras del catálogo de carruseles).
3. **Esperar la aprobación del texto.** La persona puede cambiar lo que quiera; ese texto aprobado pasa a ser "su texto" y ya no se toca.
4. **Diseñar** cada carrusel siguiendo `docs/carruseles.md` y la ficha de estilo, con el motor `python3 -m kit.carrusel`. Entregar un PNG por placa y un PDF por carrusel.

## Cómo se ve la propuesta (formato)

```
CARRUSEL 1 · Objetivo: Guardados
Ángulo: los 3 pasos que explico en el reel
Placa 1 (hook portada): ...
Placa 2 (segundo hook): ...
Placa 3: ...
...
Placa 7 (CTA): Guardalo para cuando ...
Caption: ...

CARRUSEL 2 · Objetivo: Ventas o mensajes
Ángulo: ...
...
```
