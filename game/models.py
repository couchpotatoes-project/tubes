from django.db import models

# Create your models here.
class Level(models.Model):
    id= models.AutoField(primary_key=True)
    levelId = models.IntegerField()
    squares = models.IntegerField()
    positions = models.TextField()