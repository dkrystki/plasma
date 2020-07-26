===============================================
Citygroves - Property management tool
===============================================

prerequisites
-------------
Docker has to be installed and added to sudo group so it can be run without root privileges.


Set up
-----------
1) Bootstrap monorepo

.. code-block:: console

    git clone https://github.com/dkrystki/plasma.git
    cd plasma
    sudo apt install python3-pip
    ./bootstrap

2) Install dependencies

.. code-block:: console

    cd citygroves
    ./shell.py
    ./cluster.py install_deps

3) Edit docker's daemon.json file and add following line to it:

.. code-block:: console

    "insecure-registries" : ["citygroves.registry.local"]


restart docker daemon

4) Bootstrap

.. code-block:: console

    ./cluster.py bootstrap

5) Deploy

.. code-block:: console

    ./cluster.py deploy

6) go to:

.. code-block:: console

    http://citygroves.frontend.local


7) log in:

.. code-block:: console

    login: test@test.pl
    password: password
