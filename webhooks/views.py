from django.shortcuts import render
from django.http import request, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
import git

# Create your views here.
# @require_POST
@csrf_exempt
def webhook_update(request):
    print("AUTOMATIC BABY YEAHHHHHHHHHHH")
    print("IT'S GIT UPDATE BABY")
    print("So this will then PULL when a PUSH event happens")
    print("and we need to look into Python Decoupling")
    print("So then we have to:")
    print("git pull")
    print("restart server via touch wsgi")
    repo = git.Repo("jacksorjacksor-wagtailsite")
    origin = repo.remote(name="origin")
    origin.pull()
    return HttpResponse("<h1>HI!</h1>")
