from django.db import models

# Create your models here.
class UniqueCode(models.Model):
    uniqueCode   = models.IntegerField()
    sender       = models.CharField(max_length=100)
    receiver     = models.CharField(max_length=100,null=True)
