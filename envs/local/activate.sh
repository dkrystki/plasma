
if [ "${BASH_SOURCE-}" = "$0" ]; then
    echo "You must source this script: \$ source $0" >&2
    exit 33
fi

export ROOT
ROOT="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
ROOT=$(dirname "$ROOT")
ROOT=$(dirname "$ROOT")

deactivate () {
    # reset old environment variables
    if ! [ -z "${_OLD_VIRTUAL_PATH:+_}" ] ; then
        PATH="$_OLD_VIRTUAL_PATH"
        export PATH
        unset _OLD_VIRTUAL_PATH
    fi
    if ! [ -z "${_OLD_VIRTUAL_PYTHONHOME:+_}" ] ; then
        PYTHONHOME="$_OLD_VIRTUAL_PYTHONHOME"
        export PYTHONHOME
        unset _OLD_VIRTUAL_PYTHONHOME
    fi

    if ! [ -z "${_OLD_KUBECONFIG_PATH:+_}" ] ; then
        KUBECONFIG="$_OLD_KUBECONFIG_PATH"
        export KUBECONFIG
        unset _OLD_KUBECONFIG_PATH
    fi
#
#    if ! [ -z "${_OLD_PYTHON_PATH:+_}" ] ; then
#        PYTHONPATH="$_OLD_PYTHON_PATH"
#        export PYTHONPATH
#        unset _OLD_PYTHON_PATH
#    fi

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

VIRTUAL_ENV="$ROOT/.venv"
export VIRTUAL_ENV
_OLD_VIRTUAL_PATH="$PATH"
PATH="$VIRTUAL_ENV/bin:$PATH"
export PATH

# unset PYTHONHOME if set
if ! [ -z "${PYTHONHOME+_}" ] ; then
    _OLD_VIRTUAL_PYTHONHOME="$PYTHONHOME"
    unset PYTHONHOME
fi

#_OLD_PYTHON_PATH="$PYTHONPATH"
#export PYTHONPATH
#PYTHONPATH="$ROOT/lib:$PYTHONPATH"

_OLD_KUBECONFIG_PATH="$KUBECONFIG"
export KUBECONFIG=~/.kube/config
minikube config set WantUpdateNotification false

eval "$(minikube -p shangren docker-env)"

# load settings
export $(grep -v '^#' "$ROOT"/settings.env | xargs -d '\n')

# do not try to push images after building
{
  skaffold config set --global local-cluster true
} &> /dev/null

_OLD_VIRTUAL_PS1="${PS1:-}"
if [ "x 🐣" != x ] ; then
    PS1="🐣${PS1:-}"
fi
export PS1


printenv > "$ROOT"/activate.env
