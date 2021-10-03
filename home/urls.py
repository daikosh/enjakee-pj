from django.urls import path
from .views import IndexView, ProjectsView, AboutusView, ContactView
from .views import TimelineView, AnnView, WankoView, Ann0View, NyankoView


urlpatterns = [
    path('', IndexView.as_view()),
    path('projects/', ProjectsView.as_view()),
    path('aboutus/', AboutusView.as_view()),
    path('contact/', ContactView.as_view()),
    path('projects/timeline/', TimelineView.as_view()),
    path('projects/ann/', AnnView.as_view()),
    path('projects/wanko/', WankoView.as_view()),
    path('projects/ann0/', Ann0View.as_view()),
    path('projects/nyanko/', NyankoView.as_view()),
]
