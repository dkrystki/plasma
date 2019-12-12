#!/usr/bin/env bash

set -euo pipefail

apt-get update && apt-get install -y iputils-ping

#addgroup --gid 1000 "$1"
#adduser --disabled-password --disabled-login --gecos "" --uid 1000 --gid 1000 "$1"
#echo "su "$1"" >> /root/.bashrc

#usermod -aG sudo "$1"

# uncomment aliases and colors
echo 'force_color_prompt=yes' >> /root/.bashrc
echo "alias ll='ls -la'" >> /root/.bashrc
echo "alias la='ls -A'" >> /root/.bashrc
echo "alias ls='ls --color=auto'" >> /root/.bashrc

echo "cd /srv" >> /root/.bashrc
echo "PS1='\[\033[1;36m\]\u\[\033[1;31m\]@\[\033[1;32m\]\h:\[\033[1;35m\]\w\[\033[1;31m\]\$\[\033[0m\] '" >> /root/.bashrc

echo "echo -e \"`cat ./docker/motd/motd`\"" >> /root/.bashrc

#mkdir -p /home/"$1"/.ssh
#echo "Host *" > /home/"$1"/.ssh/config
#echo " StrictHostKeyChecking no" >> /home/"$1"/.ssh/config

#cp docker_comm/supervisor/supervisord.conf /etc/supervisor/conf.d/supervisord.conf
