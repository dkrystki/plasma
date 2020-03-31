#!/usr/bin/env python3
import sys
sys.path.append("../../")

from importlib import import_module
from plasma.shell import parser


if __name__ == "__main__":
    args = parser.parse_args(sys.argv[1:])

    env = import_module(f"env_{args.stage}").Env()

    if args.save:
        env.dump_dot_env()

    if args.dry_run:
        env.print_envs()
    else:
        env.shell()
