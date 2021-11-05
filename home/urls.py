from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.Login.as_view(), name='login'),
    path('index/', views.IndexView.as_view(), name='index'),
    # path('login/', views.Login.as_view(), name='login'),
    # path('logout/', views.Logout.as_view(), name='logout'),
    path('projects/', views.ProjectsView.as_view()),
    path('aboutus/', views.AboutusView.as_view()),
    path('contact/', views.ContactView.as_view()),
    path('projects/timeline/', views.TimelineView.as_view()),
    path('projects/timeline/1/', views.Timeline1View.as_view()),
    path('projects/timeline/2/', views.Timeline2View.as_view()),
    path('projects/timeline/3/', views.Timeline3View.as_view()),
    path('projects/timeline/4/', views.Timeline4View.as_view()),
    path('projects/ann/', views.AnnView.as_view()),
    path('projects/ann/1/', views.Ann1View.as_view()),
    path('projects/ann/2/', views.Ann2View.as_view()),
    path('projects/ann/3/', views.Ann3View.as_view()),
    path('projects/ann/4/', views.Ann4View.as_view()),
    path('projects/ann/5/', views.Ann5View.as_view()),
    path('projects/wanko/', views.WankoView.as_view()),
    path('projects/wanko/1/', views.Wanko1View.as_view()),
    path('projects/wanko/2/', views.Wanko2View.as_view()),
    path('projects/wanko/3/', views.Wanko3View.as_view()),
    path('projects/wanko/4/', views.Wanko4View.as_view()),
    path('projects/wanko/5/', views.Wanko5View.as_view()),
    path('projects/ann0/', views.Ann0View.as_view()),
    path('projects/ann0/1/', views.Ann01View.as_view()),
    path('projects/ann0/2/', views.Ann02View.as_view()),
    path('projects/ann0/3/', views.Ann03View.as_view()),
    path('projects/ann0/4/', views.Ann04View.as_view()),
    path('projects/nyanko/', views.NyankoView.as_view()),
]
