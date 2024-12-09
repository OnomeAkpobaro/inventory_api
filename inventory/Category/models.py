from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.
CATEGORIES = (
    ("category A", "category A"),
    ("category B", "category B"),
    ("category C", "category C"),
    ...

)

class Category(models.Model):
    name = models.CharField(choices=CATEGORIES,unique=True)

    def __str__(self):
        return self.name
    

