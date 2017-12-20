from django.db.models import Q
from rest_framework.serializers import (
    Serializer,
    SerializerMethodField,
    HyperlinkedIdentityField,
    ModelSerializer
)
from channels.models import Channel, Category


class RecursiveSerializer(Serializer):

    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data


class CategorySerializer(ModelSerializer):
    categories = RecursiveSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ('id', 'name', 'categories')


class ChannelSerializer(ModelSerializer):

    detail_url = HyperlinkedIdentityField(
        view_name='detail-channel',
        lookup_field='slug'
    )

    class Meta:
        model = Channel
        fields = ('id', 'name', 'detail_url')


class ChannelDetailSerializer(ModelSerializer):
    categories = SerializerMethodField()

    class Meta:
        model = Channel
        fields = ('id', 'name', 'categories')

    def get_categories(self, obj):
        categories = Category.objects.filter(
            Q(channel__slug=obj.slug) & Q(parent_category__isnull=True)
        )
        serializer = CategorySerializer(categories, many=True)

        return serializer.data
