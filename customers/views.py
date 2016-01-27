from django.shortcuts import render
from django.views.generic.base import TemplateView
from meubisapp.views import LoginRequired


class RelationsListView(LoginRequired, TemplateView):
    template_name = "relations_list.html"  


class RelationsAddView(LoginRequired, TemplateView):
    template_name = "relations_add.html"  