from django.conf import settings
from home.models import User_Info, Variables, Documents_Info, Comment
from home.forms import PostForm
from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from home.custom import *



context_default = {
    'version': settings.SITE_VER,
    'css_version': settings.CSS_VER,
    'superuser_id': settings.SUPERUSER_ID,
    'user_info_condition': settings.USER_INFO_CONDITION,
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
    datas = Variables.objects.all()
    if len(datas) == 0:
        obj = Variables(
            visits= 0,
            doc_index_recent= 0,
            visits_free=0,
            visits_rout=0,
            visits_lol=0,
            visits_dl=0,
            visits_web=0,
            visits_java=0,
            visits_window=0,
            visits_indiv=0
        )
        obj.save()
    context_default = {
        'version'            : settings.SITE_VER,
        'css_version'        : settings.CSS_VER,
        'superuser_id'       : settings.SUPERUSER_ID,
        'user_info_condition': settings.USER_INFO_CONDITION,
        'variables'          : Variables.objects.all().first(),
        'process_rate'       : settings.PROCESS_RATE,
    }


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
    update_context()
    User_Infos = User_Info.objects.all()

    prev = request.GET.get('call')
    login_context = {
        'user_information': User_Infos,
        'previous_call' : prev,
    }
    return render(request, 'major/login_page.html', merge_dicts(context_default, login_context))


def get_signup_page(request):
    update_context()
    User_Infos = User_Info.objects.all()
    login_context = {
        'user_information': User_Infos,
    }
    return render(request, 'major/signup.html', merge_dicts(context_default, login_context))


def post_user_info(request):
    obj = User_Info(
        user_id=request.POST.get('user-id'),
        user_nickname=request.POST.get('user-nickname'),
        user_pw=request.POST.get('user-pw')
    )
    obj.save()
    return redirect('/login')


def post_user_login(request):
    for user in User_Info.objects.filter().all():
        if user.user_id == request.POST.get('user-id'):
            request.session['username'] = user.user_nickname
            request.session['userid'] = user.user_id
            break

    previous = request.GET.get('call')

    if previous == None:
        return redirect('/homepage')
    return redirect('/board?name=' + previous)


def user_logout(request):
    try:
        del request.session['username']
        del request.session['userid']
    except:
        pass
    return redirect('/homepage')


def get_board_list(request):
    update_context()

    classification = request.GET.get('name')

    visit_num = update_visits(classification)

    board_name = switch_urlname_to_board_name(classification)

    post_all_list = Documents_Info.objects.filter(classify=classification).order_by('doc_index').reverse()
    paginator = Paginator(post_all_list, settings.PAGE_MAX_DETAILS)

    page = request.GET.get('page')

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    ranger = range(1,settings.PAGE_MAX_CHAPTER+1)

    if page != None :
        pagei = int(page)
        page_page = (int)((pagei-1)/settings.PAGE_MAX_CHAPTER)
        ranger = range(
            page_page * settings.PAGE_MAX_CHAPTER + 1,
            (page_page+1) * settings.PAGE_MAX_CHAPTER + 1,
                            )

    page_viewed_total = 0
    posts_num = len(post_all_list)


    for post_data in post_all_list:
        page_viewed_total += post_data.doc_view_cnt

    addition = {
        'posts' : posts,
        'max_page': settings.PAGE_MAX_CHAPTER,
        'page_range': ranger,
        'board_name' : board_name,
        'classification' : classification,
        'visits': visit_num,
        'post_num': posts_num,
        'page_viewed_total': page_viewed_total,
    }
    merged = merge_dicts(context_default, document_context)
    return render(request, 'major/post_list.html', merge_dicts(merged, addition))



# WRITE PAGES


def get_write_post(request):
    update_context()
    pform = PostForm()

    classification = request.GET.get('board')
    board_rename = switch_urlname_to_board_name_trick(classification)
    addition = {
        'form' : pform,
        'board_name' : board_rename,
        'classification' : classification
    }
    merged = merge_dicts(context_default, document_context)
    return render(request, 'major/new_post.html', merge_dicts(merged, addition))



# Posting PAGES


def post_document(request):
    recent_index = Variables.objects.all().first().doc_index_recent + 1
    Variables.objects.all().first().update(doc_index_recent=recent_index)

    classification = request.GET.get('board')

    new_doc = Documents_Info(
        classify= classification,
        doc_index='{:05d}'.format(recent_index),
        doc_title=request.POST.get('doc-title'),
        doc_writer=request.session['username'],
        doc_content=request.POST.get('fields'),
        doc_view_cnt=0
    )

    new_doc.save()

    url_trick = request.GET.get('board')

    return redirect('/board?name='+url_trick)


# Post View


def postview(request):
    update_context()

    classification = request.GET.get('classify')
    board_name = switch_urlname_to_board_name_trick(classification)

    post_index = request.GET.get('pindex')
    datas = Documents_Info.objects.filter(doc_index=post_index)
    Documents_Info.objects.filter(doc_index=post_index).update(doc_view_cnt= datas.first().doc_view_cnt+1)

    post = Documents_Info.objects.filter(doc_index=post_index).first()


    addition = {
        'doc_data' : datas.first(),
        'board_name' : board_name,
        'post': post,
    }

    merged = merge_dicts(context_default, document_context)
    return render(request, 'major/show_post.html', merge_dicts(merged, addition))


def save_new_comment(request):
    if request.method == 'POST':

        recent_index = Variables.objects.all().first().comment_index_recent + 1
        Variables.objects.all().first().update(comment_index_recent=recent_index)

        post = Documents_Info.objects.filter(doc_index=request.POST['post_id']).first()
        user = User_Info.objects.filter(user_id=request.session['userid']).first()
        Comments.objects.create(
            comment_content=request.POST['comment_contents'],
            comment_writer=user,
            comment_post=post,
            comment_id='{:06d}'.format(recent_index),
        )
        return redirect('/postview?pindex='+post.doc_index+'&classify='+post.classify)
