from django.db import models

class FoodItem(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    category = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to="food_images/", blank=True, null=True)

    def __str__(self):
        return self.name