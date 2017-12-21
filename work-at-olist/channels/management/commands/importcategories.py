import os
from django.core.management.base import BaseCommand, CommandError
from channels.models import Channel


class Command(BaseCommand):
    help = 'Import the channels categories from a text file.'

    def add_arguments(self, parser):
        parser.add_argument('channel', nargs=1)
        parser.add_argument('filename', nargs=1)

    def get_file_line(self, *args, **options):
        filename = options['filename'][0]

        if not os.path.isfile(filename):
            raise CommandError("File not found.")

        with open(filename, 'r') as file:
            for line in file.readlines():
                line = [word.strip() for word in line.split('/')]
                yield line

    def get_categories(self, *args, **options):

        channel_desc = options['channel'][0]
        for categories in self.get_file_line(*args, **options):
            channel = categories[0]

            """
            if the channel inside the file is
            not the same of the argument, raise a Exception.
            """
            if channel != channel_desc:
                raise Exception(
                    "The channel inside the file\
                    is different from the argument."
                )

            try:
                category = {'channel': channel}

                if categories[-2] != channel:
                    category['parent_category'] = categories[-2]
                else:
                    category['parent_category'] = None

                category['category'] = categories[-1]

                yield category

            except:
                pass

    def handle(self, *args, **options):
        print("Trying to import the categories...")

        channel_desc = options['channel'][0]

        #checking if the channel inside the file is the same of the argument.
        for line in self.get_file_line(*args, **options):
            if line[0] != channel_desc:
                raise Exception(
                    "The channel inside the file is different from the argument."
                )

            channel_obj = Channel.objects.get_or_create(name=channel_desc)

        categories = self.get_categories(*args, **options)
        for cat in categories:
            print(cat)