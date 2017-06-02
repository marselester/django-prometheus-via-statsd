from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^hello/', include('olympus.apps.hello.urls')),
    url(r'^admin/', admin.site.urls),
]
