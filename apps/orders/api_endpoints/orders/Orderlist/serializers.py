from rest_framework import serializers
from apps.orders.models import Order

class OrderlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'