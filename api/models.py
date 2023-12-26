from django.db import models

class Exercise(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)
    description = models.TextField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=25, blank=True, null=True)
    muscle_group = models.CharField(max_length=30, blank=True, null=True)
    equipment = models.CharField(max_length=15, blank=True, null=True)
    level = models.CharField(max_length=15, blank=True, null=True)
    image1 = models.CharField(max_length=500, null=True, blank=True)
    image2 = models.CharField(max_length=500, null=True, blank=True)
    image3 = models.CharField(max_length=500, null=True, blank=True)
    image4 = models.CharField(max_length=500, null=True, blank=True)

    class Meta:
        ordering = ["muscle_group"]

    def get_all_exercises():
        return Exercise.objects.all()        
