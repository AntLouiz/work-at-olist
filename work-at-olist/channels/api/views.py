from rest_framework.generics import ListAPIView
from .serializers import ChannelSerializer
from channels.models import Channel


class ChannelList(ListAPIView):

    queryset = Channel.objects.all()
    serializer_class = ChannelSerializer
