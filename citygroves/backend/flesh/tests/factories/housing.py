from datetime import datetime

import factory

from housing import models

import pytest_factoryboy


class UnitFactory(factory.Factory):
    class Meta:
        model = models.Unit

    number = 8


class RoomFactory(factory.Factory):
    class Meta:
        model = models.Room

    number = 5
    unit = factory.SubFactory(UnitFactory)


def register():
    pytest_factoryboy.register(UnitFactory)
    pytest_factoryboy.register(RoomFactory)
