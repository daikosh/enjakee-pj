from django.urls import path
from . import views


urlpatterns = [
    path('', views.IndexView.as_view()),
    path('projects/', views.ProjectsView.as_view()),
    path('aboutus/', views.AboutusView.as_view()),
    path('contact/', views.ContactView.as_view()),
    path('projects/timeline/', views.TimelineView.as_view()),
    path('projects/ann/', views.AnnView.as_view()),
    path('projects/ann/1/', views.Ann1View.as_view()),
    path('projects/ann/2/', views.Ann2View.as_view()),
    path('projects/ann/3/', views.Ann3View.as_view()),
    path('projects/ann/4/', views.Ann4View.as_view()),
    path('projects/wanko/', views.WankoView.as_view()),
    path('projects/ann0/', views.Ann0View.as_view()),
    path('projects/ann0/1/', views.Ann01View.as_view()),
    path('projects/ann0/2/', views.Ann02View.as_view()),
    path('projects/ann0/3/', views.Ann03View.as_view()),
    path('projects/ann0/4/', views.Ann04View.as_view()),
    path('projects/nyanko/', views.NyankoView.as_view()),
]
