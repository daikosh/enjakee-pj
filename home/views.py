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
    template_name = 'projects/timeline.html'

class Timeline1View(TemplateView):
    template_name = 'projects/timeline/1.html'

class Timeline2View(TemplateView):
    template_name = 'projects/timeline/2.html'

class Timeline3View(TemplateView):
    template_name = 'projects/timeline/3.html'

class Timeline4View(TemplateView):
    template_name = 'projects/timeline/4.html'

class AnnView(TemplateView):
    template_name = 'projects/ann.html'

class Ann1View(TemplateView):
    template_name = 'projects/ann/1.html'

class Ann2View(TemplateView):
    template_name = 'projects/ann/2.html'

class Ann3View(TemplateView):
    template_name = 'projects/ann/3.html'

class Ann4View(TemplateView):
    template_name = 'projects/ann/4.html'

class WankoView(TemplateView):
    template_name = 'projects/wanko.html'

class Ann0View(TemplateView):
    template_name = 'projects/ann0.html'

class Ann01View(TemplateView):
    template_name = 'projects/ann0/1.html'

class Ann02View(TemplateView):
    template_name = 'projects/ann0/2.html'

class Ann03View(TemplateView):
    template_name = 'projects/ann0/3.html'

class Ann04View(TemplateView):
    template_name = 'projects/ann0/4.html'

class NyankoView(TemplateView):
    template_name = 'projects/nyanko.html'