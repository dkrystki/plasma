set -eo pipefail

export PROJECT_ROOT
PROJECT_ROOT="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
export PLASMA_ROOT
PLASMA_ROOT="$( dirname "$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )")"
export PLASMA_COMM_ROOT="$PLASMA_ROOT/comm"

export SETUP_PS1="export CUSTOM_PS1=\"\$STAGE_EMOJI(\$APP_NAME)\""

source "$PROJECT_ROOT"/.settings

source "$PLASMA_COMM_ROOT/bash/setup_stage.sh"

PATH=$PATH:"$PROJECT_ROOT"/bin

export MONOREPO_ROOT=$(dirname "$PROJECT_ROOT")

export PYTHONPATH="$MONOREPO_ROOT$PYTHONPATH"

eval $SETUP_PS1
