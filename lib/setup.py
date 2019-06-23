from setuptools import find_packages, setup

setup(
    name='shengren',
    version='0.1.0',
    packages=['shengren'],
    description='Library for functionality shared between Shengren microservices',
    install_requires=['requests', 'furl'
    ],
)
