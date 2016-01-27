from django.conf.urls import patterns, url
from .views import ProductsListView, ProductsAddView

urlpatterns = patterns('',
    url(r'^products/$', ProductsListView.as_view(), name='products-list'),
    url(r'^products/add/$', ProductsAddView.as_view(), name='products-add'),
)