from home.models import Variables

def merge_dicts(x, y):
    return {**x, **y}

def switch_urlname_to_board_name(str):
    strdict = {
        'free' : "자유게시판",
        'routine' : "일상",
        'league-of-legends' : "LOL",
        'deep-learning' : "딥러닝",
        'web' : "WEB",
        'java' : "JAVA",
        'window-issues': "Window",
        "individual": "개인게시판",
    }

    returns = strdict.get(str, "null")

    return returns

def switch_urlname_to_board_name_trick(str):
    strdict = {
        'free' : "자유",
        'routine' : "일상",
        'league-of-legends' : "리그오브레전드",
        'deep-learning' : "Deep-Learning",
        'web' : "WEB",
        'java' : "JAVA",
        'window-issues': "Window Issues",
        "individual": "개인",
    }

    returns = strdict.get(str, "null")

    return returns


def update_visits(classify):
    value = 0
    if classify == "free":
        value = Variables.objects.first().visits_free
        Variables.objects.all().update(visits_free= value+1)
    elif classify == "routine":
        value = Variables.objects.first().visits_rout
        Variables.objects.all().update(visits_rout=value + 1)
    elif classify == "league-of-legends":
        value = Variables.objects.first().visits_lol
        Variables.objects.all().update(visits_lol=value + 1)
    elif classify == "deep-learning":
        value = Variables.objects.first().visits_dl
        Variables.objects.all().update(visits_dl=value + 1)
    elif classify == "web":
        value = Variables.objects.first().visits_web
        Variables.objects.all().update(visits_web=value + 1)
    elif classify == "java":
        value = Variables.objects.first().visits_java
        Variables.objects.all().update(visits_java=value + 1)
    elif classify == "window-issues":
        value = Variables.objects.first().visits_window
        Variables.objects.all().update(visits_window=value + 1)
    elif classify == "individual":
        value = Variables.objects.first().visits_indiv
        Variables.objects.all().update(visits_indiv=value + 1)
    return value+1