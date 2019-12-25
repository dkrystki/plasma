import environ

from comm.python.plasma.utils.deploy import Namespace

env = environ.Env()

stage = env.str("STAGE")

if stage == "local":
    namespace = Namespace("citygroves-local")
elif stage == "stage":
    namespace = Namespace("citygroves-stage")
elif stage == "prod":
    namespace = Namespace("citygroves-prod")
