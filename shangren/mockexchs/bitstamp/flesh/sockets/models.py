from django.db import models


class Client(models.Model):
    channel = models.CharField(max_length=127)

