import os
from django.core.management.base import BaseCommand, CommandError
from channels.models import Channel, Category


class Command(BaseCommand):
    help = 'Import the channels categories from a text file.'

    def add_arguments(self, parser):
        parser.add_argument('channel', nargs=1)
        parser.add_argument('filename', nargs=1)

    def get_file_line(self, *args, **options):
        filename = options['filename'][0]

        if not os.path.isfile(filename):
            raise CommandError("File not found.")

        self.stdout.write("Importing the categories...")
        with open(filename, 'r') as file:
            for line in file.readlines():
                line = [word.strip() for word in line.split('/')]
                yield line

    def get_channel(self, *args, **options):
        channel_object, _ = Channel.objects.get_or_create(
            name=options['channel'][0]
        )
        self.stdout.write(
            "Channel {} {}".format(
                channel_object.name,
                self.style.SUCCESS('imported successfully.')
            )
        )
        return channel_object

    def get_categories(self, *args, **options):
        channel_object = self.get_channel(*args, **options)

        if channel_object.category_set.exists():
            channel_object.category_set.all().delete()

        for categories in self.get_file_line(*args, **options):
            channel = categories[0]

            """
            if the channel inside the file is
            not the same of the argument, raise a Exception.
            """
            if channel != channel_object.name:
                channel_object.delete()
                raise CommandError(
                    "The channel inside the file "
                    "is different from the argument."
                )

            try:
                category = {'channel': channel_object}

                if categories[-2] != channel:
                    category['parent_category'] = categories[-2]
                else:
                    category['parent_category'] = None

                category['name'] = categories[-1]

                yield category

            except IndexError:
                pass

    def create_categories(self, *args, **options):

        categories = self.get_categories(*args, **options)
        for category in categories:
            name = category['name']
            channel = category['channel']

            if category['parent_category']:
                category['parent_category'] = Category.objects.get(
                    name=category['parent_category'],
                    channel=channel
                )

            Category.objects.get_or_create(
                name=name,
                channel=channel,
                parent_category=category['parent_category']
            )
            self.stdout.write(
                "\t{} {}".format(
                    category['name'],
                    self.style.SUCCESS('imported.')
                )
            )

    def handle(self, *args, **options):
        self.create_categories(*args, **options)
        self.stdout.write(
            self.style.SUCCESS('The file data was successfully imported.')
        )
