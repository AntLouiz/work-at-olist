from rest_framework.generics import ListAPIView, RetrieveAPIView
from .serializers import (
    ChannelSerializer,
    ChannelDetailSerializer,
    CategorySerializer
)

from channels.models import Channel, Category


class ChannelList(ListAPIView):

    queryset = Channel.objects.all()
    serializer_class = ChannelSerializer


class ChannelDetail(RetrieveAPIView):

    lookup_field = 'slug'
    queryset = Channel.objects.all()
    serializer_class = ChannelDetailSerializer


class CategoryDetail(RetrieveAPIView):

    lookup_field = 'slug'
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
