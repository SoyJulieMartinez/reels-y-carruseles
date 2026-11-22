"""Motor de carruseles: placas 1080x1350 en HTML -> PNG + PDF + hoja de revisión.

    python3 -m kit.carrusel marca.json carrusel.json carpeta_salida

carrusel.json = {"placas": [ {...}, {...} ]}. Cada placa tiene "tipo" y sus textos.
El texto NO se reescribe: solo se marcan énfasis.
  *palabra*   -> tipografía de acento en cursiva, color de acento
  ==frase==   -> franja de color detrás (composición J)
  **palabra** -> negrita

Tipos (letra del catálogo entre paréntesis):
  portada  {titulo, apoyo?, foto?}                         la única con letra 90–110 px
  texto    {titulo?, texto?}                               (A) texto grande con aire
  foto     {titulo?, texto?, foto, lado: izq|der}          (B) foto fundida con el fondo
  cita     {texto, autor?}                                 (C)
  lista    {titulo?, items: [...], tildes: bool, iconos?: [nombres de kit/iconos.py]}  (D / O)
  comparacion {izq: {titulo, items}, der: {titulo, items}} (E)
  dato     {numero, texto}                                 (F)
  chat     {titulo?, mensajes: [{de: ella|yo, texto}]}     (H)
  pasos    {titulo?, items: [...]}                         (K)
  respiro  {texto}                                         (L)
  pregunta {texto}                                         (M)
  fondo_foto {foto, titulo?, texto?}                       (N) foto desenfocada detrás
  cierre   {texto?, accion}                                una sola acción escrita
Cualquier placa acepta "fondo": claro|blanco|acento_suave|medio|acento|oscuro.
Si no se indica, el motor alterna fondos sin repetir y deja el más oscuro para el cierre.
"""
import base64, html, json, os, re, sys
from . import fuentes

W, H, M = 1080, 1350, 90
CLAROS = {"claro", "blanco", "acento_suave"}
ROTACION = ["claro", "blanco", "acento_suave", "claro", "medio", "blanco"]


def _marca(m):
    return json.load(open(m)) if isinstance(m, str) else m


def _hex(c):
    return "#" + c.lstrip("#")


def _fmt(s):
    s = html.escape(s)
    s = re.sub(r"==(.+?)==", r'<span class="band">\1</span>', s)
    s = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", s)
    s = re.sub(r"\*(.+?)\*", r'<em class="ac">\1</em>', s)
    return s.replace("\n", "<br>")


def _img64(p, maximo=1600):
    import io
    from PIL import Image, ImageOps
    im = ImageOps.exif_transpose(Image.open(p)).convert("RGB")
    im.thumbnail((maximo, maximo))
    b = io.BytesIO(); im.save(b, "JPEG", quality=90)
    return "data:image/jpeg;base64," + base64.b64encode(b.getvalue()).decode()


def _icono64(nombre, ctx):
    import tempfile
    from .iconos import icono
    p = os.path.join(tempfile.gettempdir(), f"kit_ico_{nombre}_{ctx['trazo'].strip('#')}.png")
    icono(nombre, p, fondo=ctx["fondo"], trazo=ctx["trazo"], radio=40)
    return "data:image/png;base64," + base64.b64encode(open(p, "rb").read()).decode()


def _fontface(rol, familia):
    fuentes.instalar(familia)
    css = []
    for n in fuentes.disponibles(familia):
        peso = int(re.sub(r"\D", "", n.split("-")[-1]))
        it = n.endswith("i")
        data = base64.b64encode(open(os.path.join(fuentes.CACHE, n + ".ttf"), "rb").read()).decode()
        css.append(f"@font-face{{font-family:'{rol}';src:url(data:font/ttf;base64,{data});font-weight:{peso};font-style:{'italic' if it else 'normal'}}}")
    return "\n".join(css)


def _fondos(placas):
    out, prev, k = [], None, 0
    for i, p in enumerate(placas):
        f = p.get("fondo")
        if not f:
            if p["tipo"] == "cierre":
                f = "oscuro"
            elif p["tipo"] == "portada":
                f = "claro"
            else:
                f = ROTACION[k % len(ROTACION)]; k += 1
                while f == prev or (i + 1 < len(placas) and placas[i + 1]["tipo"] == "cierre" and f == "oscuro"):
                    f = ROTACION[k % len(ROTACION)]; k += 1
        out.append(f); prev = f
    return out


def _cuerpo(p, ctx):
    t = p["tipo"]; g = lambda k, d="": p.get(k, d)
    h2 = lambda s, cls="t": f'<h2 class="{cls}">{_fmt(s)}</h2>' if s else ""
    pp = lambda s: f'<p class="x">{_fmt(s)}</p>' if s else ""
    if t == "portada":
        foto = f'<div class="ph ph-bottom" style="background-image:url({_img64(g("foto"))})"></div>' if g("foto") and os.path.exists(g("foto")) else ""
        return foto + f'<div class="box {"top" if foto else ""}">{h2(g("titulo"), "t portada")}{pp(g("apoyo"))}</div>'
    if t == "texto":
        return f'<div class="box">{h2(g("titulo"))}{pp(g("texto"))}</div>'
    if t == "foto":
        lado = g("lado", "der")
        return (f'<div class="ph ph-{lado}" style="background-image:url({_img64(g("foto"))})"></div>'
                f'<div class="box half-{"izq" if lado == "der" else "der"}">{h2(g("titulo"))}{pp(g("texto"))}</div>')
    if t == "fondo_foto":
        return (f'<div class="ph ph-full" style="background-image:url({_img64(g("foto"))})"></div><div class="velo"></div>'
                f'<div class="box sobre">{h2(g("titulo"))}{pp(g("texto"))}</div>')
    if t == "cita":
        a = f'<p class="autor">{_fmt(g("autor"))}</p>' if g("autor") else ""
        return f'<div class="box"><div class="comillas">“</div><p class="cita">{_fmt(g("texto"))}</p>{a}</div>'
    if t in ("lista", "pasos"):
        lis = []
        for i, it in enumerate(g("items", [])):
            ics = g("iconos", [])
            if t == "lista" and i < len(ics):
                mark = f'<img class="ico" src="{_icono64(ics[i], ctx)}">'
            else:
                mark = f'<span class="num">{i + 1:02d}</span>' if t == "pasos" else ('<span class="tilde">✓</span>' if g("tildes") else '<span class="pt"></span>')
            lis.append(f"<li>{mark}<span>{_fmt(it)}</span></li>")
        return f'<div class="box">{h2(g("titulo"))}<ul class="lista">{"".join(lis)}</ul></div>'
    if t == "comparacion":
        col = lambda d, cls: (f'<div class="col {cls}"><h3>{_fmt(d.get("titulo", ""))}</h3><ul>' +
                              "".join(f"<li>{_fmt(x)}</li>" for x in d.get("items", [])) + "</ul></div>")
        return f'<div class="box">{h2(g("titulo"))}<div class="cmp">{col(g("izq", {}), "a")}{col(g("der", {}), "b")}</div></div>'
    if t == "dato":
        return f'<div class="box"><div class="numero">{_fmt(g("numero"))}</div>{pp(g("texto"))}</div>'
    if t == "chat":
        ms = "".join(f'<div class="msg {m.get("de", "ella")}">{_fmt(m["texto"])}</div>' for m in g("mensajes", []))
        return f'<div class="box">{h2(g("titulo"))}<div class="chat">{ms}</div></div>'
    if t == "respiro":
        return f'<div class="box"><p class="respiro">{_fmt(g("texto"))}</p></div>'
    if t == "pregunta":
        return f'<div class="box"><p class="pregunta">{_fmt(g("texto"))}</p></div>'
    if t == "cierre":
        return f'<div class="box">{pp(g("texto"))}<p class="accion">{_fmt(g("accion"))}</p></div>'
    raise ValueError(f"tipo de placa desconocido: {t}")


def html_carrusel(marca, carrusel):
    m = _marca(marca); c = {k: _hex(v) for k, v in m["colores"].items()}
    c.setdefault("medio", c["acento_suave"]); c.setdefault("blanco", "#ffffff")
    tip = m["tipografias"]
    placas = carrusel["placas"]
    fondos = _fondos(placas)
    secciones = []
    for i, (p, f) in enumerate(zip(placas, fondos)):
        tono = "claro" if f in CLAROS or f == "medio" else "oscuro"
        secciones.append(f'<section class="placa {p["tipo"]} bg-{f} tono-{tono}" data-n="{i + 1}">{_cuerpo(p, {"fondo": c["acento_suave"] if f not in ("acento_suave", "medio") else c["blanco"], "trazo": c["acento"]})}</section>')
    css = f"""
{_fontface('sans', tip['sans'])}
{_fontface('acento', tip['acento'])}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{background:#888;font-family:'sans';-webkit-font-smoothing:antialiased}}
.placa{{width:{W}px;height:{H}px;position:relative;overflow:hidden;display:flex;align-items:center;justify-content:center;padding:{M}px;margin-bottom:20px}}
.bg-claro{{background:{c['claro']}}} .bg-blanco{{background:{c['blanco']}}} .bg-acento_suave{{background:{c['acento_suave']}}}
.bg-medio{{background:{c['medio']}}} .bg-acento{{background:{c['acento']}}} .bg-oscuro{{background:{c['oscuro']}}}
.tono-claro{{color:{c['oscuro']};--ac:{c['acento']};--band:{c['acento_suave']};--suave:{c['acento']}}}
.tono-oscuro{{color:{c['claro']};--ac:{c['acento_suave']};--band:{c['acento']};--suave:{c['acento_suave']}}}
.bg-acento_suave{{--band:{c['blanco']}}} .bg-acento{{--band:{c['oscuro']};--ac:{c['acento_suave']}}} .bg-medio{{--ac:{c['oscuro']};--band:{c['claro']}}}
.box{{position:relative;z-index:2;width:100%;display:flex;flex-direction:column;gap:34px;text-align:left}}
.t{{font-weight:700;font-size:76px;line-height:1.06;letter-spacing:-.02em;text-wrap:balance}}
.t.portada{{font-size:104px;line-height:1.0}}
.x{{font-weight:400;font-size:40px;line-height:1.38;text-wrap:pretty;max-width:880px}}
em.ac{{font-family:'acento';font-style:italic;font-weight:500;color:var(--ac);font-size:1.12em;letter-spacing:0}}
b{{font-weight:700}}
.band{{background:linear-gradient(transparent 12%,var(--band) 12%,var(--band) 92%,transparent 92%);padding:0 .12em;box-decoration-break:clone;-webkit-box-decoration-break:clone}}
.comillas{{font-family:'acento';font-size:260px;line-height:.6;color:var(--ac);height:110px}}
.cita{{font-family:'acento';font-style:italic;font-weight:500;font-size:74px;line-height:1.12;text-wrap:balance}}
.autor{{font-size:32px;font-weight:600;letter-spacing:.08em;text-transform:uppercase;opacity:.8}}
.lista{{list-style:none;display:flex;flex-direction:column;gap:30px}}
.lista{{gap:18px}} .lista li{{display:flex;gap:26px;align-items:center;font-size:44px;line-height:1.25;font-weight:600;background:rgba(255,255,255,.55);border-radius:30px;padding:30px 36px}}
.tono-oscuro .lista li{{background:rgba(255,255,255,.08)}} .bg-blanco .lista li{{background:{c['claro']}}}
.num{{font-family:'acento';font-style:italic;font-size:78px;line-height:.8;color:var(--ac);min-width:96px}}
.tilde{{flex:none;width:58px;height:58px;border-radius:50%;background:var(--ac);color:{c['claro']};display:flex;align-items:center;justify-content:center;font-size:34px;font-weight:700}}
.tono-oscuro .tilde{{color:{c['oscuro']}}}
.ico{{flex:none;width:80px;height:80px}}
.pt{{flex:none;width:16px;height:16px;border-radius:50%;background:var(--ac);}}
.cmp{{display:grid;grid-template-columns:1fr 1fr;gap:26px}}
.col{{border-radius:28px;padding:40px 34px;display:flex;flex-direction:column;gap:22px}}
.col.a{{background:rgba(0,0,0,.06)}} .col.b{{background:var(--ac);color:{c['claro']}}}
.tono-oscuro .col.a{{background:rgba(255,255,255,.08)}} .tono-oscuro .col.b{{color:{c['oscuro']}}}
.col h3{{font-size:44px;font-weight:700;line-height:1.1}}
.col ul{{list-style:none;display:flex;flex-direction:column;gap:16px;font-size:36px;line-height:1.28}}
.numero{{font-family:'acento';font-weight:600;font-size:400px;line-height:.9;color:var(--ac);letter-spacing:-.03em}}
.chat{{display:flex;flex-direction:column;gap:20px}}
.msg{{max-width:78%;padding:26px 32px;border-radius:34px;font-size:34px;line-height:1.35}}
.msg.ella{{background:rgba(0,0,0,.07);border-bottom-left-radius:8px;align-self:flex-start}}
.tono-oscuro .msg.ella{{background:rgba(255,255,255,.1)}}
.msg.yo{{background:var(--ac);color:{c['claro']};border-bottom-right-radius:8px;align-self:flex-end}}
.respiro{{font-family:'acento';font-style:italic;font-weight:500;font-size:96px;line-height:1.08;text-align:center;text-wrap:balance}}
.respiro em.ac{{font-size:1em}}
.pregunta{{font-weight:700;font-size:92px;line-height:1.04;letter-spacing:-.02em;text-wrap:balance}}
.cierre .box{{align-items:flex-start}}
.accion{{font-weight:700;font-size:84px;line-height:1.05;letter-spacing:-.02em;text-wrap:balance}}
.ph{{position:absolute;background-size:cover;background-position:center 30%;z-index:1}}
.ph-full{{inset:0;filter:blur(18px) brightness(.85);transform:scale(1.08)}}
.velo{{position:absolute;inset:0;z-index:1;background:{c['oscuro']};opacity:.55}}
.fondo_foto{{color:{c['claro']};--ac:{c['acento_suave']}}}
.ph-der,.ph-izq{{top:0;bottom:0;width:58%}}
.ph-der{{right:0;-webkit-mask-image:linear-gradient(90deg,transparent,#000 38%)}}
.ph-izq{{left:0;-webkit-mask-image:linear-gradient(270deg,transparent,#000 38%)}}
.half-izq{{margin-right:auto;width:52%}} .half-der{{margin-left:auto;width:52%}}
.half-izq .t,.half-der .t{{font-size:66px}}
.ph-bottom{{left:0;right:0;bottom:0;height:68%;background-position:center 22%;-webkit-mask-image:linear-gradient(180deg,transparent,#000 30%)}}
.placa.portada:has(.ph) {{align-items:flex-start}}
"""
    return f"<!doctype html><html><head><meta charset='utf-8'><style>{css}</style></head><body>{''.join(secciones)}</body></html>"


REVISAR_JS = """() => [...document.querySelectorAll('.placa')].map(s => {
  const n = +s.dataset.n, prob = [];
  const r = s.getBoundingClientRect();
  s.querySelectorAll('.box *').forEach(e => {
    if (!e.childNodes.length || ![...e.childNodes].some(c => c.nodeType===3 && c.textContent.trim())) return;
    const b = e.getBoundingClientRect(), fs = parseFloat(getComputedStyle(e).fontSize);
    if (fs < 30) prob.push(`texto de ${Math.round(fs)} px (mínimo 30): "${e.textContent.trim().slice(0,30)}"`);
    if (b.top < r.top + 60 || b.bottom > r.bottom - 60 || b.left < r.left + 60 || b.right > r.right - 60)
      prob.push(`se sale del margen: "${e.textContent.trim().slice(0,30)}"`);
  });
  return {n, prob};
})"""


def _ajustar_js():
    # Achica títulos que no entran (sin bajar de 64 px, ni la portada de 90) antes de capturar
    return """() => document.querySelectorAll('.placa').forEach(s => {
      const box = s.querySelector('.box'); if (!box) return;
      const lim = () => box.scrollHeight > s.clientHeight - 180 || box.scrollWidth > box.clientWidth + 2;
      const t = s.querySelectorAll('.t,.pregunta,.accion,.respiro,.cita');
      let guard = 40;
      while (lim() && guard--) t.forEach(e => {
        const fs = parseFloat(getComputedStyle(e).fontSize), min = e.classList.contains('portada') ? 90 : 64;
        if (fs > min) e.style.fontSize = (fs - 3) + 'px';
      });
    })"""


def render(marca, carrusel, carpeta):
    from playwright.sync_api import sync_playwright
    import img2pdf
    from PIL import Image
    carrusel = json.load(open(carrusel)) if isinstance(carrusel, str) else carrusel
    os.makedirs(carpeta, exist_ok=True)
    doc = html_carrusel(marca, carrusel)
    open(os.path.join(carpeta, "carrusel.html"), "w").write(doc)
    pngs = []
    with sync_playwright() as p:
        nav = p.chromium.launch()
        pg = nav.new_page(viewport={"width": W, "height": H})
        pg.set_content(doc, wait_until="load")
        pg.evaluate("document.fonts.ready")
        pg.evaluate(_ajustar_js())
        problemas = pg.evaluate(REVISAR_JS)
        for i, s in enumerate(pg.query_selector_all(".placa")):
            out = os.path.join(carpeta, f"placa-{i + 1:02d}.png")
            s.screenshot(path=out); pngs.append(out)
        nav.close()
    with open(os.path.join(carpeta, "carrusel.pdf"), "wb") as f:
        f.write(img2pdf.convert(pngs))
    ims = [Image.open(x).convert("RGB").resize((270, 338)) for x in pngs]
    n = min(5, len(ims)); hoja = Image.new("RGB", (n * 270 + (n + 1) * 10, ((len(ims) + n - 1) // n) * 348 + 10), "#999")
    for i, im in enumerate(ims):
        hoja.paste(im, (10 + (i % n) * 280, 10 + (i // n) * 348))
    hoja.save(os.path.join(carpeta, "revision.jpg"), quality=88)
    avisos = [f"placa {x['n']}: {q}" for x in problemas for q in x["prob"]]
    fondos = _fondos(carrusel["placas"])
    avisos += [f"placas {i} y {i + 1}: mismo fondo ({fondos[i]})" for i in range(1, len(fondos)) if fondos[i] == fondos[i - 1]]
    for a in avisos:
        print("REVISAR:", a)
    if not avisos:
        print("Revisión automática: sin problemas (igual mirá revision.jpg)")
    return pngs, avisos


if __name__ == "__main__":
    render(sys.argv[1], sys.argv[2], sys.argv[3])
