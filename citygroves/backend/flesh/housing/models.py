from django.db import models


class Unit(models.Model):
    number = models.IntegerField(unique=True)

    def __str__(self):
        return f"{self.number}"


class Room(models.Model):
    number = models.IntegerField()
    unit: Unit = models.ForeignKey(Unit, on_delete=models.CASCADE)

    def __str__(self):
        return f"U{self.unit.number}R{self.number}"
