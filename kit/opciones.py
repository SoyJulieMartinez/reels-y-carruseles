"""Opciones de estilo para elegir cuando la persona no tiene referencias o duda.

Reel: 3 portadas del mismo hook en 3 estilos, sobre el video real (renderiza solo los primeros segundos).
    python3 -m kit.opciones reel crudo.mp4 marca.json "tu presencia digital es" "malísima" salida/

Carrusel: las 2 primeras placas en 3 direcciones de color y composición, SIN cambiar el texto.
    python3 -m kit.opciones carrusel marca.json carrusel.json salida/

Deja opciones.jpg con las variantes rotuladas A, B y C para mostrar y elegir (o mezclar: "A con los colores de C").
"""
import copy, json, os, subprocess, sys
from PIL import Image, ImageDraw, ImageFont

ESTILOS_REEL = {
    "A · Editorial": dict(fantasma=True),
    "B · Impacto": dict(mayus=True),
    "C · Contraste": dict(contraste=True),
}


def _rotular(ims, salida, ancho=360):
    try:
        f = ImageFont.truetype("DejaVuSans-Bold.ttf", 24 if ancho > 320 else 21)
    except OSError:
        f = ImageFont.load_default()
    ims = [(et, im.resize((ancho, int(im.height * ancho / im.width)))) for et, im in ims]
    h = max(im.height for _, im in ims)
    hoja = Image.new("RGB", (len(ims) * (ancho + 20) + 20, h + 70), "white")
    d = ImageDraw.Draw(hoja)
    for i, (et, im) in enumerate(ims):
        x = 20 + i * (ancho + 20)
        d.text((x, 18), et, fill="black", font=f); hoja.paste(im, (x, 60))
    hoja.save(salida, quality=88)
    return salida


def opciones_reel(video, marca, apoyo, protagonista, salida, hasta=3.6):
    from .reel import Reel
    os.makedirs(salida, exist_ok=True)
    ims = []
    for i, (nombre, op) in enumerate(ESTILOS_REEL.items()):
        r = Reel(video, marca, carpeta=os.path.join(salida, f"_{i}"), fin=min(hasta + 0.4, 6))
        kw = {}
        if op.get("fantasma"):
            kw["fantasma"] = protagonista.upper()
        if op.get("mayus"):
            kw.update(mayus=True, protagonista=protagonista.upper())
        if op.get("contraste"):
            r.desenfoque(0, hasta)
            r.sonidos.clear()
            kw.update(modo="sobre_oscuro", color_apoyo="claro", color_prot="acento_suave", y=700)
        prot = kw.pop("protagonista", protagonista)
        r.hook(apoyo, prot, hasta=hasta, **kw)
        out = os.path.join(salida, f"opcion-{'ABC'[i]}.mp4")
        r.render(out)
        png = os.path.join(salida, f"opcion-{'ABC'[i]}.png")
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", out, "-frames:v", "1", png], check=True)
        ims.append((nombre, Image.open(png).convert("RGB")))
    return _rotular(ims, os.path.join(salida, "opciones.jpg"))


def opciones_carrusel(marca, carrusel, salida):
    from .carrusel import render
    carrusel = json.load(open(carrusel)) if isinstance(carrusel, str) else carrusel
    base = copy.deepcopy(carrusel["placas"][:2])
    variantes = {
        "A · Luminosa": ["claro", "blanco"],
        "B · Intensa": ["oscuro", "acento_suave"],
        "C · Color de marca": ["acento", "claro"],
    }
    ims = []
    for i, (nombre, fondos) in enumerate(variantes.items()):
        placas = copy.deepcopy(base)
        for p, f in zip(placas, fondos):
            p["fondo"] = f
        if i == 2 and len(placas) > 1 and placas[1]["tipo"] == "texto" and not placas[1].get("titulo"):
            placas[1]["tipo"] = "respiro"   # misma frase, composición L
        carpeta = os.path.join(salida, f"opcion-{'ABC'[i]}")
        pngs, _ = render(marca, {"placas": placas}, carpeta)
        a = [Image.open(p).convert("RGB") for p in pngs]
        par = Image.new("RGB", (sum(x.width for x in a) + 20 * (len(a) - 1), a[0].height), "white")
        x = 0
        for im in a:
            par.paste(im, (x, 0)); x += im.width + 20
        ims.append((nombre, par))
    return _rotular(ims, os.path.join(salida, "opciones.jpg"), ancho=560)


if __name__ == "__main__":
    if sys.argv[1] == "reel":
        print(opciones_reel(*sys.argv[2:7]))
    else:
        print(opciones_carrusel(*sys.argv[2:5]))
