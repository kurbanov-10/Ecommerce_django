from django.db import models
from apps.common.models import BaseModel
from apps.products.models import Product

class Category(BaseModel):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    products = models.ManyToManyField(Product, related_name='categories')

    def __str__(self):
        return self.name