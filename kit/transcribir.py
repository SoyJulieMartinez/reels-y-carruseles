"""Transcripción local con Whisper (faster-whisper), con tiempos por palabra.

    python3 -m kit.transcribir video.mp4 palabras.json

Si la descarga del modelo desde HuggingFace está bloqueada, lo baja desde npm
(paquetes @skillninja/shortmovie-telop-model-p0..p3, sin ejecutar scripts).
"""
import glob, hashlib, json, os, subprocess, sys, tarfile, tempfile, wave
import numpy as np

MODELO = os.path.expanduser("~/.cache/kit-whisper-small")


def _modelo_por_npm():
    os.makedirs(MODELO, exist_ok=True)
    tmp = tempfile.mkdtemp()
    for i in range(4):
        subprocess.run(["npm", "pack", "-q", f"@skillninja/shortmovie-telop-model-p{i}"], cwd=tmp, check=True, capture_output=True)
    for tgz in glob.glob(os.path.join(tmp, "*.tgz")):
        with tarfile.open(tgz) as t:
            t.extractall(os.path.join(tmp, os.path.basename(tgz)[:-4]), filter="data")
    p0 = glob.glob(os.path.join(tmp, "*p0*", "package"))[0]
    for f in ("config.json", "tokenizer.json", "vocabulary.json", "preprocessor_config.json"):
        open(os.path.join(MODELO, f), "wb").write(open(os.path.join(p0, f), "rb").read())
    with open(os.path.join(MODELO, "model.bin"), "wb") as out:
        for i in range(4):
            out.write(open(glob.glob(os.path.join(tmp, f"*p{i}*", "package", f"model.bin.part{i}"))[0], "rb").read())
    esperado = open(os.path.join(p0, "model.sha256")).read().split()[0]
    real = hashlib.sha256(open(os.path.join(MODELO, "model.bin"), "rb").read()).hexdigest()
    if esperado != real:
        raise RuntimeError("El modelo descargado no coincide con su sha256")
    return MODELO


def cargar_modelo():
    from faster_whisper import WhisperModel
    if os.path.exists(os.path.join(MODELO, "model.bin")):
        return WhisperModel(MODELO, device="cpu", compute_type="int8")
    try:
        return WhisperModel("small", device="cpu", compute_type="int8")
    except Exception:
        return WhisperModel(_modelo_por_npm(), device="cpu", compute_type="int8")


def transcribir(video, salida, idioma="es"):
    wav = salida + ".wav"
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", video, "-ac", "1", "-ar", "16000", wav], check=True)
    w = wave.open(wav)
    audio = np.frombuffer(w.readframes(w.getnframes()), np.int16).astype(np.float32) / 32768
    segs, _ = cargar_modelo().transcribe(audio, language=idioma, word_timestamps=True, vad_filter=False, beam_size=5)
    palabras = []
    for s in segs:
        print(f"[{s.start:6.2f}-{s.end:6.2f}] {s.text}", flush=True)
        for x in s.words:
            palabras.append({"text": x.word.strip(), "start": round(x.start, 3), "end": round(x.end, 3)})
    json.dump(palabras, open(salida, "w"), ensure_ascii=False, indent=1)
    os.remove(wav)
    return palabras


def listar(palabras_json):
    """Imprime índice:palabra(inicio) para poder corregir con {índice: 'texto'}."""
    w = json.load(open(palabras_json))
    print(" ".join(f"{i}:{x['text']}({x['start']:.2f})" for i, x in enumerate(w)))


if __name__ == "__main__":
    transcribir(sys.argv[1], sys.argv[2])
    listar(sys.argv[2])
