#!../.venv/bin/python3
import sys
sys.path.append("../../")

from importlib import import_module
from plasma.shell import parser


if __name__ == "__main__":
    args = parser.parse_args(sys.argv[1:])

    env = import_module(f"aux.env_{args.stage}").AuxEnv()

    if args.save:
        env.dump_dot_env()

    if args.dry_run:
        env.print_envs()
    else:
        env.shell()
