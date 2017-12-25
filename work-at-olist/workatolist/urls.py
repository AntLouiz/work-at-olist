from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('channels.urls')),
    url(r'^api/', include('channels.api.urls'))
]
