from django.core.management.base import BaseCommand, CommandError
from rest_framework_api_key.models import APIKey

class Command(BaseCommand):
    help = 'Creates a new API key'

    def add_arguments(self, parser):
        parser.add_argument('name', type=str, help='The name for the API key')

    def handle(self, *args, **options):
        try:
            key = APIKey.objects.create(name=options['name'])
            try:  # Attempt to access key in a modern way
                key_value = key.key.decode('utf-8')
                print(key.key)
            except AttributeError:  # Fallback for older versions
                key_value = key.prefix + key.hashed_key
                print(key.hashed_key)
            self.stdout.write(self.style.SUCCESS(f'API key created successfully: {key_value}'))
        except Exception as e:
            raise CommandError(f'Error creating API key: {e}')
