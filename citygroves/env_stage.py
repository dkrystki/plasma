#!../.venv/bin/python
import citygroves.env_comm


class Env(citygroves.env_comm.Env):
    emoji: str = "🤖"

    def __init__(self) -> None:
        super().__init__()

