from django.shortcuts import render
from django.views.generic.base import TemplateView
from meubisapp.views import LoginRequired


class ProductsListView(LoginRequired, TemplateView):
    template_name = "products_list.html"  


class ProductsAddView(LoginRequired, TemplateView):
    template_name = "products_add.html"  