#!.venv/bin/python
import argparse
import sys

from plasma.env import Env


parser = argparse.ArgumentParser()
parser.add_argument('stage', type=str, default="local",
                    help='Stage to activate.', nargs="?")
parser.add_argument('--dry-run', default=False, action="store_true")
parser.add_argument('--save', default=False, action="store_true")


if __name__ == "__main__":
    args = parser.parse_args(sys.argv[1:])

    env = Env()

    if args.save:
        env.dump_dot_env()

    if args.dry_run:
        env.print_envs()
    else:
        env.shell()
