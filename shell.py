#!/usr/bin/env python3
import sys
sys.path.append("../")

import sys

from plasma import env
from plasma.comm.python.pl.shell import parser


if __name__ == "__main__":
    args = parser.parse_args(sys.argv[1:])

    env = env.PlasmaEnv()

    if args.dry_run:
        env.print_envs()
    else:
        env.shell()
