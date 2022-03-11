from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from .forms import LoginForm


# class Top(TemplateView):
#     template_name = 'register/top.html'

class Login(LoginView):
    """ログインページ"""
    form_class = LoginForm
    template_name = 'register/login.html'

class Logout(LogoutView):
    """ログアウトページ"""
    template_name = 'register/login.html'

class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'index.html'

class ProjectsView(LoginRequiredMixin, TemplateView):
    template_name = 'projects.html'

class AboutusView(LoginRequiredMixin, TemplateView):
    template_name = 'aboutus.html'

class ContactView(LoginRequiredMixin, TemplateView):
    template_name = 'contact.html'

class FaqView(LoginRequiredMixin, TemplateView):
    template_name = 'faq.html'

class TimelineView(LoginRequiredMixin, TemplateView):
    template_name = 'projects/timeline.html'

class Timeline1View(LoginRequiredMixin, TemplateView):
    template_name = 'projects/timeline/1.html'

class Timeline2View(LoginRequiredMixin, TemplateView):
    template_name = 'projects/timeline/2.html'

class Timeline3View(LoginRequiredMixin, TemplateView):
    template_name = 'projects/timeline/3.html'

class Timeline4View(LoginRequiredMixin, TemplateView):
    template_name = 'projects/timeline/4.html'

class Timeline5View(LoginRequiredMixin, TemplateView):
    template_name = 'projects/timeline/5.html'

class Timeline6View(LoginRequiredMixin, TemplateView):
    template_name = 'projects/timeline/6.html'

class Timeline7View(LoginRequiredMixin, TemplateView):
    template_name = 'projects/timeline/7.html'

class AnnView(LoginRequiredMixin, TemplateView):
    template_name = 'projects/ann.html'

class Ann1View(LoginRequiredMixin, TemplateView):
    template_name = 'projects/ann/1.html'

class Ann2View(LoginRequiredMixin, TemplateView):
    template_name = 'projects/ann/2.html'

class Ann3View(LoginRequiredMixin, TemplateView):
    template_name = 'projects/ann/3.html'

class Ann4View(LoginRequiredMixin, TemplateView):
    template_name = 'projects/ann/4.html'

class Ann5View(LoginRequiredMixin, TemplateView):
    template_name = 'projects/ann/5.html'

class Ann6View(LoginRequiredMixin, TemplateView):
    template_name = 'projects/ann/6.html'

class Ann65View(LoginRequiredMixin, TemplateView):
    template_name = 'projects/ann/6.5.html'

class Ann7View(LoginRequiredMixin, TemplateView):
    template_name = 'projects/ann/7.html'

class Ann8View(LoginRequiredMixin, TemplateView):
    template_name = 'projects/ann/8.html'

class Ann9View(LoginRequiredMixin, TemplateView):
    template_name = 'projects/ann/9.html'

class WankoView(LoginRequiredMixin, TemplateView):
    template_name = 'projects/wanko.html'

class Wanko1View(LoginRequiredMixin, TemplateView):
    template_name = 'projects/wanko/1.html'

class Wanko2View(LoginRequiredMixin, TemplateView):
    template_name = 'projects/wanko/2.html'

class Wanko3View(LoginRequiredMixin, TemplateView):
    template_name = 'projects/wanko/3.html'

class Wanko4View(LoginRequiredMixin, TemplateView):
    template_name = 'projects/wanko/4.html'

class Wanko5View(LoginRequiredMixin, TemplateView):
    template_name = 'projects/wanko/5.html'

class Wanko6View(LoginRequiredMixin, TemplateView):
    template_name = 'projects/wanko/6.html'

class Wanko7View(LoginRequiredMixin, TemplateView):
    template_name = 'projects/wanko/7.html'

class Wanko8View(LoginRequiredMixin, TemplateView):
    template_name = 'projects/wanko/8.html'

class Ann0View(LoginRequiredMixin, TemplateView):
    template_name = 'projects/ann0.html'

class Ann01View(LoginRequiredMixin, TemplateView):
    template_name = 'projects/ann0/1.html'

class Ann02View(LoginRequiredMixin, TemplateView):
    template_name = 'projects/ann0/2.html'

class Ann03View(LoginRequiredMixin, TemplateView):
    template_name = 'projects/ann0/3.html'

class Ann04View(LoginRequiredMixin, TemplateView):
    template_name = 'projects/ann0/4.html'

class Ann05View(LoginRequiredMixin, TemplateView):
    template_name = 'projects/ann0/5.html'

class Ann06View(LoginRequiredMixin, TemplateView):
    template_name = 'projects/ann0/6.html'

class Ann07View(LoginRequiredMixin, TemplateView):
    template_name = 'projects/ann0/7.html'

class Ann08View(LoginRequiredMixin, TemplateView):
    template_name = 'projects/ann0/8.html'

class NyankoView(LoginRequiredMixin, TemplateView):
    template_name = 'projects/nyanko.html'