from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from channels.models import Channel


class TestChannelListView(APITestCase):

    def setUp(self):
        Channel.objects.create(
            name='Games'
        )

        Channel.objects.create(
            name='Books'
        )

        self.url = reverse('list-channels')

    def test_get_response(self):

        response = self.client.get(self.url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_get_data_response(self):

        response = self.client.get(self.url)

        channel_name = response.data[0]['name']
        channel_id = response.data[0]['id']
        channel_detail_url = response.data[0]['detail_url']

        self.assertEquals(channel_name, 'Games')
        self.assertEquals(channel_id, 1)
        self.assertIn('/api/channels/games/', channel_detail_url)

        channel_name = response.data[1]['name']
        channel_id = response.data[1]['id']
        channel_detail_url = response.data[1]['detail_url']

        self.assertEquals(channel_name, 'Books')
        self.assertEquals(channel_id, 2)
        self.assertIn('/api/channels/books/', channel_detail_url)
