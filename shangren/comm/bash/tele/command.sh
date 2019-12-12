# Args
# Directory where envs should be stored

printenv | sed '/^.*CUSTOM_PS1.*$/d' |
  sed '/^.*LS_COLORS.*$/d' |
  sed '/^.*LESSCLOSE.*$/d' |
  sed '/^.*PROMPT_COMMAND.*$/d' |
  sed '/^.*DIRENV.*$/d' |
  sed '/^.*PYTHONPATH.*$/d' |
  sed 's/^/export /' \
  > "$1"/.telepresence.sh &&
  printenv | sed '/^.*CUSTOM_PS1.*$/d' |
  sed '/^.*LS_COLORS.*$/d' |
  sed '/^.*PROMPT_COMMAND.*$/d' |
  sed '/^.*DIRENV.*$/d' |
  sed '/^.*PYTHONPATH.*$/d' |
  sed '/^.*LESSCLOSE.*$/d' \
  > "$1"/.telepresence.env \
 && tail -f /dev/null
