from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings

# Create your views here.

context = {
    'version': settings.SITE_VER
}


def index(request):
    return render(request, 'homepage.html', context)


def get_develop_log(request):
    return render(request, 'development_log.html', context)


def get_login_page(request):
    return render(request, 'login_page.html', context)


def get_signup_page(request):
    return render(request, 'signup.html', context)