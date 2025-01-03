from django.db import models

# Create your models here.
class users(models.Model):
    username = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    password = models.CharField(max_length=128)
    age = models.PositiveIntegerField()
    
    def __str__(self):
        return self.username