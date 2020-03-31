FROM ubuntu:18.04

RUN mkdir /srv/plasma
WORKDIR /srv/plasma

RUN apt update
RUN apt install python3 git python3-pip sudo -y

COPY . /srv/plasma

CMD ["tail", "-f", "/dev/null"]
