import plasma.citygroves.env_comm


class Env(plasma.citygroves.env_comm.Env):
    emoji: str = "🤖"
    stage: str = "stage"

    def __init__(self) -> None:
        super().__init__()

