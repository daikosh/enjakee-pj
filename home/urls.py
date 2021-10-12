from django.urls import path
from . import views


urlpatterns = [
    path('', views.IndexView.as_view()),
    path('projects/', views.ProjectsView.as_view()),
    path('aboutus/', views.AboutusView.as_view()),
    path('contact/', views.ContactView.as_view()),
    path('projects/timeline/', views.TimelineView.as_view()),
    path('projects/ann/', views.AnnView.as_view()),
    path('projects/ann/1', views.Ann1View.as_view()),
    path('projects/wanko/', views.WankoView.as_view()),
    path('projects/ann0/', views.Ann0View.as_view()),
    path('projects/nyanko/', views.NyankoView.as_view()),
]
