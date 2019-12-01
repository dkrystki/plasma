set -eo pipefail

CURRENT_DIR=$(pwd)

export SHANGREN_ROOT
export SHANGREN_ROOT="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

source "$SHANGREN_ROOT"/.settings

source "$SHANGREN_ROOT"/setup_stage.sh

PATH=$PATH:"$SHANGREN_ROOT"/bin

eval $SETUP_PS1

cd "$CURRENT_DIR"
