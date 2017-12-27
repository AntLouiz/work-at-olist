from django.conf.urls import url
from django.urls import path
from rest_framework.documentation import include_docs_urls
from channels.api.views import (
    ChannelList,
    ChannelDetail,
    CategoryList
)

urlpatterns = [
    url(r'^docs/', include_docs_urls(
        title='Channels API'
    )),
    url(r'^channels/$', ChannelList.as_view(), name="list-channels"),
    path(
        'channels/<slug:slug>/',
        ChannelDetail.as_view(),
        name="detail-channel"
    ),
    url(r'^categories/', CategoryList.as_view(), name="list-category"),
]
