===============================================
Plasma - Personal Monorepo
===============================================

Disclaimer
----------
This project is work in progress, some things might be rough around the edges and I am continually refactoring
and improving things.

This repo is also a testing ground for my another project - Pangea Kubernetes infrastructure
as python code framework which makes developing Kubernetes applications easy,
reducing a lot of devops boilerplate and delivering production ready environment out of the box.

What is the monorepo?
---------------------
Monorepo is a software engineering strategy where code for many project
are stored in a single repository.

Why did I chose this strategy?
--------------------------------
I have learned in my engineering practice to follow "KISS principle" (keep it stupid simple).
Monorepo approach ticks almost all the boxes when it comes to simplicity and productivity.
I have worked in projects that used monorepo and splits repo approach and learned that overhead of managing split repos
is something that I want to avoid.

Folder structure
################
Monorepo does not mean the code is a monolith in fact it still should be modular.

::

    plasma[MONOREPO]/
    ├── comm[COMM]/   # Monorepo wise common code.
    │   ├── bash/  # Bash scripts.
    │   ├── python/  # Python libraries and helpers.
    │   ├── bin/  # Common binaries.
    │   └── docker/  # Common Dockerfiles, dockers scripts.
    ├── citygroves[CLUSTER]/  # Property management website.
    │   ├── .bin/  # Miscellaneous executables. Added to the PATH env var when shell.py is activate.
    │   ├── .deps/  # External dependencies like kubectl or helm downloaded during bootstrap
    |   ├── comm/   # Project wise common code
    |   ├── comm[COMM]/   # Project wise common code
    │   ├── envs/  # Kubernetes config files for different environments.
    │   ├── doc/  # Documentation.
    │   ├── backend[APP]/  # Application (microservice).
    │   |   ├── .bin/ # Miscellaneous executables. Added to the PATH env var in .evnrc shell script.
    |   |   ├── flesh/ # Source code. This is what goes into a docker container.
    |   |   ├── chart/ # Kubernetes helm chart.
    |   |   ├── values/ # Kubernetes values files for all the stages.
    |   |   |   ├── test/
    |   |   |   |   ├── postgresql.yaml
    |   |   |   |   ├── redis.yaml
    |   |   |   |   └── backend.yaml
    |   |   |   ├── local/
    |   |   |   ├── stage/
    |   |   |   └── prod/
    |   |   ├── app.py  # Command line utility that implements app wise devops functions like deployment
    |   |   └── shell.py  # Spawns a shell with prepared environmental variables and settings for a given stage
    |   ├── frontend[APP]/  # Application (microservice).
    |   ├── env_comm.py  # common environment settings
    |   ├── env_local.py  # local environment settings subclasses from common ones
    |   ├── env_stage.py  # staging environment settings subclasses from common ones
    |   ├── cluster.py  # Command line utility that implements cluster wise devops functions like deployment
    |   └── shell.py  # Spawns a shell with prepared environmental variables and settings for a given stage
    └── shangren[CLUSTER]/  # Cryptocurrency auto trading bot.


Workflow
--------
Design of this monorepo is compliant with the 12-factor app concept.
Each stage or module is configured using environmental variables generated using python command
line utily :code:`"./shell.py {stage}"`
An example flow would be as follows:

.. code-block:: console

    user@user:/plasma$ ./shell.py
    (pl)user@pc:/plasma$ pl.bootstrap
    (pl)user@pc:/plasma$ cd citygroves  # property management tool project
    (pl)user@pc:/plasma/citygroves$ ./shell.py local  # activates local environment
    🐣(cg)user@pc:/plasma/citygroves$ ./cluster.py bootstrap_local_dev  # install dependencies as helm or kubectl
    🐣(cg)user@pc:/plasma/citygroves$ ./cluster.py bootstrap  # bootstraps local kubernetes in docker (kind) cluster
    🐣(cg)user@pc:/plasma/citygroves$ ./cluster.py deploy  # deploy all apps
    🐣(cg)user@pc:/plasma/citygroves$ ./cluster.py add_hosts  # add hosts to /etc/hosts file
    🐣(cg)user@user:/plasma/citygroves$ curl add_hosts  # add hosts to /etc/hosts file
    🐣(cg)user@user:/plasma/citygroves$ cd backend
    🐣(cg)user@user:/plasma/citygroves$ ./shell.py local
    🐣(be)user@user:/plasma/citygroves$ ./app.py skaffold

Stages
######
Current stage can be changed using :code:`"./shell.py {stage}"`. This will change kubernetes context and
environmental variables to according cluster.
Environments are configured in env_*.py files and available from python code as a regular package or
environmental variables
All of the comands will be run against this stage. For example. Running :code:`{app_code}.terminal` command will open a
terminal to a pod for the current stage.
Current stage is indicated by emoji in the shell prompt.

::

    🛠️ test
    🐣 local
    🤖 staging
    🔥 productions

TODO
----

* Add tests to frontend
* Add more tests to devops packages
