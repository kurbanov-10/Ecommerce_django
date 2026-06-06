from django.db import models
from django.contrib.auth.models import User
from apps.common.models import BaseModel
from apps.products.models import Product

class Order(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.TextField(null=True, blank=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f"Order {self.id}  {self.user.username}"
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"OrderItem {self.id} - Order {self.order.id} - Product {self.product.name}"
    
    def save(self, *args, **kwargs):
        if not self.price:
            self.price = self.product.price
        super().save(*args, **kwargs)