from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from home.models import User_Info, Variables, Documents_Info

from home.models import Post
from home.forms import PostForm

from django.shortcuts import render, redirect


context_default = {
    'version': settings.SITE_VER,
    'css_version': settings.CSS_VER,
    'superuser_id': settings.SUPERUSER_ID,
    'user_info_condition': settings.USER_INFO_CONDITION,
    'variables': Variables.objects.all()[0],
    'process_rate': settings.PROCESS_RATE,
}

document_context = {
    'document_info' : Documents_Info.objects.all(),
}


def update_context():
    global document_context, context_default
    document_context = {
        'document_info': Documents_Info.objects.all(),
    }
    context_default = {
        'version'            : settings.SITE_VER,
        'css_version'        : settings.CSS_VER,
        'superuser_id'       : settings.SUPERUSER_ID,
        'user_info_condition': settings.USER_INFO_CONDITION,
        'variables'          : Variables.objects.all()[0],
        'process_rate'       : settings.PROCESS_RATE,
    }


def merge_dicts(x, y):
    return {**x, **y}


def index(request):
    save_count = 0
    for visit_counter in Variables.objects.filter().all():
        save_count = visit_counter.visits+1
        break

    Variables.objects.filter().all().update(visits=save_count)

    context2 = {
        'superuser_id': settings.SUPERUSER_ID,
    }
    update_context()
    return render(request, 'major/homepage.html', merge_dicts(context_default, context2))


def get_develop_log(request):
    update_context()
    return render(request, 'major/development_log.html', context_default)


def get_login_page(request):
    User_Infos = User_Info.objects.all()
    login_context = {
        'user_information': User_Infos,
    }
    update_context()
    return render(request, 'major/login_page.html', merge_dicts(context_default, login_context))


def get_signup_page(request):
    update_context()
    return render(request, 'major/signup.html', context_default)


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
        del request.session['userid']
    except:
        pass
    return index(request)



# LIST PAGES


def get_web_list(request):
    for i in Documents_Info.objects.all():
        print(i.doc_title)
    update_context()
    return render(request, 'list_pages/web_list.html', merge_dicts(context_default, document_context))


def get_routine_list(request):
    return render(request, 'list_pages/routine_list.html', merge_dicts(context_default, document_context))


def get_lol_list(request):
    return render(request, 'list_pages/lol_list.html', merge_dicts(context_default, document_context))


def get_DL_list(request):
    return render(request, 'list_pages/dl_list.html', merge_dicts(context_default, document_context))


def get_java_list(request):
    return render(request, 'list_pages/java_list.html', merge_dicts(context_default, document_context))


def get_window_list(request):
    return render(request, 'list_pages/window_list.html', merge_dicts(context_default, document_context))


def get_free_list(request):
    return render(request, 'list_pages/free_list.html', merge_dicts(context_default, document_context))


def get_individual_list(request):
    return render(request, 'list_pages/individual_list.html', merge_dicts(context_default, document_context))



# WRITE PAGES


def get_web_write(request):
    pform = PostForm()
    addition = {
        'form' : pform,
    }
    update_context()
    merged = merge_dicts(context_default, document_context)
    return render(request, 'write_pages/web_write.html', merge_dicts(merged, addition))


def get_routine_write(request):
    return render(request, 'write_pages/routine_write.html', merge_dicts(context_default, document_context))


def get_lol_write(request):
    return render(request, 'write_pages/lol_write.html', merge_dicts(context_default, document_context))


def get_DL_write(request):
    return render(request, 'write_pages/dl_write.html', merge_dicts(context_default, document_context))


def get_java_write(request):
    return render(request, 'write_pages/java_write.html', merge_dicts(context_default, document_context))


def get_window_write(request):
    return render(request, 'write_pages/window_write.html', merge_dicts(context_default, document_context))


def get_individual_write(request):
    return render(request, 'write_pages/individual_write.html', merge_dicts(context_default, document_context))


def get_free_write(request):
    pform = PostForm()
    addition = {
        'form' : pform,
    }
    merged = merge_dicts(context_default, document_context)
    return render(request, 'write_pages/free_write.html', merge_dicts(merged, addition))



# Posting PAGES


def web_posting(request):
    recent_index = -1
    for variable in Variables.objects.filter().all():
        recent_index = variable.doc_index_recent+1
        break

    Variables.objects.all().update(doc_index_recent=recent_index)

    new_doc = Documents_Info(
        classify='WEB',
        doc_index='{:05d}'.format(recent_index),
        doc_title=request.POST.get('doc-title'),
        doc_writer=request.session['username'],
        doc_content=request.POST.get('fields'),
        doc_view_cnt=0
    )

    new_doc.save()
    print("generated!")

    return redirect('../web/list')
