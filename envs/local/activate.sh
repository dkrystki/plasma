

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
}

# unset irrelevant variables
deactivate nondestructive

_OLD_KUBECONFIG_PATH="$KUBECONFIG"
export KUBECONFIG=~/.kube/config
eval "$(minikube -p shangren docker-env)"
{
  skaffold config set --global local-cluster true
} &> /dev/null

_OLD_VIRTUAL_PS1="${PS1:-}"
if [ "x \e[32m(local) " != x ] ; then
    PS1="\e[32m(local) ${PS1:-}"
fi
export PS1
