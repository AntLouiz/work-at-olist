from django.core.exceptions import ObjectDoesNotExist
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.exceptions import NotFound
from .serializers import (
    ChannelSerializer,
    ChannelDetailSerializer,
    CategoryListSerializer
)

from channels.models import Channel, Category


class ChannelList(ListAPIView):

    queryset = Channel.objects.all()
    serializer_class = ChannelSerializer


class ChannelDetail(RetrieveAPIView):

    lookup_field = 'slug'
    queryset = Channel.objects.all()
    serializer_class = ChannelDetailSerializer


class CategoryList(ListAPIView):
    """
    Get the all the categories.
    You can filter a category using the channel name and the category name
    has argument. Example: `/api/categories/?channel=XBOX 360&name=Games`
    """
    serializer_class = CategoryListSerializer

    def get_queryset(self):
        queryset = Category.objects.all().filter(parent_category__isnull=True)
        channel = self.request.query_params.get('channel')
        name = self.request.query_params.get('name')

        if name and channel:
            try:
                queryset = Category.objects.get(
                    name=name,
                    channel__name=channel
                )

                return [queryset]
            except ObjectDoesNotExist:
                raise NotFound()

        return queryset
