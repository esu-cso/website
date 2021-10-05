from django.views.generic import TemplateView

class ProjectPage(TemplateView):
    template_name = 'projects/projects.html'

class ExtraLifePage(TemplateView):
    template_name = 'projects/extralife.html'

class TelescopePage(TemplateView):
    template_name = 'projects/telescope.html'

class ConferencesPage(TemplateView):
    template_name = 'projects/conferences.html'

class WindTurbinePage(TemplateView):
    template_name = 'projects/windturbine.html'

class GameDevPage(TemplateView):
    template_name = 'projects/gamedev.html'