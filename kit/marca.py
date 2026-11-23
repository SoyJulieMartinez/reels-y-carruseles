"""Armar el marca.json rápido, sin ficha.

    python3 -m kit.marca paleta logo.png [captura2.jpg ...]   # propone 6 colores con su rol
    python3 -m kit.marca crear salida.json "Nombre" "@usuario" "#f4efe9,#ffffff,#ebcdcb,#d6a5a7,#a9666b,#2f2a2b" "Poppins" "Cormorant Garamond"
    python3 -m kit.marca propuestas                            # 3 combinaciones de tipografías para elegir

La paleta sale de las imágenes que pase la persona (logo, brand kit, capturas de su feed).
Las tipografías no se pueden detectar con seguridad desde una imagen: se preguntan o se proponen.
"""
import colorsys, json, sys

PARES = [
    ("Moderna y cálida", "Poppins", "Cormorant Garamond"),
    ("Elegante editorial", "Montserrat", "Playfair Display"),
    ("Cercana y fresca", "DM Sans", "Fraunces"),
    ("Fuerte y directa", "Archivo", "DM Serif Display"),
    ("Suave y femenina", "Nunito Sans", "Libre Baskerville"),
]


def _hex(rgb):
    return "#%02x%02x%02x" % tuple(int(c) for c in rgb)


def _lum(rgb):
    r, g, b = [c / 255 for c in rgb]
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def _sat(rgb):
    return colorsys.rgb_to_hls(*[c / 255 for c in rgb])[2]


def paleta(*imagenes, n=12):
    """Devuelve dict con roles claro, blanco, acento_suave, medio, acento, oscuro."""
    from PIL import Image
    conteo = {}
    for p in imagenes:
        im = Image.open(p).convert("RGB")
        im.thumbnail((600, 600))
        sumas = {}
        for cnt, rgb in im.getcolors(600 * 600):
            k = tuple(v // 24 for v in rgb)  # agrupa tonos casi iguales
            s_ = sumas.setdefault(k, [0, 0, 0, 0])
            s_[0] += cnt; s_[1] += rgb[0] * cnt; s_[2] += rgb[1] * cnt; s_[3] += rgb[2] * cnt
        for cnt, r, g, b in sumas.values():
            if cnt < 0.0002 * im.width * im.height:
                continue  # bordes y antialias
            rgb = (r // cnt, g // cnt, b // cnt)
            conteo[rgb] = conteo.get(rgb, 0) + cnt
    cols = sorted(conteo, key=lambda c: -conteo[c])
    # unir colores muy parecidos
    unicos = []
    for c in cols:
        if all(sum((a - b) ** 2 for a, b in zip(c, u)) > 900 for u in unicos):
            unicos.append(c)
    oscuro = min(unicos, key=_lum)
    claros = [c for c in unicos if _lum(c) > 0.82]
    claro = max(claros, key=lambda c: conteo.get(c, 0)) if claros else (244, 239, 233)
    mezcla = lambda a, b, t: tuple(round(x * (1 - t) + y * t) for x, y in zip(a, b))
    total = max(conteo.values())
    con_color = [c for c in unicos if c not in (oscuro, claro) and _sat(c) > 0.15 and 0.04 < _lum(c) < 0.9]
    con_color.sort(key=lambda c: -(conteo.get(c, 0) / total + _sat(c)))
    acento = next((c for c in con_color if _lum(c) < 0.7), con_color[0] if con_color else None)
    aviso = None
    if acento is None:
        aviso = "No encontré un color de acento claro en las imágenes: preguntale a la persona cuál es su color principal."
        acento = mezcla(oscuro, (255, 255, 255), 0.3)
    otros = [c for c in con_color if c != acento and _lum(c) > _lum(acento)]
    medio = otros[0] if otros else mezcla(acento, (255, 255, 255), 0.4)
    acento_suave = mezcla(acento, (255, 255, 255), 0.65)
    if _lum(oscuro) > 0.3:
        oscuro = mezcla(acento, (0, 0, 0), 0.75)
    return {"claro": _hex(claro), "blanco": "#ffffff", "acento_suave": _hex(acento_suave),
            "medio": _hex(medio), "acento": _hex(acento), "oscuro": _hex(oscuro), **({"_aviso": aviso} if aviso else {})}


def crear(salida, nombre, usuario, colores, sans="Poppins", acento="Cormorant Garamond", subtitulos=None):
    if isinstance(colores, str):
        v = [c.strip() for c in colores.split(",")]
        colores = dict(zip(["claro", "blanco", "acento_suave", "medio", "acento", "oscuro"], v))
    m = {"nombre": nombre, "usuario": usuario, "colores": colores,
         "tipografias": {"sans": sans, "acento": acento},
         "subtitulos": subtitulos or {"palabras": 3, "tamano": 104, "y": 1250, "mayusculas": False, "resaltar_activa": True}}
    json.dump(m, open(salida, "w"), ensure_ascii=False, indent=2)
    return salida


def muestra(marca, salida):
    """Imagen chica con la paleta y las tipografías, para que la persona confirme."""
    from PIL import Image, ImageDraw, ImageFont
    from . import fuentes
    m = json.load(open(marca)) if isinstance(marca, str) else marca
    W, H = 1080, 640
    im = Image.new("RGB", (W, H), m["colores"]["claro"])
    d = ImageDraw.Draw(im)
    roles = ["claro", "blanco", "acento_suave", "medio", "acento", "oscuro"]
    for i, r in enumerate(roles):
        x = 60 + i * 162
        d.rounded_rectangle([x, 380, x + 140, 520], 24, fill=m["colores"][r], outline="#00000022")
        d.text((x + 70, 545), f"{r}\n{m['colores'][r]}", fill=m["colores"]["oscuro"], anchor="ma", align="center")
    fuentes.instalar(m["tipografias"]["sans"]); fuentes.instalar(m["tipografias"]["acento"])
    import os
    f1 = ImageFont.truetype(os.path.join(fuentes.CACHE, fuentes.elegir(m["tipografias"]["sans"], 700) + ".ttf"), 84)
    f2 = ImageFont.truetype(os.path.join(fuentes.CACHE, fuentes.elegir(m["tipografias"]["acento"], 500, True) + ".ttf"), 120)
    d.text((60, 70), "tu presencia digital", font=f1, fill=m["colores"]["oscuro"])
    d.text((60, 170), "con estilo propio", font=f2, fill=m["colores"]["acento"])
    im.save(salida)
    return salida


if __name__ == "__main__":
    cmd = sys.argv[1]
    if cmd == "paleta":
        print(json.dumps(paleta(*sys.argv[2:]), indent=2))
    elif cmd == "crear":
        print(crear(*sys.argv[2:]))
    elif cmd == "muestra":
        print(muestra(sys.argv[2], sys.argv[3]))
    elif cmd == "propuestas":
        for i, (n, a, b) in enumerate(PARES, 1):
            print(f"{i}. {n}: {a} + {b}")
