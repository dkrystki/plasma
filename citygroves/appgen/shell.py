#!../../.venv/bin/python3
import sys
sys.path.append("../../../")

from importlib import import_module
from plasma.comm.python.pl.shell import parser


if __name__ == "__main__":

    env = import_module(f"plasma.citygroves.appgen.env_{args.stage}").AppgenEnv()

    if args.save:
        env.dump_dot_env()

    if args.dry_run:
        env.print_envs()
    else:
        env.shell()
