from django.db import models


class EngineTypesChoices(models.TextChoices):
    gasoline = "gasoline",
    gas = "gas",
    diesel = "diesel"
    hybrid_HEV = "hybrid HEV",
    hybrid_PHEV= "hybrid PHEV",
    electro = "electro"
    propane_butane_gas = "propane_butane_gas",
    methane_gas_gasoline = "methane_gas_gasoline"
