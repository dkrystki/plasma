
ROOT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
ROOT_DIR=`dirname "$ROOT_DIR"`
ROOT_DIR=`dirname "$ROOT_DIR"`

deactivate () {
    # reset old environment variables
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

    unset
}

# unset irrelevant variables
deactivate nondestructive

_OLD_KUBECONFIG_PATH="$KUBECONFIG"
export KUBECONFIG=~/.kube/config
minikube config set WantUpdateNotification false
{
  skaffold config set --global local-cluster true
} &> /dev/null
source ""$ROOT_DIR"/dataprovs/.env"
export SHANGREN_IP=`minikube -p shangren ip`

_OLD_VIRTUAL_PS1="${PS1:-}"
if [ "x 🐣" != x ] ; then
    PS1="🐣${PS1:-}"
fi
export PS1
