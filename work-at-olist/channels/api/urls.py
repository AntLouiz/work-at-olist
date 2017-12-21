from django.conf.urls import url
from django.urls import path
from channels.api.views import (
    ChannelList,
    ChannelDetail,
    CategoryDetail
)

urlpatterns = [
    url(r'^channels/$', ChannelList.as_view(), name="list-channels"),
    path(
        'channels/<slug:slug>/',
        ChannelDetail.as_view(),
        name="detail-channel"
    ),
    path(
        'category/<slug:slug>/',
        CategoryDetail.as_view(),
        name="detail-category"
    ),
]
