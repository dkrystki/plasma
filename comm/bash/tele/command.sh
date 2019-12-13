# Args
# Directory where envs should be stored

cd "$APP_ROOT" || exit

printenv | sed '/^.*CUSTOM_PS1.*$/d' |
  sed '/^.*LS_COLORS.*$/d' |
  sed '/^.*LESSCLOSE.*$/d' |
  sed '/^.*PROMPT_COMMAND.*$/d' |
  sed '/^.*DIRENV.*$/d' |
  sed '/^.*PYTHONPATH.*$/d' |
  sed 's/^/export /' \
  > .telepresence.sh &&
  printenv | sed '/^.*CUSTOM_PS1.*$/d' |
  sed '/^.*LS_COLORS.*$/d' |
  sed '/^.*PROMPT_COMMAND.*$/d' |
  sed '/^.*DIRENV.*$/d' |
  sed '/^.*PYTHONPATH.*$/d' |
  sed '/^.*LESSCLOSE.*$/d' \
  > .telepresence.env \
 && tail -f /dev/null
