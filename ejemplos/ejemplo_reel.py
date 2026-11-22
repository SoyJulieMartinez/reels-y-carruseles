"""Ejemplo completo: el reel de la Jornada Estratégica 1:1 de Julie Martínez.
Uso: python3 ejemplos/ejemplo_reel.py crudo.mp4 palabras.json salida.mp4
(palabras.json sale de: python3 -m kit.transcribir crudo.mp4 palabras.json)
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from kit.reel import Reel, hoja_de_contacto, portada

crudo, palabras, salida = sys.argv[1:4]
r = Reel(crudo, os.path.join(os.path.dirname(__file__), "marca-julie.json"))

# Hook = portada (completo desde el cuadro 0)
r.hook("tu presencia digital es", "malísima", fantasma="MALÍSIMA")

# Tarjetas de lo que no se puede pagar (terminan en el corte de cámara de 10.23 s)
r.chip(5.10, 10.23, 540, 320, "community manager", rot=-2)
r.chip(6.00, 10.23, 310, 435, "diseñador web", rot=3, tam=42)
r.chip(9.32, 10.23, 745, 435, "marketing digital", rot=-3, tam=42)

# Título + placa oscura
r.titulo(15.84, 16.92, 17.98, "una jornada 1:1", "presencial")
r.placa(17.98, 20.15)
r.texto(17.98, 20.15, 540, 740, "sí, como escuchaste bien", "sans", 300, 84, "claro", modo="placa")
r.fantasma(18.80, 20.15, 540, 900, "presencial", tam=330, color="acento_suave", alfa="EC")
r.texto(18.80, 20.15, 540, 890, "presencial", "acento", 500, 230, "acento_suave", italica=True, modo="placa")

r.titulo(23.68, 24.38, 25.15, "y lo vas a ver", "conmigo")

# Checklist sobre fondo desenfocado
r.checklist(35.86, [(31.18, "la desarrollamos juntas"), (32.46, "te enseño a subir productos"), (34.42, "y seguís desde tu casa")],
            titulo=(30.28, "tienda online"), etiqueta=(29.02, "[ EJEMPLO ]"))

# Trabas
r.chip(36.16, 41.72, 300, 320, "¿qué contenido?", rot=-3)
r.chip(37.52, 41.72, 780, 320, "mala calidad", rot=3)
r.chip(39.16, 41.72, 300, 435, "sin micrófono", rot=2)
r.chip(40.28, 41.72, 780, 435, "¿qué digo?", rot=-3)

r.titulo(41.72, 42.78, 43.98, "te ayudo con todas", "mis herramientas", tam_apoyo=80)
r.titulo(52.14, 55.22, 56.84, "lo que sea que necesites", "yo puedo ayudarte", tam_apoyo=74, tam_prot=160)

# Cierre
r.titulo(59.52, 60.28, r.fin, "escribime la palabra", "jornada", tam_apoyo=80)
r.barra_comentario(59.52, "JORNADA", 61.0)

r.subtitulos(palabras,
             corregir={3: "tenés", 4: "un", 14: "podés", 18: "community", 19: "", 45: "todo", 57: "Sí,", 97: "necesitás",
                       117: "sabés", 123: "celular", 131: "sabés", 171: "sea", 191: "escribime", 194: "JORNADA"},
             enfasis={"negocio", "conocimiento", "jornada", "presencial", "desarrollar", "aprender", "contenido", "guiones", "miedo", "redes", "marketing"},
             mantener={"JORNADA"})

r.render(salida)
hoja_de_contacto(salida, [0, 9.9, 19.6, 31.5, 35.5, 40.9, 62.8], salida + "_revision.jpg")
portada(salida, salida + "_portada.jpg")
print("listo:", salida)
