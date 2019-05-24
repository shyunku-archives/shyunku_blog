from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from home.models import User_Info, Variables, Documents_Info
# Create your views here.

context_default = {
    'version': settings.SITE_VER,
    'css_version': settings.CSS_VER,
    'superuser_id': settings.SUPERUSER_ID,
    'user_info_condition': settings.USER_INFO_CONDITION,
    'variables': Variables.objects.all()[0],
}

document_context = {
    'document_info' : Documents_Info.objects.all(),
}


def merge_dicts(x, y):
    return {**x, **y}


def index(request):
    save_count = 0
    for visit_counter in Variables.objects.filter().all():
        save_count = visit_counter.visits+1
        print(str(save_count))
        break

    Variables.objects.filter().all().update(visits=save_count)

    context2 = {
        'superuser_id': settings.SUPERUSER_ID,
    }
    return render(request, 'homepage.html', merge_dicts(context_default, context2))


def get_develop_log(request):
    return render(request, 'development_log.html', context_default)


def get_login_page(request):
    User_Infos = User_Info.objects.all()
    login_context = {
        'user_information': User_Infos,
    }
    return render(request, 'login_page.html', merge_dicts(context_default, login_context))


def get_signup_page(request):
    return render(request, 'signup.html', context_default)


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
            request.session['userid'] = user.user_id
            break
    return index(request)


def user_logout(request):
    try:
        del request.session['username']
    except:
        pass
    return index(request)


def get_web_list(request):
    return render(request, 'WEB_list.html', merge_dicts(context_default, document_context))