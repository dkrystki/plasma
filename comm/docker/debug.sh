#!/usr/bin/env bash

set -euo pipefail

apt-get update && apt-get install -y iputils-ping

# uncomment aliases and colors
echo 'force_color_prompt=yes' >> /root/.bashrc
echo "alias ll='ls -la'" >> /root/.bashrc
echo "alias la='ls -A'" >> /root/.bashrc
echo "alias ls='ls --color=auto'" >> /root/.bashrc

echo "cd /srv" >> /root/.bashrc
echo "PS1='\[\033[1;36m\]\u\[\033[1;31m\]@\[\033[1;32m\]\h:\[\033[1;35m\]\w\[\033[1;31m\]\$\[\033[0m\] '" >> /root/.bashrc

echo "echo -e \"`cat /tmp/docker/motd/motd`\"" >> /root/.bashrc
