"""Ejemplo de ritmo "Muy dinámico" (R3 de la biblioteca): un cambio visual cada ~3 s.

Dos pasos:
  1. Efectos sobre el crudo (12 efectos de efectos/ en una sola pasada):
     efectos/.venv/bin/python efectos/scripts/fx.py --plan ejemplos/efectos-plan-dinamico.json crudo.mp4 con_efectos.mp4
  2. Motor encima (títulos, etiquetas, placas, íconos, sonidos, subtítulos):
     python3 ejemplos/reel_dinamico.py con_efectos.mp4 palabras.json final.mp4
Los tiempos son los del reel de ejemplo: con otro video, se rehacen según su transcripción.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from kit.reel import Reel, hoja_de_contacto, portada

BASE, PALABRAS, SALIDA = sys.argv[1:4]
r = Reel(BASE, os.path.join(os.path.dirname(os.path.abspath(__file__)), "marca-julie.json"))

# 0.0–3.6 · Hook = portada (quieto desde el cuadro 0) + acercamiento en "malísima" (efecto)
r.hook("tu presencia digital es", "malísima", fantasma="MALÍSIMA")

# 3.7–5.1 · "INVERTIR" tachado (efecto)
# 5.1–7.4 · Etiquetas de lo que no se puede pagar
r.chip(5.10, 7.40, 330, 330, "community manager", rot=-3)
r.chip(6.00, 7.40, 760, 450, "diseñador web", rot=3)
r.ocultar(5.10, 7.40)

# 7.4–10.23 · Blanco y negro (efecto) + título
r.titulo(7.45, 9.30, 10.23, "lo que sea que necesites en", "marketing digital", tam_apoyo=70, tam_prot=150)

# 10.23–13.5 · Encuadre "MI CEREBRO" (efecto) · 13.56–15.8 · acercamiento lento (efecto)

# 15.84–17.98 · Título del servicio
r.titulo(15.84, 16.24, 17.98, "en una jornada", "estratégica 1:1", tam_prot=170, fantasma="1:1")

# 17.98–20.15 · Placa oscura
r.placa(17.98, 20.15)
r.texto(17.98, 20.15, 540, 760, "sí, como escuchaste bien", "sans", 300, 80, "claro", modo="placa")
r.fantasma(19.14, 20.15, 540, 930, "presencial", tam=320, color="acento_suave", alfa="EC")
r.texto(19.14, 20.15, 540, 920, "presencial", "acento", 500, 220, "acento_suave", italica=True, modo="placa")

# 20.18–23.6 · "CREAR" detrás de la cabeza (efecto)
# 23.68–25.15 · Título
r.titulo(23.68, 24.38, 25.15, "y lo vas a ver", "conmigo")

# 25.2–28.15 · Cartel de luces "VAS A APRENDER" (efecto)
# 29.0–31.1 · Ejemplo
r.titulo(29.02, 30.28, 31.10, "ejemplo:", "tienda online", fantasma="TIENDA")

# 31.18–35.86 · Lista con íconos sobre desenfoque
r.checklist(35.86, [(31.30, "la desarrollamos juntas", "personas"),
                    (32.90, "te enseño a subir productos", "celular"),
                    (34.60, "y seguís desde tu casa", "casa")],
            titulo=(31.18, "paso a paso"), etiqueta=(31.18, "[ TIENDA ONLINE ]"))

# 35.9–41.7 · Trabas: etiquetas que se suman + acercamiento en "mala calidad" (efecto)
r.chip(36.16, 41.72, 300, 320, "¿qué contenido?", rot=-3)
r.chip(37.52, 41.72, 780, 320, "mala calidad", rot=3)
r.chip(39.16, 41.72, 300, 435, "sin micrófono", rot=2)
r.chip(40.28, 41.72, 780, 435, "¿qué digo?", rot=-3)
r.ocultar(36.16, 41.72)

# 41.72–44.0 · Título
r.titulo(41.72, 42.78, 44.00, "te ayudo con todas", "mis herramientas", tam_apoyo=80)

# 44.0–46.9 · Interruptores "te grabo / te enseño / guiones" (efecto)
r.ocultar(44.0, 46.88)
for t in (44.3, 45.1, 46.2):
    r.sonido(t, "tecla", 0.8)
# 46.9–49.1 · "MIEDO" tachado (efecto) · 49.1–52.1 · foco "CONTENIDO" (efecto) · 52.1–53.5 · puntos (efecto)
r.sonido(47.82, "pop", 0.9)

# 53.9–56.84 · Título
r.titulo(53.94, 55.22, 56.84, "en marketing digital", "yo puedo ayudarte", tam_apoyo=74, tam_prot=160)

# 56.84–59.5 · Placa color de marca con el servicio
r.placa(56.84, 59.53, color="acento")
r.texto(56.84, 59.53, 540, 720, "Jornada Estratégica 1:1", "sans", 600, 76, "claro", modo="placa")
r.fantasma(57.40, 59.53, 540, 900, "6 horas", tam=330, color="acento_suave", alfa="E6")
r.texto(57.40, 59.53, 540, 890, "6 horas", "acento", 500, 210, "claro", italica=True, modo="placa")
r.texto(58.10, 59.53, 540, 1060, "presenciales, conmigo", "sans", 400, 60, "acento_suave", modo="placa")

# 59.52–fin · CTA
r.titulo(59.52, 60.28, r.fin, "escribime la palabra", "jornada")
r.barra_comentario(59.52, "JORNADA", 61.0)

r.subtitulos(PALABRAS,
             corregir={3: "tenés", 4: "un", 14: "podés", 18: "community", 19: "", 45: "todo", 54: "una", 55: "jornada",
                       57: "Sí,", 97: "necesitás", 117: "sabés", 123: "celular", 131: "sabés", 171: "sea",
                       191: "escribime", 194: "JORNADA"},
             enfasis={"negocio", "conocimiento", "jornada", "presencial", "desarrollar", "aprender", "contenido",
                      "guiones", "miedo", "redes", "marketing"},
             mantener={"JORNADA"})

if "--probar" in sys.argv:
    r.probar([0.5, 6.5, 9.8, 16.9, 19.5, 30.5, 34.9, 40.9, 43.5, 55.8, 58.6, 61.5])
else:
    r.render(SALIDA)
    hoja_de_contacto(SALIDA, [0, 4.4, 6.5, 9.0, 11.8, 14.8, 17.0, 19.6, 22.0, 24.6, 26.8, 30.5, 34.9, 38.0, 40.9,
                              43.0, 45.5, 48.0, 50.5, 53.0, 55.8, 58.6, 61.8], SALIDA + "_revision.jpg")
    portada(SALIDA, SALIDA + "_portada.jpg")
    print("listo:", SALIDA)
