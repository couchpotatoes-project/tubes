from django.db import models

# Create your models here.
class Level(models.Model):
    id= models.AutoField(primary_key=True)
    levelId = models.IntegerField()
    squares = models.IntegerField()
    positions = models.TextField()
	
class UserScore(models.Model):
	id= models.AutoField(primary_key=True)
	username = models.TextField()
	levelId = models.IntegerField()
	moves = models.IntegerField()
	time = models.TextField()