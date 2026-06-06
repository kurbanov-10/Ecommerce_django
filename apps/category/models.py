from django.db import models
from apps.common.models import BaseModel


class Category(BaseModel):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    icon = models.ImageField(upload_to='images/category', null=True, blank=True)

    def __str__(self):
        return self.name