from django.db import models


class RolesChoices(models.TextChoices):
    Admin = "admin",
    Manager = "manager",
    Visitor = "visitor",
    Owner = "owner"
    # Seller = "seller",
    # Premium_seller = "premium_seller",
    Partners_admin = "partners_admin"
    Partners_manager = "partners_manager"
    Partners_mechanic = "partners_mechanic"
    Partners_sales = "partners_sales"
