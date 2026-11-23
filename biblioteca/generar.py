"""Genera la biblioteca de recursos en HTML (para elegir) y en Markdown (para Claude).

    python3 biblioteca/generar.py
"""
import html, json, os, sys

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
from recursos import SECCIONES  # noqa: E402

RAIZ = os.path.dirname(AQUI)
SOLO_CARRUSEL = {"carruseles", "iconos"}
SOLO_REEL = {"ritmo", "formatos", "hook", "subtitulos", "textos", "efectos", "transiciones", "sonidos", "color", "cierre"}


def markdown():
    out = ["# Biblioteca de recursos (referencia para Claude)", "",
           "Cada recurso tiene un código. Cuando la persona pide por código o por nombre (por ejemplo \"R3, F03, E-backdrop-word, SND-whoosh\"), "
           "buscalo acá: la última columna dice con qué se hace. La versión para elegir es `biblioteca/biblioteca-de-recursos.html`.", "",
           "Reglas al usarla:",
           "- Lo que elige la persona manda, pero si un recurso no encaja con lo que dice en ese momento, proponé una alternativa en una línea.",
           "- Nunca repetir el mismo recurso dos veces seguidas. Los efectos terminan en un corte de cámara.",
           "- \"motor\" = `kit/reel.py`; \"efectos\" = `efectos/scripts/fx.py`; \"earshot\", \"real-sfx\" y \"HyperFrames\" se instalan con `bash setup.sh --todo`.",
           "- Si una herramienta extra no está instalada, usar lo más parecido del motor y decirlo en la entrega.", ""]
    for s in SECCIONES:
        out += [f"## {s['titulo']}", "", s["intro"], ""]
        for g, items in s["grupos"]:
            if g:
                out += [f"### {g}", ""]
            out += ["| Código | Nombre | Qué es | Cómo se hace |", "|---|---|---|---|"]
            for c, n, d, como in items:
                out.append(f"| `{c}` | {n} | {d.replace('|', '/')} | {como.replace('|', '/')} |")
            out.append("")
    open(os.path.join(RAIZ, "docs", "biblioteca-de-recursos.md"), "w").write("\n".join(out))


def html_page():
    secciones = []
    nav = []
    for s in SECCIONES:
        modo = "carrusel" if s["clave"] in SOLO_CARRUSEL else "reel"
        if s["clave"] == "iconos":
            modo = "ambos"
        nav.append(f'<a href="#{s["clave"]}" data-modo="{modo}">{html.escape(s["titulo"])}</a>')
        grupos = []
        for g, items in s["grupos"]:
            cards = []
            for c, n, d, _ in items:
                cards.append(
                    f'<button type="button" class="item" data-codigo="{html.escape(c)}" data-nombre="{html.escape(n)}" '
                    f'data-seccion="{html.escape(s["titulo"])}" data-unico="{0 if s["multiple"] else 1}" aria-pressed="false">'
                    f'<span class="n">{html.escape(n)}</span>'
                    + (f'<span class="d">{html.escape(d)}</span>' if d else "")
                    + f'<span class="c">{html.escape(c)}</span></button>')
            grupos.append((f'<h3>{html.escape(g)}</h3>' if g else "") + f'<div class="grid{" grid-ico" if s["clave"] == "iconos" else ""}">{"".join(cards)}</div>')
        secciones.append(
            f'<section id="{s["clave"]}" data-modo="{modo}"><div class="sec-head"><h2>{html.escape(s["titulo"])}</h2>'
            f'<p>{html.escape(s["intro"])}</p></div>{"".join(grupos)}</section>')
    total = sum(len(items) for s in SECCIONES for _, items in s["grupos"])
    return PLANTILLA.replace("{{NAV}}", "".join(nav)).replace("{{SECCIONES}}", "".join(secciones)).replace("{{TOTAL}}", str(total))


PLANTILLA = r"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Biblioteca de recursos · Reels y carruseles con Claude</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;1,500&family=Poppins:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>
:root{--lino:#f4efe9;--blush:#ebcdcb;--rosa:#d6a5a7;--palo:#a9666b;--carbon:#2f2a2b;--blanco:#fff;--linea:#e2d8d1}
*{box-sizing:border-box;margin:0;padding:0}
html{scroll-behavior:smooth;scroll-padding-top:120px}
body{font-family:Poppins,system-ui,sans-serif;background:var(--lino);color:var(--carbon);line-height:1.45;padding-bottom:140px}
.wrap{max-width:1120px;margin:0 auto;padding:0 20px}
header.top{padding:56px 0 28px}
.eyebrow{font-size:12px;letter-spacing:.14em;text-transform:uppercase;color:var(--palo);font-weight:600}
h1{font-size:clamp(34px,6vw,60px);line-height:1.02;letter-spacing:-.02em;font-weight:700;margin:10px 0 14px}
h1 em,h2 em{font-family:"Cormorant Garamond",serif;font-style:italic;font-weight:500;color:var(--palo);letter-spacing:0}
.lead{font-size:17px;max-width:720px}
.pasos{display:flex;gap:10px;flex-wrap:wrap;margin-top:22px}
.pasos span{background:var(--blanco);border:1px solid var(--linea);border-radius:999px;padding:8px 14px;font-size:14px}
.pasos b{color:var(--palo)}
.barra{position:sticky;top:0;z-index:5;background:rgba(244,239,233,.94);backdrop-filter:blur(8px);border-bottom:1px solid var(--linea)}
.barra .wrap{display:flex;flex-direction:column;gap:10px;padding-top:12px;padding-bottom:10px}
.fila{display:flex;gap:10px;align-items:center;flex-wrap:wrap}
.modo{display:inline-flex;background:var(--blanco);border:1px solid var(--linea);border-radius:999px;padding:4px}
.modo button{border:0;background:none;font:600 14px Poppins;padding:8px 16px;border-radius:999px;cursor:pointer;color:var(--carbon)}
.modo button[aria-pressed=true]{background:var(--carbon);color:var(--lino)}
input[type=search]{flex:1;min-width:180px;font:15px Poppins;padding:10px 14px;border:1px solid var(--linea);border-radius:999px;background:var(--blanco);color:var(--carbon)}
input[type=search]:focus,textarea:focus,button:focus-visible{outline:2px solid var(--palo);outline-offset:2px}
nav.secs{display:flex;gap:6px;overflow-x:auto;scrollbar-width:none}
nav.secs::-webkit-scrollbar{display:none}
nav.secs a{flex:none;font-size:13px;text-decoration:none;color:var(--carbon);padding:6px 12px;border-radius:999px;border:1px solid transparent}
nav.secs a:hover{border-color:var(--linea);background:var(--blanco)}
section{padding:40px 0 8px}
.sec-head{display:flex;flex-direction:column;gap:4px;margin-bottom:16px}
h2{font-size:clamp(24px,3.4vw,34px);letter-spacing:-.01em;font-weight:700}
.sec-head p{color:#6b5f60;font-size:15px}
h3{font-size:13px;letter-spacing:.12em;text-transform:uppercase;color:var(--palo);font-weight:600;margin:22px 0 10px}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(240px,1fr));gap:10px}
.grid-ico{grid-template-columns:repeat(auto-fill,minmax(140px,1fr))}
.item{position:relative;text-align:left;font:inherit;color:inherit;background:var(--blanco);border:1.5px solid var(--linea);border-radius:18px;padding:14px 16px 12px;cursor:pointer;display:flex;flex-direction:column;gap:4px;transition:border-color .15s,background .15s,transform .1s}
.item:hover{border-color:var(--rosa)}
.item:active{transform:scale(.99)}
.item .n{font-weight:600;font-size:15px;padding-right:26px}
.item .d{font-size:13.5px;color:#5e5354}
.item .c{font-size:11px;color:#9a8d8e;letter-spacing:.04em;margin-top:4px}
.item::after{content:"";position:absolute;top:13px;right:13px;width:20px;height:20px;border-radius:50%;border:1.5px solid var(--rosa)}
.item[aria-pressed=true]{background:var(--blush);border-color:var(--palo)}
.item[aria-pressed=true]::after{background:var(--palo) url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 20 20'%3E%3Cpath d='M5 10.5l3.2 3L15 7' fill='none' stroke='%23fff' stroke-width='2.4' stroke-linecap='round' stroke-linejoin='round'/%3E%3C/svg%3E") center/16px no-repeat;border-color:var(--palo)}
.oculto{display:none!important}
.vacio{padding:40px 0;text-align:center;color:#6b5f60}
/* pedido */
.pedido{position:fixed;left:0;right:0;bottom:0;z-index:10;background:var(--carbon);color:var(--lino);border-radius:22px 22px 0 0;box-shadow:0 -10px 40px rgba(47,42,43,.25)}
.pedido .wrap{padding-top:14px;padding-bottom:16px}
.pedido-top{display:flex;align-items:center;gap:12px;justify-content:space-between}
.pedido-top strong{font-size:16px}
.pedido-top strong em{font-family:"Cormorant Garamond",serif;font-style:italic;font-weight:500;color:var(--blush);font-size:20px}
.btn{font:600 14px Poppins;border-radius:999px;padding:10px 18px;border:0;cursor:pointer}
.btn-claro{background:var(--blush);color:var(--carbon)}
.btn-borde{background:none;color:var(--lino);border:1px solid rgba(244,239,233,.35)}
.pedido-cuerpo{display:none;margin-top:14px;max-height:62vh;overflow:auto}
.pedido.abierto .pedido-cuerpo{display:block}
.pedido label{display:block;font-size:13px;margin:4px 0 6px;color:var(--blush)}
.pedido textarea{width:100%;font:14px Poppins;border-radius:14px;border:0;padding:12px;background:#3b3536;color:var(--lino);resize:vertical}
#mensaje{min-height:220px;font-size:13.5px;white-space:pre-wrap}
.acciones{display:flex;gap:8px;margin-top:10px;flex-wrap:wrap}
.aviso{font-size:13px;color:var(--blush);margin-left:4px;align-self:center}
footer{padding:40px 0 20px;font-size:13px;color:#6b5f60}
@media (max-width:640px){.grid{grid-template-columns:1fr}.grid-ico{grid-template-columns:repeat(2,1fr)}header.top{padding-top:36px}}
@media (prefers-reduced-motion:reduce){html{scroll-behavior:auto}.item{transition:none}}
</style>
</head>
<body>
<header class="top wrap">
  <div class="eyebrow">Reels y carruseles con Claude</div>
  <h1>Biblioteca de <em>recursos</em></h1>
  <p class="lead">¿No tenés referencias o no sabés qué pedir? Tocá los recursos que te gustan: tipo de video, efectos, sonidos, transiciones, cierre. Al final copiás el pedido y lo pegás en tu Proyecto de Claude junto con tu video. Tu identidad visual ya está en tu ficha: esto suma <em>cómo</em> querés que se vea.</p>
  <div class="pasos"><span><b>1</b> Elegí reel o carrusel</span><span><b>2</b> Tocá lo que te gusta</span><span><b>3</b> Copiá tu pedido</span></div>
</header>
<div class="barra">
  <div class="wrap">
    <div class="fila">
      <div class="modo" role="group" aria-label="Qué estás armando">
        <button type="button" data-modo="reel" aria-pressed="true">Reel</button>
        <button type="button" data-modo="carrusel" aria-pressed="false">Carrusel</button>
      </div>
      <input type="search" id="buscar" placeholder="Buscar: pantalla dividida, whoosh, lista…" aria-label="Buscar recursos">
    </div>
    <nav class="secs" aria-label="Secciones">{{NAV}}</nav>
  </div>
</div>
<main class="wrap">
  {{SECCIONES}}
  <p class="vacio oculto" id="vacio">No hay recursos con esa palabra. Probá con otra o escribilo en las notas de tu pedido.</p>
</main>
<footer class="wrap">{{TOTAL}} recursos. Creado por Julie Martínez · @soyjuliemartinez</footer>

<div class="pedido" id="pedido">
  <div class="wrap">
    <div class="pedido-top">
      <strong>Tu pedido · <em id="cuenta">nada elegido</em></strong>
      <button type="button" class="btn btn-claro" id="ver" aria-expanded="false">Ver y copiar</button>
    </div>
    <div class="pedido-cuerpo">
      <label for="notas">Notas (opcional): qué dice tu video, una palabra clave, un sonido que no está en la lista…</label>
      <textarea id="notas" rows="2" placeholder="Ej.: la palabra clave del cierre es GUÍA; en el segundo 20 hablo de mis 3 servicios"></textarea>
      <label for="mensaje" style="margin-top:12px">Mensaje para pegar en Claude</label>
      <textarea id="mensaje" readonly></textarea>
      <div class="acciones">
        <button type="button" class="btn btn-claro" id="copiar">Copiar pedido</button>
        <button type="button" class="btn btn-borde" id="limpiar">Empezar de nuevo</button>
        <span class="aviso" id="aviso" role="status"></span>
      </div>
    </div>
  </div>
</div>

<script>
(function(){
  var items=[].slice.call(document.querySelectorAll('.item'));
  var modo='reel';
  var guardado={};
  try{guardado=JSON.parse(localStorage.getItem('biblioteca-pedido')||'{}')}catch(e){}
  (guardado.codigos||[]).forEach(function(c){var b=document.querySelector('.item[data-codigo="'+c+'"]');if(b)b.setAttribute('aria-pressed','true')});
  if(guardado.notas)document.getElementById('notas').value=guardado.notas;
  if(guardado.modo)modo=guardado.modo;

  function elegidos(todos){return items.filter(function(b){return b.getAttribute('aria-pressed')==='true'&&(todos||!b.closest('section').classList.contains('oculto'))})}
  function guardar(){try{localStorage.setItem('biblioteca-pedido',JSON.stringify({codigos:elegidos(true).map(function(b){return b.dataset.codigo}),notas:document.getElementById('notas').value,modo:modo}))}catch(e){}}

  function mensaje(){
    var sel=elegidos();
    var porSec={},orden=[];
    sel.forEach(function(b){var s=b.dataset.seccion;if(!porSec[s]){porSec[s]=[];orden.push(s)}porSec[s].push(b.dataset.codigo+' '+b.dataset.nombre)});
    var notas=document.getElementById('notas').value.trim();
    var t=(modo==='reel'?'Editá este video':'Diseñá este carrusel')+' usando estos recursos de la biblioteca (docs/biblioteca-de-recursos.md), con mi identidad visual de la ficha:\n';
    if(!orden.length)t+='\n(Todavía no elegiste nada: tocá los recursos que te gustan.)\n';
    orden.forEach(function(s){t+='\n• '+s+': '+porSec[s].join(' · ')});
    if(notas)t+='\n\nNotas: '+notas;
    t+='\n\nSi algún recurso no encaja con lo que digo en ese momento, proponeme una alternativa antes de editar.';
    return t;
  }
  function actualizar(){
    var n=elegidos().length;
    document.getElementById('cuenta').textContent=n?(n+(n===1?' recurso':' recursos')):'nada elegido';
    document.getElementById('mensaje').value=mensaje();
    guardar();
  }
  items.forEach(function(b){b.addEventListener('click',function(){
    var on=b.getAttribute('aria-pressed')!=='true';
    if(on&&b.dataset.unico==='1'){items.filter(function(x){return x.dataset.seccion===b.dataset.seccion}).forEach(function(x){x.setAttribute('aria-pressed','false')})}
    b.setAttribute('aria-pressed',on?'true':'false');actualizar();
  })});

  function aplicarModo(){
    [].forEach.call(document.querySelectorAll('.modo button'),function(b){b.setAttribute('aria-pressed',b.dataset.modo===modo?'true':'false')});
    [].forEach.call(document.querySelectorAll('section[data-modo], nav.secs a'),function(el){var m=el.dataset.modo;el.classList.toggle('oculto',!(m==='ambos'||m===modo))});
    actualizar();
  }
  [].forEach.call(document.querySelectorAll('.modo button'),function(b){b.addEventListener('click',function(){modo=b.dataset.modo;aplicarModo();filtrar()})});

  function norm(s){return s.toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g,'')}
  function filtrar(){
    var q=norm(document.getElementById('buscar').value.trim()),hay=false;
    [].forEach.call(document.querySelectorAll('main section'),function(sec){
      if(sec.classList.contains('oculto'))return;
      var vis=0;
      [].forEach.call(sec.querySelectorAll('.item'),function(b){var ok=!q||norm(b.textContent).indexOf(q)>=0;b.classList.toggle('oculto',!ok);if(ok)vis++});
      [].forEach.call(sec.querySelectorAll('h3'),function(h){var g=h.nextElementSibling;h.classList.toggle('oculto',!g.querySelector('.item:not(.oculto)'))});
      sec.style.display=vis?'':'none';if(vis)hay=true;
    });
    document.getElementById('vacio').classList.toggle('oculto',hay);
  }
  document.getElementById('buscar').addEventListener('input',filtrar);
  document.getElementById('notas').addEventListener('input',actualizar);

  var ped=document.getElementById('pedido'),ver=document.getElementById('ver');
  ver.addEventListener('click',function(){var a=ped.classList.toggle('abierto');ver.setAttribute('aria-expanded',a);ver.textContent=a?'Cerrar':'Ver y copiar'});
  document.getElementById('copiar').addEventListener('click',function(){
    var t=document.getElementById('mensaje'),av=document.getElementById('aviso');
    function listo(){av.textContent='¡Copiado! Pegalo en tu Proyecto de Claude con tu video.'}
    function manual(){t.focus();t.select();av.textContent='Seleccioné el texto: copialo con Ctrl+C o Cmd+C.'}
    try{navigator.clipboard.writeText(t.value).then(listo,manual)}catch(e){manual()}
  });
  document.getElementById('limpiar').addEventListener('click',function(){items.forEach(function(b){b.setAttribute('aria-pressed','false')});document.getElementById('notas').value='';document.getElementById('aviso').textContent='';actualizar()});
  aplicarModo();
})();
</script>
</body>
</html>
"""

if __name__ == "__main__":
    markdown()
    out = os.path.join(AQUI, "biblioteca-de-recursos.html")
    open(out, "w").write(html_page())
    print("ok:", out)
