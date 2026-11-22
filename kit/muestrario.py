"""Muestrario de recursos de edición sobre el video de la persona, con su marca.

    python3 -m kit.muestrario crudo.mp4 marca.json salida/ ["palabra clave del CTA"]

Renderiza unos segundos del crudo aplicando un recurso distinto en cada tramo y arma
muestrario.jpg: una imagen por recurso, con el número del catálogo (docs/reels.md).
Sirve para que la persona elija con qué recursos quiere su edición ("quiero el 3, el 5 y el 29").
Los textos de muestra son genéricos: en la edición real se usan sus palabras.
"""
import os, subprocess, sys
from PIL import Image
from .opciones import _rotular

RECURSOS = [
    "1 · Hook portada",
    "2 · Título escalonado",
    "3 · Etiquetas",
    "4 · Placa",
    "5 · Lista con íconos",
    "6 · Palabra gigante",
    "7 · Comentario CTA",
    "8 · Hook mayúsculas",
]
TRAMO = 2.0


def muestrario(video, marca, salida, palabra="QUIERO"):
    from .reel import Reel, duracion
    os.makedirs(salida, exist_ok=True)
    total = TRAMO * len(RECURSOS)
    d = duracion(video)
    if d < total:
        raise SystemExit(f"El video tiene que durar al menos {total:.0f} s para el muestrario (dura {d:.1f} s).")
    r = Reel(video, marca, carpeta=os.path.join(salida, "_trabajo"), fin=total)
    t = lambda i: i * TRAMO
    fin = lambda i: (i + 1) * TRAMO - 0.05
    r.hook("esta frase es", "tu gancho", hasta=fin(0), fantasma="GANCHO")
    r.titulo(t(1), t(1) + 0.3, fin(1), "una frase de apoyo", "protagonista")
    r.chip(t(2), fin(2), 330, 330, "primera idea", rot=-3)
    r.chip(t(2) + 0.2, fin(2), 760, 330, "segunda idea", rot=3)
    r.chip(t(2) + 0.4, fin(2), 540, 450, "tercera idea", rot=-2)
    r.placa(t(3), fin(3))
    r.texto(t(3), fin(3), 540, 820, "una frase fuerte", "sans", 300, 84, "claro", modo="placa")
    r.texto(t(3), fin(3), 540, 980, "en grande", "acento", 500, 220, "acento_suave", italica=True, modo="placa")
    r.checklist(fin(4), [(t(4) + 0.1, "tu objetivo", "objetivo"), (t(4) + 0.3, "tu comunidad", "personas"), (t(4) + 0.5, "tu crecimiento", "crecimiento")],
                titulo=(t(4), "tu lista"), etiqueta=(t(4), "[ EJEMPLO ]"))
    r.fantasma(t(5), fin(5), 540, 400, "GRANDE", tam=330)
    r.texto(t(5), fin(5), 540, 400, "palabra", "acento", 500, 200, "acento", italica=True)
    r.titulo(t(6), t(6), fin(6), "escribime la palabra", palabra.lower(), anim=False, sonido=False)
    r.barra_comentario(t(6), palabra.upper(), t(6) + 0.2, fin(6))
    r.titulo(t(7), t(7), fin(7), "esta frase es", "TU GANCHO", mayus=True, anim=False, sonido=False)
    out = os.path.join(salida, "muestrario.mp4")
    r.render(out)
    ims = []
    for i, nombre in enumerate(RECURSOS):
        png = os.path.join(salida, f"_{i}.png")
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", f"{t(i) + TRAMO * 0.8:.2f}", "-i", out, "-frames:v", "1", png], check=True)
        ims.append((nombre, Image.open(png).convert("RGB")))
    filas = [ims[:4], ims[4:]]
    hojas = [_rotular(f, os.path.join(salida, f"_fila{k}.jpg"), ancho=300) for k, f in enumerate(filas)]
    a, b = Image.open(hojas[0]), Image.open(hojas[1])
    final = Image.new("RGB", (max(a.width, b.width), a.height + b.height), "white")
    final.paste(a, (0, 0)); final.paste(b, (0, a.height))
    dest = os.path.join(salida, "muestrario.jpg")
    final.save(dest, quality=88)
    return dest


if __name__ == "__main__":
    print(muestrario(sys.argv[1], sys.argv[2], sys.argv[3], *sys.argv[4:5]))
