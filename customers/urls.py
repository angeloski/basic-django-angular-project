from django.conf.urls import patterns, url
from .views import RelationsListView, RelationsAddView

urlpatterns = patterns('',
    url(r'^relations/$', RelationsListView.as_view(), name='relations-list'),
    url(r'^relations/add/$', RelationsAddView.as_view(), name='relations-add'),
)