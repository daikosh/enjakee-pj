from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'index.html'

class ProjectsView(TemplateView):
    template_name = 'projects.html'

class AboutusView(TemplateView):
    template_name = 'aboutus.html'

class ContactView(TemplateView):
    template_name = 'contact.html'

class TimelineView(TemplateView):
    template_name = 'timeline.html'

class AnnView(TemplateView):
    template_name = 'ann.html'

class WankoView(TemplateView):
    template_name = 'wanko.html'

class Ann0View(TemplateView):
    template_name = 'ann0.html'
    
class NyankoView(TemplateView):
    template_name = 'nyanko.html'