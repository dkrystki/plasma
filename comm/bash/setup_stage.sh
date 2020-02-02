source "$PROJECT_ROOT"/.current_stage

case "$STAGE" in
  test)
    export STAGE_EMOJI=🛠️. ;;
  local)
    export STAGE_EMOJI=🐣 ;;
  stage)
    export STAGE_EMOJI=🤖 ;;
  prod)
    export STAGE_EMOJI=🔥 ;;
esac

export PIPENV_IGNORE_VIRTUALENVS=1

export SHANGREN_IP=192.168.0.5
export KUBECONFIG="$PROJECT_ROOT"/envs/"$STAGE"/kubeconfig.yaml

eval $SETUP_PS1
