from django.db import models

from core.models import BaseModel


class Info(BaseModel):
    class Meta:
        db_table = 'info'

    title = models.CharField(max_length=100)
    content = models.TextField(max_length=255)
    url = models.URLField(max_length=60)
