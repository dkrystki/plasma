
printenv | sed '/^.*CUSTOM_PS1.*$/d' |
  sed '/^.*LS_COLORS.*$/d' |
  sed '/^.*LESSCLOSE.*$/d' |
  sed 's/^/export /' \
  > "$1"/telepresence.sh &&
  printenv | sed '/^.*CUSTOM_PS1.*$/d' |
  sed '/^.*LS_COLORS.*$/d' |
  sed '/^.*LESSCLOSE.*$/d' \
  > "$1"/telepresence.env \
 && tail -f /dev/null
