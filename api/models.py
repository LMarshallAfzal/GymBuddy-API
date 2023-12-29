from django.db import models

class Exercise(models.Model):
    """
    Model representing an exercise.

    Fields:
    - name (CharField): The name of the exercise.
    - description (TextField): A description of the exercise.
    - type (CharField): The type of exercise (e.g., strength, cardio, flexibility).
    - muscle_group (CharField): The primary muscle group targeted by the exercise.
    - equipment (CharField): Any equipment required for the exercise.
    - level (CharField): The difficulty level of the exercise (e.g., beginner, intermediate, advanced).
    - image1 (CharField): URL for the first image of the exercise.
    - image2 (CharField): URL for the second image of the exercise.
    - image3 (CharField): URL for the third image of the exercise.
    - image4 (CharField): URL for the fourth image of the exercise.
    """

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
        """
        Retrieves all exercise objects from the database.

        Returns:
        - QuerySet: A QuerySet containing all exercise objects.
        """
        return Exercise.objects.all()        
