FROM python:3.8.0b1-slim-stretch

ENV DEBIAN_FRONTEND noninteractive
ENV LC_ALL C.UTF-8
ENV LANG C.UTF-8
ENV SHELL /bin/bash


# Install common
RUN apt update && apt install net-tools -y && pip3 install pipenv

WORKDIR /srv

# PipEnv
ENV PIPENV_VENV_IN_PROJECT true

# Setup data provider
COPY flesh .

RUN pipenv install

# Setup motd
COPY docker/motd/motd /etc/motd
COPY docker/motd/.bashrc /root/.bashrc
