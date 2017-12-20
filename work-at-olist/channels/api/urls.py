from django.conf.urls import url
from channels.api.views import ChannelList

urlpatterns = [
    url(r'^channels/', ChannelList.as_view(), name="api-list-channels"),
]
