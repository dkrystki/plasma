#!.venv/bin/python
import os
import django

import environ
import fire
from loguru import logger

environ = environ.Env()

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "photos.settings")

django.setup()


from django.contrib.auth.models import User  # noqa: E402


class Cli:
    def __init__(self):
        pass

    def create_test_user(self, username: str, password: str):
        # TODO: disable this on prod
        if User.objects.filter(username=username).exists():
            logger.info(f'Test username "{username}" already exists.')
            return

        User.objects.create_user(username=username, password=password)
        logger.info(f'Created test user with username "{username}"')

    def create_super_user(self, username: str, password: str):
        # TODO: disable this on prod
        if User.objects.filter(username=username).exists():
            logger.info(f'Username "{username}" already exists.')
            return

        User.objects.create_superuser(username=username, password=password)
        logger.info(f'Created super user with username "{username}"')


if __name__ == "__main__":
    fire.Fire(Cli())
