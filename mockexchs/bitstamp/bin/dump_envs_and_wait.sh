export -p | sed '/^.*PROMPT_COMMAND.*$/d' > telepresence.dec && printenv > telepresence.env  && tail -f /dev/null
