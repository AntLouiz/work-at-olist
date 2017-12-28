import os
from io import StringIO
from django.core.management import call_command
from django.core.management.base import CommandError
from django.test import TestCase
from channels.models import Channel, Category


class TestImportCategoriesCommand(TestCase):

    def setUp(self):
        self.filename = 'books_categories.txt'
        with open(self.filename, 'w') as file:
            file.write("Books\n")
            file.write("Books / National Literature\n")
            file.write("Books / National Literature / Science Fiction\n")
            file.write("Books / Computers\n")

    def tearDown(self):
        os.remove(self.filename)

    def test_command_output(self):
        out = StringIO()
        call_command('importcategories', 'Books', self.filename, stdout=out)
        self.assertIn(
            'The file data was successfully imported',
            out.getvalue()
        )

    def test_command_error(self):
        out = StringIO()

        with self.assertRaises(CommandError):
            call_command(
                'importcategories',
                'books',
                self.filename,
                stdout=out
            )

        with self.assertRaises(CommandError):
            call_command(
                'importcategories',
                'Books',
                'file.txt',
                stdout=out
            )

    def test_command_result_data(self):
        call_command('importcategories', 'Books', self.filename)

        channel = Channel.objects.all()
        categories = Category.objects.all()

        self.assertEquals(1, channel.count())
        self.assertEquals(3, categories.count())

        self.assertEquals(True, channel.filter(name='Books').exists())
        self.assertEquals(
            True,
            categories.filter(name='National Literature').exists()
        )
        self.assertEquals(
            True,
            categories.filter(name='Science Fiction').exists()
        )
