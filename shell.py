#!/usr/bin/env python3
import sys
sys.path.append("../")

import sys

from plasma.comm.python.pl.env import Env
from plasma.comm.python.pl.shell import parser


if __name__ == "__main__":
    args = parser.parse_args(sys.argv[1:])

    env = Env()

    if args.save:
        env.dump_dot_env()

    if args.dry_run:
        env.print_envs()
    else:
        env.shell()
