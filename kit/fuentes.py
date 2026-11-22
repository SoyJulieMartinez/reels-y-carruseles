"""Descarga las tipografías de la marca desde Google Fonts (vía GitHub) y crea
instancias estáticas con nombres uniformes, para que libass y Playwright las usen igual.

Cada fuente queda como  ~/.cache/kit-fuentes/rk-<familia>-<peso>[i].ttf
con ese mismo nombre de familia interno (por ejemplo "rk-poppins-600" o "rk-cormorantgaramond-500i").
"""
import json, os, re, sys, urllib.request
from fontTools.ttLib import TTFont

CACHE = os.path.expanduser("~/.cache/kit-fuentes")
PESOS = [300, 400, 500, 600, 700, 800, 900]
RAW = "https://raw.githubusercontent.com/google/fonts/main/ofl/{}/{}"


def _carpeta(familia):
    return re.sub(r"[^a-z0-9]", "", familia.lower())


def _get(url):
    req = urllib.request.Request(url, headers={"User-Agent": "kit-reels"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read()


def _renombrar(font, familia):
    n = font["name"]
    for rec in list(n.names):
        if rec.nameID in (1, 2, 4, 6, 16, 17):
            n.removeNames(nameID=rec.nameID)
    n.setName(familia, 1, 3, 1, 0x409)
    n.setName("Regular", 2, 3, 1, 0x409)
    n.setName(familia, 4, 3, 1, 0x409)
    n.setName(familia.replace(" ", ""), 6, 3, 1, 0x409)
    font["OS/2"].fsSelection = 0x40
    font["head"].macStyle = 0
    return font


def instalar(familia, archivos_locales=None):
    """Deja en CACHE los pesos disponibles de `familia`.
    archivos_locales: lista de .ttf/.otf propios de la marca (si no es de Google Fonts)."""
    os.makedirs(CACHE, exist_ok=True)
    origen = os.path.join(CACHE, "_origen", _carpeta(familia))
    os.makedirs(origen, exist_ok=True)
    if archivos_locales:
        fuentes = list(archivos_locales)
    else:
        meta = _get(RAW.format(_carpeta(familia), "METADATA.pb")).decode("utf-8", "ignore")
        nombres = sorted(set(re.findall(r'filename:\s*"([^"]+)"', meta)))
        fuentes = []
        for nombre in nombres:
            dest = os.path.join(origen, nombre)
            if not os.path.exists(dest):
                open(dest, "wb").write(_get(RAW.format(_carpeta(familia), urllib.request.quote(nombre))))
            fuentes.append(dest)
    hechos = []
    for f in fuentes:
        base = os.path.basename(f)
        italica = "italic" in base.lower()
        tt = TTFont(f)
        if "fvar" in tt:
            from fontTools.varLib.instancer import instantiateVariableFont
            ejes = {a.axisTag: a for a in tt["fvar"].axes}
            w = ejes.get("wght")
            for p in PESOS:
                if w and not (w.minValue <= p <= w.maxValue):
                    continue
                nombre = f"rk-{_carpeta(familia)}-{p}{'i' if italica else ''}"
                dest = os.path.join(CACHE, nombre + ".ttf")
                if not os.path.exists(dest):
                    fija = {"wght": p} if w else {}
                    for tag, ax in ejes.items():
                        if tag != "wght":
                            fija[tag] = ax.defaultValue
                    inst = instantiateVariableFont(TTFont(f), fija, updateFontNames=False)
                    _renombrar(inst, nombre).save(dest)
                hechos.append(nombre)
        else:
            p = tt["OS/2"].usWeightClass
            p = min(PESOS, key=lambda x: abs(x - p))
            nombre = f"rk-{_carpeta(familia)}-{p}{'i' if italica else ''}"
            dest = os.path.join(CACHE, nombre + ".ttf")
            if not os.path.exists(dest):
                _renombrar(tt, nombre).save(dest)
            hechos.append(nombre)
    if not hechos:
        raise RuntimeError(f"No encontré archivos de la fuente {familia!r}")
    return sorted(set(hechos))


def disponibles(familia):
    if not os.path.isdir(CACHE):
        return []
    pre = f"rk-{_carpeta(familia)}-"
    return sorted(f[:-4] for f in os.listdir(CACHE) if f.startswith(pre) and f.endswith(".ttf"))


def elegir(familia, peso, italica=False):
    """Devuelve el nombre de fuente más cercano al peso pedido (con o sin itálica)."""
    ops = disponibles(familia)
    cands = [o for o in ops if o.endswith("i") == italica] or ops
    def peso_de(n):
        return int(re.sub(r"\D", "", n.split("-")[-1]))
    return min(cands, key=lambda n: abs(peso_de(n) - peso))


def ratio(nombre):
    """Cuánto más chico que \\fs se dibuja la letra (altura de línea / em)."""
    t = TTFont(os.path.join(CACHE, nombre + ".ttf"))
    h = t["hhea"]
    return (h.ascent - h.descent) / t["head"].unitsPerEm


if __name__ == "__main__":
    marca = json.load(open(sys.argv[1]))
    for rol in ("sans", "acento"):
        fam = marca["tipografias"][rol]
        print(rol, fam, instalar(fam, marca["tipografias"].get(rol + "_archivos")))
