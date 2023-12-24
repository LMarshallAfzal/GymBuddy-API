from django.core.management.base import BaseCommand
from django.db import transaction
from tqdm import tqdm
from api.models import Exercise, Image

class Command(BaseCommand):
    help = 'Removes all exercise data from the database'

    def handle(self, *args, **options):
        total_exercises = Exercise.objects.count()
        with transaction.atomic():
            with tqdm(total=total_exercises, desc='Unseeding Exercises') as pbar:
                exercises = Exercise.objects.all().iterator()
                for exercise in exercises:
                    exercise.delete()  # Delete exercise instances directly
                    pbar.update()  # Update progress bar for each exercise

            Image.objects.all().delete()

        self.stdout.write(self.style.SUCCESS('Database unseeded successfully!'))
