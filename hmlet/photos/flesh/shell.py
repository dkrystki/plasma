#!../../../.venv/bin/python3
import os
import sys
from tempfile import NamedTemporaryFile

sys.path.append("../../../../")


if __name__ == "__main__":
    with NamedTemporaryFile(mode='w+', buffering=True, delete=True) as tmprc:
        tmprc.write('source ~/.bashrc\n')
        tmprc.write("source .venv/bin/activate\n")

        os.system(f"bash --rcfile {tmprc.name}")
