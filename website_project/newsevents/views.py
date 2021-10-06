from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import ListView
from .models import NewsArticles

class NewsEvents(ListView):
    model = NewsArticles
    template_name = 'NewsEvents.html'
    context_object_name = 'NewsArticles'