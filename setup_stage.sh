source current_stage

case "$STAGE" in
  local)
    export CUSTOM_PS1=🐣 ;;
  stage)
    export CUSTOM_PS1=🤖 ;;
  prod)
    export CUSTOM_PS1=🔥 ;;
esac

export PIPENV_IGNORE_VIRTUALENVS=1

export SHANGREN_IP=192.168.0.5
export KUBECONFIG="$SHANGREN_ROOT"/envs/"$STAGE"/kubeconfig

scp shangren-"$STAGE"@"$SHANGREN_IP":/home/shangren-"$STAGE"/.kube/config "$SHANGREN_ROOT"/envs/"$STAGE"/kubeconfig > /dev/null
