#!../.venv/bin/python
import citygroves.frontend.env_comm
import citygroves.env_local


class Local(citygroves.frontend.env_comm.Env):
    emoji: str = "🐣"

    def __init__(self) -> None:
        super().__init__()
        self.parent = citygroves.env_local.Local()
