#!/usr/bin/python
import os
script_dir = os.path.dirname(os.path.realpath(__file__))

profile = "local"

os.system("TSOCKS_CONF_FILE={0}/tsocks.conf tsocks firefox -no-remote -P {1}".format(script_dir, profile))
