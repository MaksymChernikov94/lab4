from django.conf.urls import url, include
from django.contrib import admin

from news.views import IndexView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^news/', include('news.urls', namespace='news'))
]
