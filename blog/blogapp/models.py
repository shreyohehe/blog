from django.db import models
from datetime import datetime
class Posts(models.Model):
    title= models.CharField(max_length=100)
    details=models.CharField(max_length=1000000)
    date=models.DateTimeField(default= datetime.now, blank=True)

# Create your models here.
