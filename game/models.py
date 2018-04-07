from django.db import models

# Create your models here.
class Level(models.Model):
    
    levelId = models.AutoField(primary_key=True)
    squares = models.IntegerField()
    positions = models.TextField()
    
