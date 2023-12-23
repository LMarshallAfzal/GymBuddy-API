from django.db import models

class Exercise(models.Model):
    name = models.CharField(max_length=255, blank=False)
    description = models.TextField()
    type = models.CharField(max_length=25)
    muscle_group = models.CharField(max_length=30)
    equipment = models.CharField(max_length=15)
    level = models.CharField(max_length=15)

class Image(models.Model):
    url = models.CharField(max_length=500)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)

