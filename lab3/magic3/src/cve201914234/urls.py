from django.contrib import admin
from django.urls import path, include
from django.conf import settings

URL_BASE = settings.URL_BASE
urlpatterns = [
    path(URL_BASE + '/admin/', admin.site.urls),
    path(URL_BASE, include('magic3.urls'))
]
