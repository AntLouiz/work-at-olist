from django.conf.urls import url
from django.urls import path
from channels.api.views import ChannelList, ChannelDetail

urlpatterns = [
    url(r'^channels/$', ChannelList.as_view(), name="list-channels"),
    path(
        'channels/<slug:slug>/',
        ChannelDetail.as_view(),
        name="detail-channel"
    ),
]
