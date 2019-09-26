# This script activates telepresence and activates pipenv
# source this script before doing any debugging with telepresence
# Run telepresence.sh first

PROJECT_ROOT="$( cd "$( dirname $1 )" >/dev/null 2>&1 && pwd )"
PROJECT_ROOT="$(dirname "$PROJECT_ROOT")"

test -f "$PROJECT_ROOT"/telepresence.dec && source "$PROJECT_ROOT"/telepresence.dec
