#!../.venv/bin/python
from citygroves.env_comm import Env


class Local(Env):
    emoji: str = "🐣"

    def __init__(self) -> None:
        super().__init__()

