"""Evidencia para revisar un video ANTES de mostrárselo a la persona.

    python3 -m kit.revisar final.mp4 salida_revision/ [puntos.json]

Genera, sin tocar el video:
  - hoja.jpg: inicio, final y, por cada punto, el cuadro anterior, el del punto y el siguiente
    (para ver entradas, salidas y transiciones de los dos lados);
  - clips/: un clip de ~1 s alrededor de cada punto (para mirar el movimiento completo);
  - informe.json: huella SHA-256, datos técnicos, puntos y una lista de controles en estado
    "pendiente" que la revisión completa a mano (aprobado / falló / pendiente).

Esto NO aprueba nada: solo junta la evidencia. Si no se pudo mirar algo, queda pendiente.
Si no se pasan puntos y el video salió de kit.reel, se usa el puntos.json que deja el render.
"""
import hashlib, json, os, subprocess, sys
from PIL import Image, ImageDraw, ImageFont

CONTROLES = [
    "Hook completo y legible en el cuadro 0 (portada del feed)",
    "Subtítulos: coinciden con la voz, aparecen a tiempo, no se cortan ni tapan otra cosa",
    "Cada entrada y salida de títulos, chips, tarjetas y placas (todas, no solo la primera de cada tipo)",
    "Los dos lados de cada transición: sin flashes, sin escenas anticipadas, efectos que cortan con la cámara",
    "Encuadre: cara, pelo y manos sin tapar; nada en las zonas que tapa Instagram",
    "Marca: tipografías, colores y contraste correctos",
    "Cada gráfico o captura corresponde a lo que se dice en ese momento",
    "Audio: volumen parejo, sonidos que no tapan la voz, sincronía con la imagen",
    "Comienzo y final del archivo completo",
]


def _probe(video):
    out = subprocess.run(["ffprobe", "-v", "error", "-show_entries",
                          "format=duration:stream=codec_type,codec_name,width,height,r_frame_rate,color_transfer,color_primaries,sample_rate",
                          "-of", "json", video], capture_output=True, text=True, check=True).stdout
    return json.loads(out)


def _sha(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""):
            h.update(b)
    return h.hexdigest()


def _cuadro(video, t, ancho=270):
    r = subprocess.run(["ffmpeg", "-v", "error", "-ss", f"{max(0, t):.3f}", "-i", video, "-frames:v", "1",
                        "-vf", f"scale={ancho}:-2", "-f", "image2pipe", "-vcodec", "png", "-"], capture_output=True)
    from io import BytesIO
    return Image.open(BytesIO(r.stdout)).convert("RGB") if r.stdout else None


def revisar(video, salida, puntos=None, fps=30):
    if os.path.exists(salida):
        raise SystemExit(f"La carpeta {salida} ya existe: usá un nombre nuevo para cada revisión (revision-v2, v3...).")
    info = _probe(video)
    dur = float(info["format"]["duration"])
    if puntos is None:
        auto = video + ".puntos.json"
        puntos = json.load(open(auto)) if os.path.exists(auto) else []
    elif isinstance(puntos, str):
        puntos = json.load(open(puntos))
    puntos = sorted({round(p, 3) for p in puntos if 0 < p < dur})
    os.makedirs(os.path.join(salida, "clips"))
    paso = 1 / fps
    celdas = [("inicio 0.00", 0.0)]
    for p in puntos:
        celdas += [(f"{p:.2f} antes", p - paso), (f"{p:.2f}", p), (f"{p:.2f} después", p + paso)]
    celdas.append((f"final {dur:.2f}", dur - 2 * paso))
    ims = [(et, _cuadro(video, t)) for et, t in celdas]
    ims = [(et, im) for et, im in ims if im]
    w, h = ims[0][1].size
    n = 9
    hoja = Image.new("RGB", (n * w, ((len(ims) + n - 1) // n) * (h + 34)), "white")
    d = ImageDraw.Draw(hoja)
    try:
        f = ImageFont.truetype("DejaVuSans.ttf", 20)
    except OSError:
        f = ImageFont.load_default()
    for i, (et, im) in enumerate(ims):
        x, y = (i % n) * w, (i // n) * (h + 34)
        hoja.paste(im, (x, y + 34)); d.text((x + 8, y + 6), et, fill="black", font=f)
    hoja.save(os.path.join(salida, "hoja.jpg"), quality=85)
    clips = []
    for p in puntos:
        c = os.path.join(salida, "clips", f"{p:07.2f}.mp4")
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", f"{max(0, p - 0.5):.3f}", "-i", video, "-t", "1.0",
                        "-vf", "scale=540:-2", "-c:v", "libx264", "-preset", "veryfast", "-crf", "26", "-c:a", "aac", c], check=True)
        clips.append(c)
    informe = {
        "video": os.path.abspath(video), "sha256": _sha(video), "duracion": dur, "ffprobe": info,
        "puntos": puntos, "hoja": "hoja.jpg", "clips": [os.path.relpath(c, salida) for c in clips],
        "controles": [{"control": c, "estado": "pendiente", "evidencia": "", "correccion": ""} for c in CONTROLES],
        "nota": "Esto es evidencia, no aprobación. Completar cada control con aprobado / falló / pendiente.",
    }
    json.dump(informe, open(os.path.join(salida, "informe.json"), "w"), ensure_ascii=False, indent=1)
    print(f"Revisión lista en {salida}: hoja.jpg, {len(clips)} clips, informe.json")
    return informe


if __name__ == "__main__":
    revisar(sys.argv[1], sys.argv[2], sys.argv[3] if len(sys.argv) > 3 else None)
