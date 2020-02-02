import environ

from plasma.utils.deploy import Namespace

env = environ.Env()

stage = env.str("STAGE")
namespace = Namespace(f"citygroves-{stage}")
