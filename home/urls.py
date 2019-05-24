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

    path('web/list', views.get_web_list),
    path('free/list', views.get_free_list),
    path('routine/list', views.get_routine_list),
    path('lol/list', views.get_lol_list),
    path('deep_learning/list', views.get_DL_list),
    path('java/list', views.get_java_list),
    path('window_issue/list', views.get_window_list),
    path('individual/list', views.get_individual_list),

    path('web/write', views.get_web_write),
    path('free/write', views.get_free_write),
    path('routine/write', views.get_routine_write),
    path('lol/write', views.get_lol_write),
    path('deep_learning/write', views.get_DL_write),
    path('java/write', views.get_java_write),
    path('window_issue/write', views.get_window_write),
    path('individual/write', views.get_individual_write),

    path('web/posting', views.web_posting),

]