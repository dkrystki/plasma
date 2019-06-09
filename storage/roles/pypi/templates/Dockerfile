FROM ubuntu:18.04

RUN apt update && apt install python-pip -y
RUN pip install -U passlib pypiserver[cache]==1.2.1

RUN mkdir -p /srv/pypi/packages
RUN mkdir -p /srv/pypi/passwords

# Setup motd
COPY docker /etc/motd
COPY docker /root/.bashrc

WORKDIR /app/