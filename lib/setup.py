from pathlib import Path

import os
from setuptools import setup, Command

version = {}
exec(Path("shengren/__version__.py").read_text(), version)


class CleanCommand(Command):
    """Custom clean command to tidy up the project root."""
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        os.system('rm -vrf ./build ./dist ./*.pyc ./*.tgz ./*.egg-info')


setup(
    name='shengren',
    version=version['__version__'],
    packages=['shengren'],
    description='Library for functionality shared between Shengren microservices',
    install_requires=['requests', 'furl'
    ],
    cmdclass={
        'clean': CleanCommand,
    }
)