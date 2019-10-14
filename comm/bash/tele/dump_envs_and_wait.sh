
ENVS_DIR=$1

function cleanup {
  rm "$ENVS_DIR"/telepresence.env
  rm "$ENVS_DIR"/telepresence.sh
}

trap cleanup EXIT

printenv | sed '/^.*CUSTOM_PS1.*$/d' |
  sed '/^.*LS_COLORS.*$/d' |
  sed '/^.*LESSCLOSE.*$/d' |
  sed 's/^/export /' \
  > "$ENVS_DIR"/telepresence.sh &&
  printenv | sed '/^.*CUSTOM_PS1.*$/d' |
  sed '/^.*LS_COLORS.*$/d' |
  sed '/^.*LESSCLOSE.*$/d' \
  > "$ENVS_DIR"/telepresence.env \
 && tail -f /dev/null
