from django.db import models
from django.contrib.auth.models import User
from apps.common.models import BaseModel

class Order(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.TextField(null=True, blank=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.user