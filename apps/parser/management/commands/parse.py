from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Run parser'

    def handle(self, *args, **options):
        print("Parser started")
