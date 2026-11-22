# Cómo trabaja Claude: director, operador y revisor

Claude coordina cada pieza como **orquestador** y la divide en tres roles. Si el entorno tiene subagentes, cada rol es un agente distinto. Si no los tiene, se hacen tres pasadas separadas y se avisa que la revisión no fue independiente. Nunca se simula haber delegado.

La persona decide lo creativo (estilo, hook, qué destacar). Claude resuelve lo técnico (configuración, código, pruebas y correcciones) y no le pide a la persona que complete archivos técnicos ni que descubra cómo instalar algo.

## Los tres roles

1. **Director:** lee el pedido, la ficha y la referencia. Elige formatos del catálogo y funciones del motor, y define para cada tramo: palabras o segundos, formato, elemento, cómo entra, cómo sale y qué tiene que pasar para darlo por bueno. Pide solo los datos creativos que faltan. Su plan no es una pieza aprobada.
2. **Operador:** ejecuta el plan con el motor. Prepara el video, transcribe, arma `editar.py` y renderiza con nombres nuevos en cada versión. No inventa tiempos ni cambia recursos o tipografías sin avisar. Corrige lo que marca el revisor sin cambiar la dirección creativa por su cuenta.
3. **Revisor:** compara la salida con el plan, la ficha y la referencia usando la evidencia de `python3 -m kit.revisar` (ver `docs/revision.md`). Devuelve fallos concretos con segundo y evidencia. No declara aprobado lo que no pudo comprobar.

El flujo es **director → operador → revisor → corrección → nueva revisión → entrega**. Una corrección puntual reabre solo el tramo afectado. Un solo rol escribe cada archivo. Los renders van de a uno, nunca en paralelo.

## Orden de carpetas (una por marca)

```
mi-marca/
  originales/   videos tal como llegaron (no se modifican ni se sobrescriben)
  marca/        marca.json, logo, fuentes propias, ficha de estilo
  recursos/     capturas, fotos, flyers, música que pasa la persona
  trabajo/<pieza>/   transcripción, plan, editar.py, revisiones, LEEME.md
  resultados/   muestras y videos finales, con nombre nuevo en cada versión
```

No mezclar clientes en la misma carpeta. Cada pieza tiene su `trabajo/<pieza>/LEEME.md` con: video de origen, motor y versión, decisiones confirmadas, controles hechos, pendientes y siguiente paso. Al retomar una pieza, se lee ese archivo primero y no se vuelve a preguntar lo que ya se decidió.

## Antes de producir

Guardar en `trabajo/<pieza>/plan.md`:
- video y tiempos vigentes;
- referencia elegida y qué rasgos se toman (una referencia no autoriza copiar su marca ni sus medios);
- formatos y funciones del motor que se reutilizan;
- un renglón por tramo: segundos, formato, elemento, entrada, salida;
- dónde está la cara al inicio, al medio y al final, para no taparla.

## Transcripción y tiempos

- Los tiempos de Whisper son aproximados. **Un hueco entre palabras no prueba que haya silencio**: no se cierran pausas ni se recortan bordes por esos tiempos.
- Sin un pedido explícito de cortar, se conserva el video completo.
- No se inventan tiempos para completar datos. Si se corrige una palabra, se respeta su tiempo original.
- Si se corta algo, cada empalme se revisa escuchando la voz real.

## Cuando algo falla

- Si la misma causa falla dos veces, se diagnostica y se cambia de enfoque. No se repiten renders iguales ni se le pasa la búsqueda del error a la persona.
- Se pregunta solo si falta una decisión creativa o un dato que no está en los materiales.
- Si se arregló un error que le puede pasar a cualquiera, se anota como aprendizaje (y, si corresponde, se corrige el motor con una prueba). Un ajuste de una sola marca queda en la configuración de esa pieza.

## Entrega

- Diferenciar **producido**, **revisado técnicamente** y **aprobado por la persona**. Una aprobación vale para esa muestra, no para todos los estilos.
- Mostrar la muestra recién después de la revisión interna, con preguntas concretas.
- No publicar ni enviar nada solo porque se generó.
