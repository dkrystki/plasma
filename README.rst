===============================================
Shangren - Cryptocurrency auto trading platform
===============================================

Shangren (Shāngrén) stands for chinese 商人 which means trader. It's a side project of mine that I'm currently working on.
Shangren fetches live cryptocurrency data that is used to predict cryptocurrency prices and to make good trade decisions with a little supervision.
Data is being saved for further analysis and backtesting which helps refine AI overtime and could make the ultimate passive income solution in the future.


Development
-----------
Shangren uses docker to create an isolated development environment so your system is not being polluted.

Requirements
############
In order to run local development you have to have Docker and Docker Compose installed.
telepresence
minikube

Starting things up
##################
.. code-block:: console

    docker-compose up -d

Logging into microservices
################################
.. code-block:: console

    ./bin/terminal

The code is synchronised between a docker container and the host using volumes so any changes ( ``pipenv install`` etc ) will be affected on the host.
