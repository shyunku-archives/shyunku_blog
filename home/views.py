from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from home.models import User_Info
# Create your views here.

context = {
    'version': settings.SITE_VER,
    'css_version': settings.CSS_VER,
}


def index(request):
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1
    context2 = {
        'version'       : settings.SITE_VER,
        'css_version'   : settings.CSS_VER,
        'visits'        : num_visits,
    }
    return render(request, 'homepage.html', context2)


def get_develop_log(request):
    return render(request, 'development_log.html', context)


def get_login_page(request):
    User_Infos = User_Info.objects.all()
    login_context = {
        'user_information': User_Infos,
        'css_version': settings.CSS_VER,
    }
    return render(request, 'login_page.html', login_context)


def get_signup_page(request):
    return render(request, 'signup.html', context)


def post_user_info(request):
    obj = User_Info(
        user_id=request.POST.get('user-id'),
        user_nickname=request.POST.get('user-nickname'),
        user_pw=request.POST.get('user-pw')
        )
    obj.save()
    return get_login_page(request)


def post_user_login(request):
    for user in User_Info.objects.filter().all():
        if user.user_id == request.POST.get('user-id'):
            request.session['username'] = user.user_nickname
            break
    return index(request)


def user_logout(request):
    try:
        del request.session['username']
    except:
        pass
    return index(request)