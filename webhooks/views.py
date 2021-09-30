from django.shortcuts import render
from django.http import request, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
import git
import subprocess

# Create your views here.
# @require_POST
@csrf_exempt
def webhook_update(request):
    repo = git.Repo("jacksorjacksor-wagtailsite")
    origin = repo.remote(name="origin")
    origin.pull()
    print("here?")
    try:
        subprocess.run(["touch", "/var/www/www_jacksorjacksor_xyz_wsgi.py"])
        print("server restarted!")
    except:
        print("couldn't restart server")
    return HttpResponse("<h1>HI!</h1>")  # probably should have something else here...
