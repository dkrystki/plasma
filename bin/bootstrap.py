#!/usr/bin/python3

import os
from pathlib import Path

import subprocess


main_dir = Path(os.path.dirname(os.path.realpath(__file__))).parents[0]

os.chdir(main_dir)
subprocess.call(f"python3 -m venv {str(main_dir)}/.venv", shell=True)

python: str = f".venv/bin/python"
pip: str = f".venv/bin/pip"

subprocess.call(f"{pip} install -r requirements.txt", shell=True)
