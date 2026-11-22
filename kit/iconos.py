"""Íconos dibujados con los colores de la marca (sin descargar nada, sin derechos de terceros).

Todos del mismo estilo: trazo grueso dentro de un círculo de color. Nombres disponibles:
    check, estrella, objetivo, personas, crecimiento, corazon, chat, reloj, casa, idea,
    dinero, camara, calendario, ubicacion, flecha, rayo, celular, regalo

    from kit.iconos import icono
    icono("objetivo", "salida.png", fondo="#ebcdcb", trazo="#a9666b", radio=58)
"""
import math
from PIL import Image, ImageDraw

S = 4  # sobremuestreo para bordes suaves


def _rgb(h, a=255):
    h = h.lstrip("#")
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4)) + (a,)


def _dibujar(d, nombre, c, r, col, w):
    L = lambda pts: d.line(pts, fill=col, width=w, joint="curve")
    E = lambda x0, y0, x1, y1, **k: d.ellipse([x0, y0, x1, y1], **k)
    u = r / 58  # unidad relativa (diseñado para radio 58)
    p = lambda x, y: (c + x * u * S, c + y * u * S)
    if nombre == "check":
        L([p(-26, 2), p(-8, 20), p(28, -20)])
    elif nombre == "estrella":
        pts = [p(30 * math.cos(-math.pi / 2 + k * math.pi / 5) * (1 if k % 2 == 0 else .45),
                 30 * math.sin(-math.pi / 2 + k * math.pi / 5) * (1 if k % 2 == 0 else .45) + 2) for k in range(10)]
        d.polygon(pts, fill=col)
    elif nombre == "objetivo":
        for rr in (30, 18):
            E(*p(-rr, -rr), *p(rr, rr), outline=col, width=w)
        E(*p(-6, -6), *p(6, 6), fill=col)
    elif nombre == "personas":
        E(*p(-26, -24), *p(-8, -6), fill=col); d.pieslice([*p(-34, 0), *p(0, 34)], 180, 360, fill=col)
        E(*p(8, -28), *p(28, -8), fill=col); d.pieslice([*p(0, -4), *p(36, 32)], 180, 360, fill=col)
    elif nombre == "crecimiento":
        L([p(-28, 22), p(-10, 2), p(4, 14), p(28, -16)]); L([p(12, -16), p(28, -16), p(28, 0)])
    elif nombre == "corazon":
        d.polygon([p(0, 26), p(-28, -2), p(-26, -18), p(-14, -26), p(0, -16), p(14, -26), p(26, -18), p(28, -2)], fill=col)
        E(*p(-30, -28), *p(-2, -2), fill=col); E(*p(2, -28), *p(30, -2), fill=col)
    elif nombre == "chat":
        d.rounded_rectangle([*p(-30, -24), *p(30, 14)], radius=12 * u * S, outline=col, width=w)
        L([p(-14, 14), p(-20, 28), p(0, 14)])
    elif nombre == "reloj":
        E(*p(-30, -30), *p(30, 30), outline=col, width=w); L([p(0, -16), p(0, 0), p(14, 8)])
    elif nombre == "casa":
        L([p(-30, 0), p(0, -26), p(30, 0)]); L([p(-20, -8), p(-20, 26), p(20, 26), p(20, -8)])
    elif nombre == "idea":
        d.arc([*p(-20, -28), *p(20, 12)], 135, 405, fill=col, width=w)
        L([p(-10, 8), p(-10, 18), p(10, 18), p(10, 8)]); L([p(-7, 27), p(7, 27)])
    elif nombre == "dinero":
        from PIL import ImageFont
        try:
            fnt = ImageFont.truetype("DejaVuSans-Bold.ttf", int(62 * u * S))
        except OSError:
            fnt = ImageFont.load_default()
        d.text(p(0, 2), "$", fill=col, font=fnt, anchor="mm")
    elif nombre == "camara":
        d.rounded_rectangle([*p(-32, -16), *p(32, 24)], radius=8 * u * S, outline=col, width=w)
        L([p(-12, -16), p(-6, -26), p(6, -26), p(12, -16)]); E(*p(-12, -8), *p(12, 16), outline=col, width=w)
    elif nombre == "calendario":
        d.rounded_rectangle([*p(-28, -22), *p(28, 28)], radius=8 * u * S, outline=col, width=w)
        L([p(-28, -6), p(28, -6)]); L([p(-14, -30), p(-14, -16)]); L([p(14, -30), p(14, -16)])
    elif nombre == "ubicacion":
        d.arc([*p(-20, -32), *p(20, 8)], 140, 400, fill=col, width=w); L([p(-16, 0), p(0, 30), p(16, 0)])
        E(*p(-7, -19), *p(7, -5), fill=col)
    elif nombre == "flecha":
        L([p(-28, 0), p(26, 0)]); L([p(10, -16), p(28, 0), p(10, 16)])
    elif nombre == "rayo":
        d.polygon([p(6, -32), p(-20, 4), p(-2, 4), p(-8, 32), p(20, -6), p(2, -6)], fill=col)
    elif nombre == "celular":
        d.rounded_rectangle([*p(-18, -32), *p(18, 32)], radius=8 * u * S, outline=col, width=w); L([p(-4, 22), p(4, 22)])
    elif nombre == "regalo":
        d.rectangle([*p(-26, -6), *p(26, 28)], outline=col, width=w); d.rectangle([*p(-30, -18), *p(30, -6)], outline=col, width=w)
        L([p(0, -18), p(0, 28)]); d.arc([*p(-18, -32), *p(0, -14)], 180, 360, fill=col, width=w); d.arc([*p(0, -32), *p(18, -14)], 180, 360, fill=col, width=w)
    else:
        raise ValueError(f"Ícono desconocido: {nombre}. Disponibles: {', '.join(NOMBRES)}")


NOMBRES = ["check", "estrella", "objetivo", "personas", "crecimiento", "corazon", "chat", "reloj", "casa", "idea",
           "dinero", "camara", "calendario", "ubicacion", "flecha", "rayo", "celular", "regalo"]


def icono(nombre, salida, fondo="#ebcdcb", trazo="#a9666b", radio=58):
    n = 2 * radio * S
    im = Image.new("RGBA", (n, n), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    d.ellipse([0, 0, n - 1, n - 1], fill=_rgb(fondo, 245))
    capa = Image.new("RGBA", (n, n), (0, 0, 0, 0))
    _dibujar(ImageDraw.Draw(capa), nombre, radio * S, radio, _rgb(trazo), int(9 * S * radio / 58))
    im.alpha_composite(capa)
    im.resize((2 * radio, 2 * radio), Image.LANCZOS).save(salida)
    return salida


def muestrario(salida, fondo="#ebcdcb", trazo="#a9666b"):
    import os, tempfile
    from PIL import ImageFont
    tmp = tempfile.mkdtemp(); cols = 6; cel = 170
    hoja = Image.new("RGB", (cols * cel, ((len(NOMBRES) + cols - 1) // cols) * cel), "white")
    dd = ImageDraw.Draw(hoja)
    try:
        f = ImageFont.truetype("DejaVuSans.ttf", 18)
    except OSError:
        f = ImageFont.load_default()
    for i, n in enumerate(NOMBRES):
        im = Image.open(icono(n, os.path.join(tmp, n + ".png"), fondo, trazo))
        x, y = (i % cols) * cel, (i // cols) * cel
        hoja.paste(im, (x + 27, y + 10), im); dd.text((x + cel // 2, y + 140), n, fill="black", font=f, anchor="mm")
    hoja.save(salida)
    return salida


if __name__ == "__main__":
    import sys
    print(muestrario(sys.argv[1] if len(sys.argv) > 1 else "iconos.png"))
