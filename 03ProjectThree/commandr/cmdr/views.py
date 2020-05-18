from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import ListView
from .models import Cmdr
# Create your views here
class HomePageView(ListView):
    model=Cmdr
    template_name = 'button.html'