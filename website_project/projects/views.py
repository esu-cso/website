from django.views.generic import TemplateView

class ProjectPage(TemplateView):
    template_name = 'projects.html'

class ExtraLife(TemplateView):
    template_name = 'projects/extralife.html'
