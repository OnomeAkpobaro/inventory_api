from django.db import models
from django.contrib.auth import get_user_model
from Category.models import Category

User = get_user_model()

class Product(models.Model):
    name = models.CharField(max_length=10)
    description = models.TextField(max_length=50)
    quantity = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='products')
    created = models.DateField(auto_now=True)
    updated = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
    