#!../.venv/bin/python
import argparse
import sys
from importlib import import_module


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('stage', type=str, default="local",
                        help='Stage to activate.', nargs="?")
    parser.add_argument('--dry-run', default=False, action="store_true")
    parser.add_argument('--save', default=False, action="store_true")

    args = parser.parse_args(sys.argv[1:])

    env = import_module(f"env_{args.stage}").Env()

    if args.dry_run:
        env.print_envs()
    else:
        env.shell()
