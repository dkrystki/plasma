from dataclasses import dataclass

from plasma.aux.env_comm import AuxEnvComm
import subprocess


@dataclass
class AuxEnv(AuxEnvComm):
    def __init__(self):
        self.stage = "local"
        self.emoji = "🐣"
        super().__init__()
        self.graylog = AuxEnvComm.Graylog(address="aux.graylog.local")
        self.sentry = AuxEnvComm.Sentry(address="aux.sentry.local")
        self.registry = AuxEnvComm.Registry(address="aux.registry.local",
                                       username="user",
                                       password="password")

        ip: str = subprocess.check_output("hostname -I", shell=True).split()[0].decode("utf-8")
        self.device.ip = ip
        self.device.name = "auxiliary-local"
