# Revisión antes de mostrar una muestra

La persona no tiene que descubrir errores técnicos previsibles. Antes de mostrarle un video, el revisor junta evidencia y la mira.

## 1. Juntar evidencia

```bash
python3 -m kit.revisar resultados/reel_v1.mp4 trabajo/<pieza>/revision-v1
```

Si el video salió de `kit.reel`, el render deja `reel_v1.mp4.puntos.json` con cada momento en que algo entra o sale, y `kit.revisar` lo usa solo. También se puede pasar una lista propia de segundos: `[1.25, 3.4, 10.23]`.

Genera, sin tocar el video:
- `hoja.jpg`: inicio, final y, en cada punto, el cuadro anterior, el del punto y el siguiente;
- `clips/`: un clip de 1 segundo alrededor de cada punto, para ver el movimiento completo;
- `informe.json`: huella SHA-256 del archivo, datos técnicos y la lista de controles en estado *pendiente*.

Cada revisión usa una carpeta nueva (`revision-v2`, `v3`…). La herramienta no pisa una existente.

## 2. Revisar de verdad

Abrir la hoja, los clips y el video completo. Marcar cada control como **aprobado**, **falló** o **pendiente**, con evidencia (segundo, cuadro o clip) y la corrección necesaria:

- **Hook:** completo y legible en el cuadro 0.
- **Subtítulos:** coinciden con la voz, aparecen a tiempo, no se cortan ni tapan otra cosa.
- **Movimiento:** cada entrada y salida de cada elemento repetido, no solo de la primera tarjeta. Que una tarjeta aparezca en una foto no prueba que haya entrado bien.
- **Transiciones:** los dos lados de cada cambio, sin flashes ni escenas anticipadas; los efectos terminan en el corte de cámara.
- **Encuadre:** cara, pelo y manos sin tapar; nada en las zonas que tapa Instagram.
- **Marca:** tipografías, colores y contraste.
- **Congruencia:** cada gráfico o captura corresponde a lo que se dice. No reemplazar un recurso real por una interfaz genérica sin avisar.
- **Audio:** volumen parejo, sonidos que no tapan la voz, sincronía.
- **Archivo:** comienzo, final y duración correctos.

Si el entorno no permite mirar imágenes o escuchar, ese control queda **pendiente**: leer el JSON no reemplaza mirar. Un render que terminó sin errores no es una aprobación.

## 3. Corregir y volver a revisar

El operador corrige, se renderiza con nombre nuevo y el revisor vuelve a mirar el tramo afectado. Recién ahí se muestra la muestra a la persona, diciendo qué se comprobó y qué quedó pendiente.

## Carruseles

`python3 -m kit.carrusel` ya revisa solo textos de menos de 30 px, márgenes y fondos repetidos, y deja `revision.jpg`. Igual hay que mirarla: caras tapadas, renglones de una sola palabra y composiciones repetidas se ven a ojo.
