from django.views.generic import TemplateView

class memberpages(TemplateView):
    template_name = 'memberpages/memberpages.html'

class logankeim(TemplateView):
    template_name = 'memberpages/logankeim.html'