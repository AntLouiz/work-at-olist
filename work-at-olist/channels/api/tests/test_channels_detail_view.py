from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from channels.models import Channel, Category


class TestChannelDetailView(APITestCase):

    def setUp(self):
        channel = Channel.objects.create(
            name='Games'
        )

        Category.objects.create(
            name='XBOX ONE',
            channel=channel
        )

        parent_category = Category.objects.create(
            name='XBOX 360',
            channel=channel
        )

        Category.objects.create(
            name='Console',
            channel=channel,
            parent_category=parent_category
        )

        Category.objects.create(
            name='Games',
            channel=channel,
            parent_category=parent_category
        )

        self.url = reverse(
            'detail-channel',
            kwargs={'slug': channel.slug}
        )

    def test_get_response(self):

        response = self.client.get(self.url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_get_response_error(self):
        error_url = reverse(
            'detail-channel',
            kwargs={'slug': 'known_slug'}
        )
        response = self.client.get(error_url)

        self.assertEquals(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_get_data_response(self):

        response = self.client.get(self.url)

        channel_name = response.data['name']
        channel_categories = response.data['categories']

        self.assertEquals('Games', channel_name)
        self.assertEquals(len(channel_categories), 2)

        self.assertEquals(channel_categories[0]['name'], 'XBOX 360')
        self.assertEquals(channel_categories[1]['name'], 'XBOX ONE')
