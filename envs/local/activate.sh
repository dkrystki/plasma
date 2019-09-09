
if [ "${BASH_SOURCE-}" = "$0" ]; then
    echo "You must source this script: \$ source $0" >&2
    exit 33
fi

ROOT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
ROOT_DIR=$(dirname "$ROOT_DIR")
ROOT_DIR=$(dirname "$ROOT_DIR")

deactivate () {
    # reset old environment variables
    if ! [ -z "${_OLD_VIRTUAL_PATH:+_}" ] ; then
        PATH="$_OLD_VIRTUAL_PATH"
        export PATH
        unset _OLD_VIRTUAL_PATH
    fi
    if ! [ -z "${_OLD_VIRTUAL_PYTHONHOME+_}" ] ; then
        PYTHONHOME="$_OLD_VIRTUAL_PYTHONHOME"
        export PYTHONHOME
        unset _OLD_VIRTUAL_PYTHONHOME
    fi

    if [ -n "${_OLD_KUBECONFIG_PATH:-}" ] ; then
        KUBECONFIG="${_OLD_KUBECONFIG_PATH:-}"
        export KUBECONFIG
        unset _OLD_KUBECONFIG_PATH
    fi

    if [ -n "${_OLD_VIRTUAL_PS1:-}" ] ; then
        PS1="${_OLD_VIRTUAL_PS1:-}"
        export PS1
        unset _OLD_VIRTUAL_PS1
    fi

    if [ ! "$1" = "nondestructive" ] ; then
    # Self destruct!
        unset -f deactivate
    fi
}

# unset irrelevant variables
deactivate nondestructive

VIRTUAL_ENV=".venv"
export VIRTUAL_ENV
_OLD_VIRTUAL_PATH="$PATH"
PATH="$VIRTUAL_ENV/bin:$PATH"
export PATH

# unset PYTHONHOME if set
if ! [ -z "${PYTHONHOME+_}" ] ; then
    _OLD_VIRTUAL_PYTHONHOME="$PYTHONHOME"
    unset PYTHONHOME
fi

_OLD_KUBECONFIG_PATH="$KUBECONFIG"
export KUBECONFIG=~/.kube/config
minikube config set WantUpdateNotification false

# do not try to push images after building
{
  skaffold config set --global local-cluster true
} &> /dev/null

source ""$ROOT_DIR"/dataprovs/.env"

_OLD_VIRTUAL_PS1="${PS1:-}"
if [ "x 🐣" != x ] ; then
    PS1="🐣${PS1:-}"
fi
export PS1
