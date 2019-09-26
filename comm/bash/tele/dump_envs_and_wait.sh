export -p | sed '/^.*PROMPT_COMMAND.*$/d' > "$1"/telepresence.dec \
 && printenv > "$1"/telepresence.env \
 && tail -f /dev/null
