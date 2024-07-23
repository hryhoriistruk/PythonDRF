from django.db import models

from core.models import BaseModel


class VisitorModel(BaseModel):
    class Meta:
        db_table = 'visitors'
        ordering = ('id',)

    name = models.CharField(max_length=25)
    surname = models.CharField(max_length=25)
    email = models.EmailField()
    password = models.CharField(max_length=25)
    phone_number = models.CharField(max_length=15)
    # role
