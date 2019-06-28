FROM python:3.7

ENV DEBIAN_FRONTEND noninteractive
ENV LC_ALL C.UTF-8
ENV LANG C.UTF-8
ENV SHELL /bin/bash


# Install common
RUN apt update && apt install net-tools -y && pip3 install pipenv

# Setup motd
COPY docker/motd/motd /etc/motd
COPY docker/motd/.bashrc /root/.bashrc

# uid is set to 1000 for development purposes
RUN useradd -ms /bin/bash -u 1000 lib
COPY docker/motd/.bashrc /home/lib/.bashrc

RUN chown -R lib:lib /srv
WORKDIR /srv

# Setup data provider
COPY --chown=lib:lib . .
USER lib

# PipEnv
ENV PIPENV_VENV_IN_PROJECT true
RUN pipenv install
RUN pipenv run python setup.py clean
