# This script activates telepresence and activates pipenv
# source this script before doing any debugging with telepresence
# Run telepresence.sh first

test -f "$PROJECT_DIR"/telepresence.sh && source "$PROJECT_DIR"/telepresence.sh
