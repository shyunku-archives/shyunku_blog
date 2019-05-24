from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('homepage', views.index),
    path('develop_log', views.get_develop_log),
    path('login',views.get_login_page),
    path('signup', views.get_signup_page),
    path('save_data', views.post_user_info),
    path('authen', views.post_user_login),
    path('logout', views.user_logout),
]