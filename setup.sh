#!/usr/bin/env bash
# Prepara todo lo necesario para editar reels y diseñar carruseles.
# Uso: bash setup.sh            (básico)
#      bash setup.sh --efectos  (además prepara los efectos de efectos/, opcional y más pesado)
#      bash setup.sh --todo     (efectos + HyperFrames + skills-edicion + Watch, desde sus repositorios oficiales)
set -e
cd "$(dirname "$0")"
echo "1/4 · Paquetes de Python"
pip install -q --break-system-packages -r requirements.txt 2>/dev/null || pip install -q -r requirements.txt
echo "2/4 · ffmpeg"
command -v ffmpeg >/dev/null || { (sudo apt-get install -y -qq ffmpeg || apt-get install -y -qq ffmpeg) >/dev/null; }
ffmpeg -hide_banner -filters 2>/dev/null | grep -q " ass " && echo "   ffmpeg con subtítulos ASS: ok"
echo "3/4 · Navegador para los carruseles"
python3 -c "from playwright.sync_api import sync_playwright as s; p=s().start(); p.chromium.launch().close(); p.stop()" 2>/dev/null \
  && echo "   Chromium: ok" || python3 -m playwright install chromium >/dev/null
echo "4/4 · Modelo de transcripción (Whisper small, ~500 MB, solo la primera vez)"
python3 -c "from kit.transcribir import cargar_modelo; cargar_modelo(); print('   Whisper: ok')"
if [ "$1" = "--efectos" ] || [ "$1" = "--todo" ]; then
  echo "Extra · efectos (recorte de persona, texto detrás de la silueta, 51 efectos)"
  bash efectos/scripts/setup.sh
fi
if [ "$1" = "--todo" ]; then
  EXT=~/kit-rc-extras; mkdir -p $EXT ~/.claude/skills
  echo "Extra · skills-edicion (incluye la CLI de HyperFrames y la biblioteca de estilos)"
  [ -d $EXT/skills-edicion ] || git clone -q --depth 1 https://github.com/NexumAI-online/skills-edicion.git $EXT/skills-edicion
  (cd $EXT/skills-edicion && npm ci --ignore-scripts --silent >/dev/null 2>&1 && echo "   ok") || echo "   no se pudo instalar (seguí sin esto)"
  echo "Extra · HyperFrames (skills de composición y catálogo de bloques)"
  [ -d $EXT/hyperframes ] || git clone -q --depth 1 --filter=blob:none --sparse https://github.com/heygen-com/hyperframes.git $EXT/hyperframes
  (cd $EXT/hyperframes && git sparse-checkout set skills >/dev/null 2>&1)
  for s in hyperframes hyperframes-cli hyperframes-registry media-use slideshow; do
    [ -d $EXT/hyperframes/skills/$s ] && rm -rf ~/.claude/skills/$s && cp -r $EXT/hyperframes/skills/$s ~/.claude/skills/
  done; echo "   ok"
  echo "Extra · Watch (mirar videos cuadro a cuadro)"
  pip install -q --break-system-packages yt-dlp 2>/dev/null || pip install -q yt-dlp
  [ -d $EXT/claude-video ] || git clone -q --depth 1 https://github.com/bradautomates/claude-video.git $EXT/claude-video
  rm -rf ~/.claude/skills/watch && cp -r $EXT/claude-video/skills/watch ~/.claude/skills/ && echo "   ok"
  HS=$(ls -d /opt/pw-browsers/chromium_headless_shell-*/chrome-headless-shell-linux64 2>/dev/null | head -1)
  [ -n "$HS" ] && echo "   Para renderizar con HyperFrames: export PRODUCER_HEADLESS_SHELL_PATH=$HS/chrome-headless-shell HYPERFRAMES_BROWSER_PATH=$HS/chrome-headless-shell"
fi
echo "Listo. Fuentes de la marca: se bajan solas de Google Fonts la primera vez que se usan."
