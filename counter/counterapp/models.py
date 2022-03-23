from django.db import models


# Create your models here.
class CounterModel(models.Model):
    number = models.CharField(max_length=10);
