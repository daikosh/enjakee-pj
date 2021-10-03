from django.urls import path
from .views import IndexView, ANNView

urlpatterns = [
    path('', IndexView.as_view()),
    path('ann/', ANNView.as_view()),
]
