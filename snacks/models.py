from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth import get_user_model

# Create your models here.
class Snack(models.Model):
    name = models.CharField(max_length=64)
    purchaser = models.ForeignKey(get_user_model(),on_delete=CASCADE)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name