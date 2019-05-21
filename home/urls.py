from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('homepage', views.index),
    path('develop_log', views.get_develop_log)
]