#!/bin/bash
set -e

# --- Окружение 1: venv (Python 3.9) ---
python3.9 -m venv pr1
source pr1/bin/activate
pip install --upgrade pip
pip install -r req.txt
pip list
python script.py
deactivate

# --- Окружение 2: conda ---
source "$(conda info --base)/etc/profile.d/conda.sh"
# принятие условий использования каналов Anaconda (требует conda)
conda tos accept --override-channels \
    --channel https://repo.anaconda.com/pkgs/main
conda tos accept --override-channels \
    --channel https://repo.anaconda.com/pkgs/r
conda env create -f env.yml
conda activate first
python script2.py
conda deactivate
