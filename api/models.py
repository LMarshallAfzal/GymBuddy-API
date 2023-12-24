from django.db import models

class Exercise(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)
    description = models.TextField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=25, blank=True, null=True)
    muscle_group = models.CharField(max_length=30, blank=True, null=True)
    equipment = models.CharField(max_length=15, blank=True, null=True)
    level = models.CharField(max_length=15, blank=True, null=True)

class Image(models.Model):
    url = models.CharField(max_length=500)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)

