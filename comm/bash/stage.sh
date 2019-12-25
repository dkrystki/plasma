if [ "$0" = "$BASH_SOURCE" ]; then
    echo "Error: Script must be sourced"
    exit 1
fi

case $1 in
    local|stage|prod) ;;
    *) printf "Must be \"stage\" \"local\" or \"prod\"\n"
      exit 1 ;;
esac

echo "export STAGE="$1"" > "$PROJECT_ROOT"/.current_stage

source "$PLASMA_COMM_ROOT/bash/setup_stage.sh"
