from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import TemplateView, ListView
from .models import NewsArticles, NewsCarousel

class NewsEvents(TemplateView):
    template_name = 'NewsEvents.html'
    context_object_name = 'news_list'

    def get_context_data(self, **kwargs):
        context = super(NewsEvents, self).get_context_data(**kwargs)
        context.update({
            'FirstNewsCarousel': NewsCarousel.objects.filter()[:1],
            'NewsCarousel': NewsCarousel.objects.filter()[1:],
            'NewsArticles': NewsArticles.objects.all(),
        })

        return context
