"""Motor de edición de reels con marca.

Uso típico (lo escribe Claude para cada video):

    from kit.reel import Reel
    r = Reel("crudo.mp4", "marca.json")
    r.hook("tu presencia digital es", "malísima")
    r.titulo(15.8, 16.9, 18.0, "en un consultorio", "presencial")
    r.subtitulos("palabras.json")
    r.render("final.mp4")

Todos los tiempos se dan en segundos del video ORIGINAL (si hay cortes, se convierten solos).
"""
import json, math, os, re, subprocess, wave
import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont
from . import fuentes

W, H = 1080, 1920


def _col(h, a="00"):
    h = h.lstrip("#")
    return f"&H{a}{h[4:6]}{h[2:4]}{h[0:2]}&".upper()


def _ts(x):
    x = max(0, x)
    return f"{int(x // 3600)}:{int(x % 3600 // 60):02d}:{x % 60:05.2f}"


def _rgb(h, a=255):
    h = h.lstrip("#")
    return (int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16), a)


def _rrect(w, h, r):
    k = r * 0.45
    return (f"m {r} 0 l {w-r} 0 b {w-k} 0 {w} {k} {w} {r} l {w} {h-r} b {w} {h-k} {w-k} {h} {w-r} {h} "
            f"l {r} {h} b {k} {h} 0 {h-k} 0 {h-r} l 0 {r} b 0 {k} {k} 0 {r} 0")


def duracion(src):
    return float(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", src]).decode())


def cortes_de_camara(src, umbral=0.25):
    """Tiempos (s) donde cambia la toma. Los efectos tienen que terminar justo ahí."""
    out = subprocess.run(["ffmpeg", "-hide_banner", "-i", src, "-vf", f"select='gt(scene,{umbral})',showinfo", "-f", "null", "-"],
                         capture_output=True, text=True).stderr
    return [float(x) for x in re.findall(r"pts_time:([0-9.]+)", out)]


class Reel:
    def __init__(self, src, marca, carpeta=None, fin=None, cortes=None, sonidos="auto"):
        """sonidos: "auto" (realistas con earshot si está instalado, si no sintetizados) o "sintetizados"."""
        self.src = src
        self.sonidos_modo = sonidos
        self.m = json.load(open(marca)) if isinstance(marca, str) else marca
        self.c = {k: v.lstrip("#") for k, v in self.m["colores"].items()}
        self.dir = carpeta or os.path.splitext(src)[0] + "_kit"
        os.makedirs(self.dir, exist_ok=True)
        self.fin = fin or duracion(src)
        self.cortes = sorted(cortes or [])
        keep, t = [], 0.0
        for a, b in self.cortes:
            keep.append((t, a)); t = b
        keep.append((t, self.fin))
        self.keep = keep
        self.ev, self.ocultos, self.placas, self.desenfoques, self.capas, self.sonidos, self.marcas = [], [], [], [], [], [], []
        t = self.m["tipografias"]
        self.familia = {"sans": t["sans"], "acento": t["acento"]}
        for rol, fam in self.familia.items():
            if not fuentes.disponibles(fam):
                fuentes.instalar(fam, t.get(rol + "_archivos"))
        self._fc, self._ratio = {}, {}

    # ------------------------------------------------------------------ tiempos
    def R(self, x):
        out = 0.0
        for a, b in self.keep:
            if x >= b: out += b - a
            elif x > a: return out + (x - a)
            else: return out
        return out

    @property
    def dur(self):
        return self.R(self.fin)

    # ------------------------------------------------------------------ medidas
    def fuente(self, rol, peso, italica=False):
        return fuentes.elegir(self.familia[rol], peso, italica)

    def ancho(self, texto, fuente, tam, esp=0):
        if fuente not in self._ratio:
            self._ratio[fuente] = fuentes.ratio(fuente)
        em = max(1, int(round(tam / self._ratio[fuente])))
        k = (fuente, em)
        if k not in self._fc:
            self._fc[k] = ImageFont.truetype(os.path.join(fuentes.CACHE, fuente + ".ttf"), em)
        return self._fc[k].getlength(texto) + esp * len(texto)

    def ajustar(self, texto, fuente, tam, esp=0, maximo=960):
        w = self.ancho(texto, fuente, tam, esp)
        return int(tam * min(1, maximo / w)) if w else tam

    # ------------------------------------------------------------------ piezas
    def ocultar(self, t0, t1):
        """Sin subtítulos entre t0 y t1 (se hace solo con títulos, placas y desenfoques)."""
        self.ocultos.append((t0, t1))

    def texto(self, t0, t1, x, y, s, rol="sans", peso=600, tam=60, color="oscuro", italica=False,
              modo="sobre_claro", esp=0, rot=0, an=5, anim=True, capa=30, alfa="00", ajustar=True):
        """modo: sobre_claro (texto oscuro con halo claro), sobre_oscuro (texto claro con halo oscuro), placa (sin halo)."""
        f = self.fuente(rol, peso, italica)
        if ajustar and not rot:
            tam = self.ajustar(s, f, tam, esp, 960 if an == 5 else 1000 - x)
        if modo == "sobre_oscuro":
            fx = r"\bord7\3c&H000000&\3a&H68&\blur10\shad0"
        elif modo == "sobre_claro":
            fx = rf"\bord12\3c{_col(self.c['claro'])}\3a&H08&\blur14\shad0"
        else:
            fx = r"\bord0\shad0"
        a = r"\fad(140,0)\fscx88\fscy88\t(0,200,\fscx100\fscy100)" if anim else ""
        r = rf"\frz{rot}" if rot else ""
        col = self.c.get(color, color)
        self.ev.append(f"Dialogue: {capa},{_ts(self.R(t0))},{_ts(self.R(t1))},T,,0,0,0,,"
                       f"{{\\an{an}\\pos({x},{y})\\fn{f}\\fs{tam}\\fsp{esp}\\c{_col(col)}\\1a&H{alfa}&{r}{fx}{a}}}{s}")
        return tam

    def fantasma(self, t0, t1, x, y, s, tam=300, color="acento", alfa="E2", anim=True):
        self.texto(t0, t1, x, y, s, rol="acento", peso=300, italica=True, tam=tam, color=color, modo="placa",
                   capa=25, alfa=alfa, ajustar=False, anim=anim)

    def titulo(self, t0, t0b, t1, apoyo, protagonista, y=300, modo="sobre_claro", tam_apoyo=84, tam_prot=190,
               color_apoyo="oscuro", color_prot="acento", fantasma=None, mayus=False, anim=True, subir=None, sonido=True):
        """Título de dos líneas pegadas y escalonadas: apoyo (sans) + protagonista (acento).
        t0: aparece el apoyo · t0b: aparece la protagonista · t1: se van los dos."""
        self.ocultar(t0, t1)
        fa = self.fuente("sans", 600)
        fb = self.fuente("acento", 300 if mayus else 500, italica=not mayus)
        esp = 5 if mayus else 0
        ta = self.ajustar(apoyo, fa, tam_apoyo)
        tb = self.ajustar(protagonista, fb, tam_prot, esp)
        wa, wb = self.ancho(apoyo, fa, ta), self.ancho(protagonista, fb, tb, esp)
        ka = max(0, min(150, 540 - 95 - wa / 2))
        kb = max(0, min(150, 985 - 540 - wb / 2))
        yb = int(y + (subir if subir is not None else (0.55 if mayus else 0.36)) * tb)
        if fantasma:
            self.fantasma(t0b, t1, 540, yb + 10, fantasma, tam=int(tb * 1.5), color=color_prot, anim=anim)
        self.texto(t0, t1, int(540 - ka), y, apoyo, "sans", 600, ta, color_apoyo, modo=modo, ajustar=False, anim=anim)
        self.texto(t0b, t1, int(540 + kb), yb, protagonista, "acento", 300 if mayus else 500, tb, color_prot,
                   italica=not mayus, modo=modo, esp=esp, ajustar=False, anim=anim)
        if sonido and anim:
            self.sonido(t0b, "swish", 0.45)

    def hook(self, apoyo, protagonista, hasta=3.6, y=375, **kw):
        """El hook ES la portada: completo y quieto desde el cuadro 0."""
        kw.setdefault("tam_apoyo", 96); kw.setdefault("tam_prot", 250)
        self.titulo(0, 0, hasta, apoyo, protagonista, y=y, anim=False, sonido=False, **kw)

    def placa(self, t0, t1, color="oscuro"):
        """Fondo de color a pantalla completa (después se escriben textos encima con modo='placa')."""
        self.ocultar(t0, t1); self.placas.append((t0, t1, self.c.get(color, color)))
        self.sonido(t0 - 0.08, "swish", 1.0)

    def desenfoque(self, t0, t1):
        """El video sigue corriendo desenfocado y oscurecido, para poner contenido encima."""
        self.ocultar(t0, t1); self.desenfoques.append((t0, t1))
        self.sonido(t0 - 0.08, "swish", 1.0)

    def chip(self, t0, t1, cx, cy, s, rot=0, tam=46):
        """Tarjetita tipo pastilla con texto (entra girando, con pop)."""
        self.marcas.append((t0, t1))
        f = self.fuente("sans", 700)
        wb = int(self.ancho(s, f, int(tam * 1.4)) + 64); hb = int(tam * 2.1); r = hb // 2
        a = rf"\org({cx},{cy})\frz{rot+10}\fscx50\fscy50\t(0,220,\frz{rot}\fscx100\fscy100)"
        T0, T1 = _ts(self.R(t0)), _ts(self.R(t1))
        self.ev.append(f"Dialogue: 10,{T0},{T1},T,,0,0,0,,{{\\an5\\pos({cx},{cy+8}){a}\\c{_col(self.c['acento'])}\\1a&H80&\\bord0\\shad0\\blur14\\p1}}{_rrect(wb,hb,r)}{{\\p0}}")
        self.ev.append(f"Dialogue: 11,{T0},{T1},T,,0,0,0,,{{\\an5\\pos({cx},{cy}){a}\\c{_col(self.c['claro'])}\\bord0\\shad0\\p1}}{_rrect(wb,hb,r)}{{\\p0}}")
        self.ev.append(f"Dialogue: 12,{T0},{T1},T,,0,0,0,,{{\\an5\\pos({cx},{cy}){a}\\fn{f}\\fs{int(tam*1.4)}\\c{_col(self.c['oscuro'])}\\bord0\\shad0}}{s}")
        self.sonido(t0, "pop", 1.0)

    def tarjeta(self, imagen, t0, t1, cx, cy, ancho=640, rot=-3, recorte=None, borde="claro", radio=28):
        """Imagen (captura, flyer, foto) como tarjeta flotante con borde de marca y sombra."""
        im = Image.open(imagen).convert("RGB")
        if recorte: im = im.crop(recorte)
        im = im.resize((ancho, int(im.height * ancho / im.width)), Image.LANCZOS)
        m = Image.new("L", im.size, 0); ImageDraw.Draw(m).rounded_rectangle([0, 0, im.width - 1, im.height - 1], radius=radio, fill=255)
        pad = 50; Wc, Hc = im.width + 2 * pad, im.height + 2 * pad
        c = Image.new("RGBA", (Wc, Hc), (0, 0, 0, 0))
        sh = Image.new("RGBA", (Wc, Hc), (0, 0, 0, 0))
        ImageDraw.Draw(sh).rounded_rectangle([pad, pad + 14, pad + im.width, pad + im.height + 14], radius=radio, fill=(20, 10, 12, 150))
        c = Image.alpha_composite(c, sh.filter(ImageFilter.GaussianBlur(16)))
        b = Image.new("RGBA", (Wc, Hc), (0, 0, 0, 0))
        ImageDraw.Draw(b).rounded_rectangle([pad - 8, pad - 8, pad + im.width + 8, pad + im.height + 8], radius=radio + 8, fill=_rgb(self.c.get(borde, borde)))
        c = Image.alpha_composite(c, b)
        l = Image.new("RGBA", (Wc, Hc), (0, 0, 0, 0)); l.paste(im.convert("RGBA"), (pad, pad), m)
        c = Image.alpha_composite(c, l).rotate(rot, resample=Image.BICUBIC, expand=True)
        out = os.path.join(self.dir, f"tarjeta_{len(self.capas):02d}.png"); c.save(out)
        self.capas.append((out, t0, t1, cx, cy))
        self.sonido(t0, "pop", 1.0)

    def _icono(self, nombre="check", radio=58):
        from .iconos import icono
        p = os.path.join(self.dir, f"icono_{nombre}_{radio}.png")
        if not os.path.exists(p):
            icono(nombre, p, fondo=self.c["acento_suave"], trazo=self.c["acento"], radio=radio)
        return p

    def icono(self, nombre, t0, t1, cx, cy, radio=58, sonido=True):
        """Ícono suelto con los colores de la marca (ver kit/iconos.py para la lista de nombres)."""
        self.marcas.append((t0, t1))
        self.capas.append((self._icono(nombre, radio), t0, t1, cx, cy))
        if sonido:
            self.sonido(t0, "pop", 0.8)

    def checklist(self, t1, items, titulo=None, etiqueta=None, y0=760, paso=180, x_icono=170, x_texto=250, tam=82):
        """Lista sobre fondo desenfocado. items = [(tiempo, texto), ...] con tilde,
        o [(tiempo, texto, "nombre_de_icono"), ...] para una lista con íconos (formato 11)."""
        t0 = items[0][0] if not titulo else titulo[0]
        self.desenfoque(min(t0, etiqueta[0] if etiqueta else t0), t1)
        if etiqueta:
            self.texto(etiqueta[0], t1, 540, 380, etiqueta[1], "sans", 600, 54, "acento_suave", modo="sobre_oscuro", esp=12)
        if titulo:
            self.texto(titulo[0], t1, 540, 500, titulo[1], "acento", 500, 170, "blanco", italica=True, modo="sobre_oscuro")
        for i, it in enumerate(items):
            t, s = it[0], it[1]
            ic = self._icono(it[2] if len(it) > 2 else "check")
            y = y0 + i * paso
            self.capas.append((ic, t, t1, x_icono, y))
            self.texto(t, t1, x_texto, y, s, "sans", 600, tam, "blanco", modo="sobre_oscuro", an=4)
            self.sonido(t, "ding", 0.9)

    def barra_comentario(self, t0, palabra, t_escribe, t1=None, y=1330, usuario=True):
        """Cierre: barra de comentario de Instagram donde la palabra se escribe sola."""
        t1 = t1 or self.fin
        self.ocultar(t0, t1)
        BX, BW, BH = 110, 860, 120
        f = self.fuente("sans", 800); fp = self.fuente("sans", 500)
        T0, T1 = _ts(self.R(t0 + 0.4)), _ts(self.R(t1))
        self.ev.append(f"Dialogue: 13,{T0},{T1},T,,0,0,0,,{{\\an7\\pos({BX},{y+10})\\c&H000000&\\1a&HA0&\\bord0\\shad0\\blur16\\p1}}{_rrect(BW,BH,60)}{{\\p0}}")
        self.ev.append(f"Dialogue: 14,{T0},{T1},T,,0,0,0,,{{\\an7\\pos({BX},{y})\\fad(150,0)\\c&HFFFFFF&\\bord0\\shad0\\p1}}{_rrect(BW,BH,60)}{{\\p0}}")
        self.ev.append(f"Dialogue: 15,{T0},{T1},T,,0,0,0,,{{\\an7\\pos({BX+24},{y+24})\\fad(150,0)\\c{_col(self.c['acento_suave'])}\\bord0\\shad0\\p1}}{_rrect(72,72,36)}{{\\p0}}")
        self.ev.append(f"Dialogue: 15,{T0},{T1},T,,0,0,0,,{{\\an5\\pos({BX+BW-70},{y+60})\\fad(150,0)\\c{_col(self.c['acento'])}\\bord0\\shad0\\p1}}m 0 0 l 44 22 l 0 44 l 10 22{{\\p0}}")
        self.ev.append(f"Dialogue: 16,{T0},{_ts(self.R(t_escribe))},T,,0,0,0,,{{\\an4\\pos({BX+120},{y+60})\\fn{fp}\\fs44\\c&H999999&\\bord0\\shad0}}Agregá un comentario…")
        for i in range(1, len(palabra) + 1):
            a = t_escribe + 0.07 * (i - 1); b = t_escribe + 0.07 * i if i < len(palabra) else t1
            self.ev.append(f"Dialogue: 16,{_ts(self.R(a))},{_ts(self.R(b))},T,,0,0,0,,{{\\an4\\pos({BX+120},{y+60})\\fn{f}\\fs70\\c{_col(self.c['oscuro'])}\\bord0\\shad0}}{palabra[:i]}{{\\c{_col(self.c['acento'])}}}|")
            self.sonido(a, "tecla", 0.7)
        self.sonido(t0 + 0.4, "pop", 0.8)
        self.sonido(t_escribe + 0.07 * len(palabra) + 0.3, "enviar", 0.8)
        if usuario and self.m.get("usuario"):
            self.texto(t_escribe + 0.9, t1, 540, y + 160, self.m["usuario"], "sans", 500, 50, "oscuro", esp=2)

    # ------------------------------------------------------------------ subtítulos
    def subtitulos(self, palabras_json, corregir=None, enfasis=(), mantener=(), y=None, tam=None):
        """Subtítulos de 1 a 3 palabras, grandes, con la palabra activa resaltada.
        corregir = {índice: "texto"} ("" borra la palabra) · enfasis = palabras en tipografía de acento."""
        cfg = self.m.get("subtitulos", {})
        y = y or cfg.get("y", 1250); tam = tam or cfg.get("tamano", 110)
        maxp = cfg.get("palabras", 3); mayus = cfg.get("mayusculas", False); activa = cfg.get("resaltar_activa", True)
        words = json.load(open(palabras_json))
        for i, v in (corregir or {}).items():
            words[int(i)]["text"] = v
        mantener = set(mantener)
        for w in words:
            raw = w["text"]; w["p"] = bool(re.search(r"[.,?!]$", raw))
            s = re.sub(r"[¿?¡!.,]", "", raw)
            w["t"] = s if s in mantener else (s.upper() if mayus else s.lower())
        words = [w for w in words if w["t"]]
        enf = {e.lower() for e in enfasis}
        fs, fe = self.fuente("sans", 800), self.fuente("acento", 500, True)
        te = int(tam * 1.33)
        ancho_g = lambda g: sum(self.ancho(w["t"], fe if w["t"].lower() in enf else fs, te if w["t"].lower() in enf else tam) for w in g) + 28 * (len(g) - 1)
        oculto = lambda x: any(a - 1e-6 <= x < b for a, b in self.ocultos)
        grupos, cur = [], []
        for w in words:
            if cur and (len(cur) >= maxp or w["start"] - cur[-1]["end"] > 0.35 or cur[-1]["p"] or ancho_g(cur + [w]) > 940):
                grupos.append(cur); cur = []
            cur.append(w)
        if cur: grupos.append(cur)
        for gi, g in enumerate(grupos):
            nxt = grupos[gi + 1][0]["start"] if gi + 1 < len(grupos) else self.fin
            fin_g = min(nxt, g[-1]["end"] + 0.4)
            for k, w in enumerate(g):
                st = g[0]["start"] if k == 0 else w["start"]
                en = g[k + 1]["start"] if k + 1 < len(g) else fin_g
                if oculto(st): continue
                for a, b in self.ocultos:
                    if st < a < en: en = a
                if en - st < 0.02: continue
                partes = []
                for j, x in enumerate(g):
                    if x["t"].lower() in enf:
                        partes.append(rf"{{\fn{fe}\fs{te}\c{_col(self.c['acento_suave'])}}}{x['t']}")
                    else:
                        c = _col(self.c["acento_suave"]) if (activa and j == k) else "&HFFFFFF&"
                        partes.append(rf"{{\fn{fs}\fs{tam}\c{c}}}{x['t']}")
                pop = r"\fscx86\fscy86\t(0,110,\fscx100\fscy100)" if k == 0 else ""
                self.ev.append(f"Dialogue: 3,{_ts(self.R(st))},{_ts(self.R(en))},Cap,,0,0,0,,{{\\blur12\\an5\\pos({W//2},{y}){pop}}}" + " ".join(partes))

    # ------------------------------------------------------------------ sonidos
    def sonido(self, t, tipo, volumen=1.0):
        """tipo: pop · swish · ding · tecla · enviar, o (con earshot instalado) una descripción en inglés,
        por ejemplo "a camera shutter click" o "a soft whoosh"."""
        self.sonidos.append((t, tipo, volumen))

    EARSHOT = {"pop": "a soft pop for a card appearing", "swish": "a soft whoosh transition",
               "ding": "a soft success chime", "tecla": "a single keyboard key press",
               "enviar": "a message sent swoosh"}

    def _earshot(self, tipo, SR):
        """Sonido realista con earshot (setup.sh --todo). Devuelve None si no está instalado o falla."""
        import shutil, hashlib
        exe = shutil.which("earshot") or os.path.expanduser("~/kit-rc-extras/earshot-venv/bin/earshot")
        if not os.path.exists(exe) and not shutil.which("earshot"):
            return None
        desc = self.EARSHOT.get(tipo, tipo)
        base = os.path.join(self.dir, "sfx_" + hashlib.md5(desc.encode()).hexdigest()[:8])
        try:
            if not os.path.exists(base + ".wav"):
                subprocess.run([exe, "make", desc, "-o", base + "_raw.wav"], check=True, capture_output=True, timeout=180)
                subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", base + "_raw.wav", "-ac", "1", "-ar", str(SR),
                                "-sample_fmt", "s16", base + ".wav"], check=True)
            w = wave.open(base + ".wav")
            x = np.frombuffer(w.readframes(w.getnframes()), np.int16).astype(np.float32) / 32768
            return 0.6 * x / max(1e-6, np.abs(x).max())
        except Exception:
            return None

    def _sintetizar(self):
        SR = 48000; rng = np.random.default_rng(3)
        t = lambda d: np.arange(int(SR * d)) / SR
        def bp(x, lo, hi):
            X = np.fft.rfft(x); fr = np.fft.rfftfreq(len(x), 1 / SR); X[(fr < lo) | (fr > hi)] = 0; return np.fft.irfft(X, len(x))
        S = {}
        tt = t(0.12); f = 320 + 600 * np.exp(-tt / 0.02)
        x = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-tt / 0.035) + 0.15 * rng.standard_normal(len(tt)) * np.exp(-tt / 0.004)
        x[:144] *= np.linspace(0, 1, 144); S["pop"] = 0.6 * x / np.abs(x).max()
        tt = t(0.45); x = (np.sin(2 * np.pi * 1318 * tt) + 0.6 * np.sin(2 * np.pi * 1975 * tt) + 0.2 * np.sin(2 * np.pi * 2637 * tt)) * np.exp(-tt / 0.12)
        x[:96] *= np.linspace(0, 1, 96); S["ding"] = 0.45 * x / np.abs(x).max()
        tt = t(0.40); n = rng.standard_normal(len(tt)); env = np.sin(np.pi * np.clip(tt / 0.40, 0, 1)) ** 2
        x = np.concatenate([bp(n[:len(n) // 2], 600, 2500), bp(n[len(n) // 2:], 1500, 5000)]) * env; S["swish"] = 0.5 * x / np.abs(x).max()
        tt = t(0.035); x = bp(rng.standard_normal(len(tt)) * np.exp(-tt / 0.006) + 0.5 * np.sin(2 * np.pi * 2400 * tt) * np.exp(-tt / 0.004), 800, 8000)
        S["tecla"] = 0.5 * x / np.abs(x).max()
        tt = t(0.18); f = 700 + 900 * (tt / 0.18); x = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-tt / 0.06); x[:96] *= np.linspace(0, 1, 96)
        S["enviar"] = 0.45 * x / np.abs(x).max()
        if self.sonidos_modo != "sintetizados":
            for tipo in {x[1] for x in self.sonidos}:
                real = self._earshot(tipo, SR)
                if real is not None:
                    S[tipo] = real
        pista = np.zeros(int(SR * self.dur) + SR)
        for t0, tipo, g in self.sonidos:
            if tipo not in S:
                continue  # descripción libre sin earshot instalado: se omite
            i = int(max(0, self.R(t0)) * SR); s = S[tipo] * g; pista[i:i + len(s)] += s[:max(0, len(pista) - i)]
        pista = np.clip(pista[:int(SR * self.dur)] * 0.3, -1, 1)
        out = os.path.join(self.dir, "sonidos.wav")
        w = wave.open(out, "w"); w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR); w.writeframes((pista * 32767).astype(np.int16).tobytes()); w.close()
        return out

    # ------------------------------------------------------------------ salida
    def _ass(self):
        cfg = self.m.get("subtitulos", {})
        fs = self.fuente("sans", 800); tam = cfg.get("tamano", 110)
        head = f"""[Script Info]
ScriptType: v4.00+
PlayResX: {W}
PlayResY: {H}
WrapStyle: 2
ScaledBorderAndShadow: yes

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Cap,{fs},{tam},&H00FFFFFF,&H00FFFFFF,&H50000000,&H80000000,0,0,0,0,100,100,-2,0,1,10,0,5,0,0,0,1
Style: T,{fs},60,&H00FFFFFF,&H00FFFFFF,&H00000000,&H80000000,0,0,0,0,100,100,0,0,1,0,0,5,0,0,0,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""
        p = os.path.join(self.dir, "textos.ass")
        open(p, "w").write(head + "\n".join(self.ev) + "\n")
        return p

    def _base(self):
        # La caché depende del video de origen, su fecha y los tramos: si cambia algo, se rehace.
        import hashlib
        st = os.stat(self.src)
        firma = hashlib.md5(f"{os.path.abspath(self.src)}|{st.st_size}|{st.st_mtime}|{self.keep}".encode()).hexdigest()[:10]
        out = os.path.join(self.dir, f"base_{firma}.mov")
        if os.path.exists(out):
            return out
        info = subprocess.check_output(["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries", "stream=color_transfer", "-of", "csv=p=0", self.src]).decode()
        hdr = any(k in info for k in ("arib-std-b67", "smpte2084"))
        tone = "zscale=t=linear:npl=100,format=gbrpf32le,zscale=p=bt709,tonemap=hable:desat=0,zscale=t=bt709:m=bt709:r=tv," if hdr else ""
        partes = []
        for i, (a, b) in enumerate(self.keep):
            seg = os.path.join(self.dir, f"tramo_{firma}_{i:02d}.mov"); partes.append(f"file '{os.path.abspath(seg)}'")
            d = b - a
            subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", f"{a:.3f}", "-i", self.src, "-t", f"{d:.3f}",
                            "-vf", f"{tone}scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},setsar=1,fps=30,format=yuv420p",
                            "-af", f"afade=t=in:d=0.012,afade=t=out:st={max(0, d-0.012):.3f}:d=0.012,aresample=48000",
                            "-c:v", "libx264", "-preset", "veryfast", "-crf", "12", "-c:a", "pcm_s16le", seg], check=True)
        lista = os.path.join(self.dir, f"tramos_{firma}.txt"); open(lista, "w").write("\n".join(partes) + "\n")
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", lista, "-c", "copy", out], check=True)
        return out

    def probar(self, tiempos, salida=None):
        """Hoja de contacto rápida con los textos en esos tiempos (sin el render completo)."""
        base, ass = self._base(), self._ass(); ims = []
        for t in tiempos:
            tr = self.R(t); p = os.path.join(self.dir, "_p.png")
            subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", str(tr), "-i", base, "-frames:v", "1", "-vf",
                            f"setpts=PTS+{tr}/TB,ass={ass}:fontsdir={fuentes.CACHE},scale=360:-1", p], check=True)
            ims.append(Image.open(p).convert("RGB"))
        return _hoja(ims, salida or os.path.join(self.dir, "prueba.jpg"))

    def render(self, salida):
        base, ass = self._base(), self._ass()
        dur = self.dur
        voz = "highpass=f=80,acompressor=threshold=-20dB:ratio=3:attack=5:release=120"
        ins = ["-i", base]
        if self.sonidos:
            ins += ["-i", self._sintetizar()]
        grade = "eq=contrast=1.05:saturation=1.04,colorbalance=rs=0.03:bs=-0.02:rm=0.02"
        fc = [f"[0:v]{grade},split=2[s0][bl]", f"[bl]boxblur=28:2,eq=brightness=-0.16:saturation=0.8,split={max(1, len(self.desenfoques))}" + "".join(f"[b{i}]" for i in range(max(1, len(self.desenfoques))))]
        last = "s0"
        if not self.desenfoques: fc.append("[b0]nullsink")
        for i, (a, b) in enumerate(self.desenfoques):
            fc.append(f"[{last}][b{i}]overlay=0:0:enable='between(t,{self.R(a):.3f},{self.R(b):.3f})'[d{i}]"); last = f"d{i}"
        for i, (a, b, col) in enumerate(self.placas):
            fc.append(f"color=0x{col}:s={W}x{H}:r=30:d={dur:.3f}[pc{i}]")
            fc.append(f"[{last}][pc{i}]overlay=0:0:shortest=1:enable='between(t,{self.R(a):.3f},{self.R(b):.3f})'[p{i}]"); last = f"p{i}"
        for i, (png, a, b, cx, cy) in enumerate(self.capas):
            w_, h_ = Image.open(png).size; idx = ins.count("-i")
            ins += ["-loop", "1", "-framerate", "30", "-t", f"{dur:.3f}", "-i", png]
            ta = self.R(a)
            fc.append(f"[{idx}:v]format=rgba,fade=t=in:st={ta:.3f}:d=0.18:alpha=1[k{i}]")
            fc.append(f"[{last}][k{i}]overlay=x={cx - w_//2}:y='{cy - h_//2}+70*max(0\\,1-(t-{ta:.3f})/0.22)':enable='between(t,{ta:.3f},{self.R(b):.3f})'[o{i}]"); last = f"o{i}"
        fc.append(f"[{last}]ass={ass}:fontsdir={fuentes.CACHE},format=yuv420p[vo]")
        if self.sonidos:
            fc.append(f"[0:a]{voz}[v];[1:a]volume=1[s];[v][s]amix=inputs=2:normalize=0:duration=first,loudnorm=I=-14:TP=-1.5:LRA=9,aresample=48000[ao]")
        else:
            fc.append(f"[0:a]{voz},loudnorm=I=-14:TP=-1.5:LRA=9,aresample=48000[ao]")
        subprocess.run(["ffmpeg", "-v", "error", "-y", *ins, "-filter_complex", ";".join(fc), "-map", "[vo]", "-map", "[ao]",
                        "-t", f"{dur:.3f}", "-c:v", "libx264", "-preset", "veryfast", "-crf", "19", "-c:a", "aac", "-b:a", "192k",
                        "-movflags", "+faststart", salida], check=True)
        json.dump(self.puntos_de_revision(), open(salida + ".puntos.json", "w"))
        return salida

    def puntos_de_revision(self):
        """Todos los momentos donde algo entra o sale (en tiempo del video final), para kit.revisar."""
        ts = set()
        for a, b in self.ocultos + self.marcas + [(a, b) for a, b, _ in self.placas] + self.desenfoques + [(a, b) for _, a, b, _, _ in self.capas]:
            ts.update((self.R(a), self.R(b)))
        ts.update(self.R(b) for a, b in self.cortes)
        return sorted(round(t, 3) for t in ts if 0 < t < self.dur)


def _hoja(ims, salida, n=6):
    w, h = ims[0].size
    S = Image.new("RGB", (w * min(n, len(ims)), h * ((len(ims) + n - 1) // n)), "white")
    for i, im in enumerate(ims):
        S.paste(im, ((i % n) * w, (i // n) * h))
    S.save(salida); return salida


def hoja_de_contacto(video, tiempos, salida, ancho=300):
    """Fotogramas del video final para revisar antes de entregar."""
    ims = []
    for t in tiempos:
        p = salida + "_tmp.png"
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", str(t), "-i", video, "-frames:v", "1", "-vf", f"scale={ancho}:-1", p], check=True)
        ims.append(Image.open(p).convert("RGB"))
    os.remove(p)
    return _hoja(ims, salida)


def portada(video, salida):
    """Cuadro 0 recortado a 4:5, como se ve en el feed."""
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", "0", "-i", video, "-frames:v", "1", "-vf", "crop=1080:1350:0:285,scale=432:-1", salida], check=True)
    return salida
