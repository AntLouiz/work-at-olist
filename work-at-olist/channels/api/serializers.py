from rest_framework.serializers import ModelSerializer
from channels.models import Channel


class ChannelSerializer(ModelSerializer):

    class Meta:
        model = Channel
        fields = ('id', 'name')
