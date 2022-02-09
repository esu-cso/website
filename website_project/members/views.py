from django.views.generic import TemplateView

class MembersPage(TemplateView):
    template_name = 'members/members.html'

class PMautePaige(TemplateView):
    template_name = 'members/PMaute.html'