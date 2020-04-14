#!../.venv/bin/python3
import sys
sys.path.append("../../")


if __name__ == "__main__":
    from importlib import import_module
    from plasma.comm.python.pl.shell import parser

    args = parser.parse_args(sys.argv[1:])

    env = import_module(f"plasma.hmlet.env_{args.stage}").HmletEnv()

    if args.save:
        env.dump_dot_env()

    if args.dry_run:
        env.print_envs()
    else:
        env.shell()
