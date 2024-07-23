from django.db import models


class CurrencyChoices(models.TextChoices):
    USD = "USD",
    EUR = "EUR",
    UAH = "UAH"
