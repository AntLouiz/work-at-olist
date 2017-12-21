from django.core.management.base import BaseCommand, CommandError
from channels.models import Channel, Category


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def add_arguments(self, parser):
        parser.add_argument('channel', nargs=1)
        parser.add_argument('filename', nargs=1)

    def handle(self, *args, **options):
        channel = options['channel'][0]
        filename = options['filename'][0]

        print(channel)
        print(filename)