set -euo pipefail

export SHANGREN_ROOT
export SHANGREN_ROOT="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

source "$SHANGREN_ROOT"/setup_stage.sh

PATH=$PATH:"$SHANGREN_ROOT"/bin

eval $SETUP_PS1
