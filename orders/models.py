from django.db import models
from food.models import FoodItem

class Order(models.Model):
    customer_name = models.CharField(max_length=100)
    food_item = models.ForeignKey(FoodItem, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    address = models.TextField()
    order_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.customer_name