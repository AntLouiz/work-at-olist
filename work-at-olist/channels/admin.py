from django.contrib import admin
from channels.models import Channel, Category


class ChannelAdmin(admin.ModelAdmin):
    fields = ('name',)


class CategoryAdmin(admin.ModelAdmin):
    fields = ('name', 'channel', 'parent_category',)


admin.site.register(Channel, ChannelAdmin)
admin.site.register(Category, CategoryAdmin)
