#!../.venv/bin/python
from shangren.env_comm import Env


class Local(Env):
    emoji: str = "🐣"

    def __init__(self) -> None:
        super().__init__()

