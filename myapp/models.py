from django.db import models
from django.utils import timezone
class Farmer(models.Model):
    Name=models.CharField(max_length=30,unique=True)
    Email=models.EmailField(unique=True)
    Mnumber=models.IntegerField()
class opinion(models.Model):
    op=models.CharField(max_length=60)
    created_at = models.DateTimeField(default=timezone.now)
def __str__(self):
    return self.Name
# Create your models here.

