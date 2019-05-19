FROM python3.7

#ENV DEBIAN_FRONTEND noninteractive
#
## set default java environment variable
#ENV JAVA_VERSION_MAJOR=8 \
#    JAVA_HOME=/usr/lib/jvm/default-jvm \
#    PATH=${PATH}:/usr/lib/jvm/default-jvm/bin/
#
## Setup motd
#COPY docker/motd/motd /etc/motd
#COPY docker/motd/.bashrc /root/.bashrc
#
## Install common
#RUN apt update && apt install wget python3-pip net-tools -y && pip3 install pipenv
#
## Install JDK
#RUN apt-get install -y --no-install-recommends openjdk-8-jre
#RUN ln -s java-8-openjdk-amd64 /usr/lib/jvm/default-jvm
#RUN apt-get clean all
#
## Create directories
#RUN mkdir /app
#
#ENV LC_ALL C.UTF-8
#ENV LANG C.UTF-8
#ENV SHELL /bin/bash
#ENV PIPENV_VENV_IN_PROJECT true
#
### Install redis
##RUN groupadd -r redis && useradd -r -g redis redis
##
##RUN mkdir /app/redis
##RUN mkdir /app/redis/logs
##RUN mkdir /app/redis/conf
##RUN chown redis:redis -R /app/redis
#
##RUN apt install redis-server -y
##COPY docker/redis/redis.conf /app/redis/conf/redis.conf
## End of install redis
#
## Setup zookeeper
#RUN mkdir /app/zookeeper
#RUN mkdir /app/zookeeper/logs
#COPY docker/zookeeper/zoo.cfg /app/zookeeper/zoo.cfg
#RUN apt install default-jre zookeeperd -y
#
## Install kafka
#RUN mkdir /app/kafka
#RUN mkdir /app/kafka/logs
#RUN useradd -m kafka
#WORKDIR /app/kafka/device
#RUN wget http://www-us.apache.org/dist/kafka/1.1.0/kafka_2.12-1.1.0.tgz
#RUN tar xzf kafka_2.12-1.1.0.tgz -C .
#RUN cp -a kafka_2.12-1.1.0/. .
#RUN rm -f kafka_2.12-1.1.0.tgz
#RUN rm -r kafka_2.12-1.1.0
#COPY docker/kafka/server.properties /app/kafka/server.properties
#
## Setup supervisord
#RUN apt install supervisor -y
#RUN mkdir -p /app/supervisor/logs
#COPY docker/supervisor/supervisord.conf /app/supervisor/supervisord.conf
#
## Setup volumes
#RUN mkdir /app/data
#RUN mkdir /app/data/data_prov
#RUN mkdir /app/data/redis
#RUN mkdir /app/data/kafka
#
## Logstash
#RUN mkdir /app/logstash/
#RUN mkdir /app/logstash/logs
#RUN cd /app/logstash/
#RUN wget -qO - https://artifacts.elastic.co/GPG-KEY-elasticsearch | apt-key add -
#RUN apt install apt-transport-https
#RUN echo "deb https://artifacts.elastic.co/packages/6.x/apt stable main" | tee -a /etc/apt/sources.list.d/elastic-6.x.list
#RUN apt update && apt install logstash
#COPY docker/logstash/logstash.config /app/logstash/logstash.config
#RUN /usr/share/logstash/bin/logstash-plugin install logstash-output-gelf
## grok patterns
#RUN mkdir /app/logstash/patterns
#COPY docker/logstash/patterns /app/logstash/patterns
#
## Setup influxdb
#RUN mkdir /app/influx
#RUN mkdir /app/influx/logs
#COPY docker/influxdb/influxdb.conf /app/influx/influxdb.conf
#ENV INFLUXDB_VERSION 1.5.4
#RUN	wget -nv https://dl.influxdata.com/influxdb/releases/influxdb_${INFLUXDB_VERSION}_amd64.deb && \
#			dpkg -i influxdb_${INFLUXDB_VERSION}_amd64.deb && rm influxdb_${INFLUXDB_VERSION}_amd64.deb
#
## Setup pipenv
#RUN mkdir /app/dataprov
#WORKDIR /app/dataprov
#COPY docker/pipenv/Pipfile Pipfile
#COPY docker/pipenv/Pipfile.lock Pipfile.lock
#RUN pipenv install
#
## Setup data provider
#RUN mkdir /app/utils
#RUN useradd -m dataprov
#RUN mkdir /app/dataprov/logs
#COPY django_proj /app/dataprov
#COPY docker/dataprov/start.sh /app/utils/start_dataprov.sh
#RUN chown dataprov:dataprov -R /app/dataprov
#COPY docker/motd/.bashrc /home/dataprov/.bashrc
#
## Setup ssh
#RUN mkdir /app/sshd/
#RUN mkdir /app/sshd/logs
#RUN apt install openssh-server -y
#RUN mkdir /var/run/sshd
#RUN echo 'root:dfbj35nbsacv465' | chpasswd
#COPY /docker/sshd/sshd_config /etc/ssh/sshd_config
## SSH login fix. Otherwise user is kicked off after login
#RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd
#ENV NOTVISIBLE "in users profile"
#RUN echo "export VISIBLE=now" >> /etc/profile
#EXPOSE 22
#EXPOSE 80
