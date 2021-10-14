from django.views.generic import TemplateView


class HomePage(TemplateView):
    template_name = 'index.html'

class ConstructionPage(TemplateView):
    template_name = 'underconstruction.html'

class ThanksPage(TemplateView):
    template_name = 'thanks.html'

class AboutUsPage(TemplateView):
    template_name = 'aboutus.html'




