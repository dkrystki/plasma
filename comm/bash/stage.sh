if [ "$0" = "$BASH_SOURCE" ]; then
    echo "Error: Script must be sourced"
    exit 1
fi

case $1 in
    test|local|stage|prod) ;;
    *) printf "Must be  \"test\" \"local\" \"stage\" or \"prod\"\n"
      return
esac

echo "export STAGE="$1"" > "$PROJECT_ROOT"/.current_stage

source "$PLASMA_COMM_ROOT/bash/setup_stage.sh"
