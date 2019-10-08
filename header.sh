set -euo pipefail

cd "$(dirname "$0")" || exit

export SHANGREN_ROOT
export SHANGREN_ROOT="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
