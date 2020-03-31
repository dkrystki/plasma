import argparse

parser = argparse.ArgumentParser()
parser.add_argument('stage', type=str, default="local",
                    help='Stage to activate.', nargs="?")
parser.add_argument('--dry-run', default=False, action="store_true")
parser.add_argument('--save', default=False, action="store_true")
