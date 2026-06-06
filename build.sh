#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"

python3 -m venv .venv
.venv/bin/pip install -q pyinstaller
.venv/bin/pyinstaller --onefile --windowed --name atenea_basurilla atenea_basurilla.py

echo "listo: dist/atenea_basurilla"
