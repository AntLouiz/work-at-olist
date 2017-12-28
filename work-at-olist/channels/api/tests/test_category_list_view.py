from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from channels.models import Channel, Category


class TestCategoryListView(APITestCase):

    def setUp(self):
        channel = Channel.objects.create(
            name='Books'
        )

        parent_category = Category.objects.create(
            name='National Literature',
            channel=channel
        )

        Category.objects.create(
            name='Science fiction',
            parent_category=parent_category,
            channel=channel
        )

        Category.objects.create(
            name='Foreign literature',
            channel=channel
        )

        self.url = reverse('list-category')

    def test_get_response(self):

        response = self.client.get(self.url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_get_data_response(self):

        response = self.client.get(self.url)
        category_name = response.data[0]['name']
        category_categories = response.data[0]['categories']
        category_parent_category = response.data[0]['parent_category']
        category_channel = response.data[0]['channel']

        self.assertEquals('Foreign literature', category_name)
        self.assertEquals('Books', category_channel)
        self.assertEquals(None, category_parent_category)
        self.assertEquals(0, len(category_categories))

        category_name = response.data[1]['name']
        category_categories = response.data[1]['categories']
        category_parent_category = response.data[1]['parent_category']
        category_channel = response.data[1]['channel']

        self.assertEquals('National Literature', category_name)
        self.assertEquals('Books', category_channel)
        self.assertEquals(None, category_parent_category)
        self.assertEquals(1, len(category_categories))

    def test_get_search_success_response(self):

        search_url = "{}?channel={}&name={}".format(
            reverse('list-category'),
            'Books',
            'National Literature'
        )
        response = self.client.get(search_url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals('National Literature', response.data[0]['name'])

    def test_get_search_error_response(self):

        search_url = "{}?channel={}&name={}".format(
            reverse('list-category'),
            'Books',
            'National'
        )
        response = self.client.get(search_url)
        self.assertEquals(response.status_code, status.HTTP_404_NOT_FOUND)
