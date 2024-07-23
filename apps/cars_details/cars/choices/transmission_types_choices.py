from django.db import models


class TransmissionTypeChoices(models.TextChoices):
    mechanics = "mechanics",
    automatic = "automatic",
    tiptronic="tiptronic",
    robot = "robot",
    variator = "variator"