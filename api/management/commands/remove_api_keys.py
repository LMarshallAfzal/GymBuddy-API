from django.core.management.base import BaseCommand
from rest_framework_api_key.models import APIKey

class Command(BaseCommand):
    help = 'Deletes all API keys'

    def handle(self, *args, **options):
        count, _ = APIKey.objects.all().delete()
        self.stdout.write(self.style.SUCCESS(f'Deleted {count} API keys'))
