from rest_framework.generics import ListAPIView, RetrieveAPIView
from .serializers import ChannelSerializer, ChannelDetailSerializer
from channels.models import Channel


class ChannelList(ListAPIView):

    queryset = Channel.objects.all()
    serializer_class = ChannelSerializer


class ChannelDetail(RetrieveAPIView):

    lookup_field = 'slug'
    queryset = Channel.objects.all()
    serializer_class = ChannelDetailSerializer
