from django.urls import path, include
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

    path('board', views.get_board_list),
    path('write-post', views.get_write_post),
    path('posting', views.post_document),
    path('postview', views.postview)
]