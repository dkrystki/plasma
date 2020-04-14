===============================================
Hmlet Photos - Take Home Project
===============================================

Design decisions
----------------
Devops is entirely handled in python and I used monorepo approach to
reuse as much code as possible.

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
    ├── hmlet[CLUSTER]/  # Take home project.
    │   ├── .bin/  # Miscellaneous executables. Added to the PATH env var when shell.py is activate.
    │   ├── .deps/  # External dependencies like kubectl or helm downloaded during bootstrap
    |   ├── comm[COMM]/   # Project wise common code
    │   ├── envs/  # Kubernetes config files for different environments.
    │   ├── doc/  # Documentation.
    │   ├── photos[APP]/  # Photos application.
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
    └── citygroves[CLUSTER]/  # Property management tool


Workflow
--------
Design of this monorepo and clusters (projects) is compliant with the 12-factor app concept.
Each stage or module is configured using environmental variables generated using python command
line utily :code:`"./shell.py {stage}"`
An example flow would be as follows:

.. code-block:: console

    user@pc:/plasma$ ./shell.py
    (pl)user@pc:/plasma$ pl.bootstrap
    (pl)user@pc:/plasma$ cd hmlet
    (pl)user@pc:/plasma/hmlet$ ./shell.py local  # activates local environment
    🐣(ht)user@pc:/plasma/hmlet$ ./cluster.py python bootstrap_local_dev  # install dependencies as helm or kubectl
    🐣(ht)user@pc:/plasma/hmlet$ ./cluster.py bootstrap  # bootstraps local kubernetes in docker (kind) cluster
    🐣(ht)user@pc:/plasma/hmlet$ ./cluster.py deploy  # deploy all apps
    🐣(ht)user@pc:/plasma/hmlet$ ./cluster.py add_hosts  # add hosts to /etc/hosts file
    🐣(ht)user@user:/plasma/hmlet$ cd photos
    🐣(ht)user@user:/plasma/hmlet/photos$ ./shell.py local
    🐣(ps)user@user:/plasma/hmlet/photos$ ./app.py skaffold

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


Requirements
############

Docker
