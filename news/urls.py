from django.conf.urls import url, include

from .views import NewsDetail, vote, ResultsView

urlpatterns = [
    url(r'^(?P<pk>[0-9]+)$', NewsDetail.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/vote$', vote, name='vote'),
    url(r'^(?P<pk>[0-9]+)/results', ResultsView.as_view(), name='results')
]
