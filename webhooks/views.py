from django.shortcuts import render
from django.http import request, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import git
import subprocess

# Create your views here.
# @require_POST # This didn't work for some reason, but OK!
@csrf_exempt
def webhook_update(request):
    repo = git.Repo("jacksorjacksor-wagtailsite")
    origin = repo.remote(name="origin")

    try:
        repo.git.add(all=True)
        repo.git.stash()
        repo.git.stash("drop")
    except:
        pass

    try:
        origin.pull()
    except:
        print("Issue with git pull")
    try:
        subprocess.run(["touch", "/var/www/www_jacksorjacksor_xyz_wsgi.py"])
        print("server restarted!")
    except:
        print("couldn't restart server")

    try:
        # Database dump:
        psql_command = "pg_restore --create --clean --host=jacksorjacksor-119.postgres.eu.pythonanywhere-services.com --port=10119 --no-password --file=database_dump --format=tar --username=jacksorjacksor --dbname=jacksorjacksor"
        psql_command_as_list = psql_command.split(" ")
        subprocess.run(psql_command_as_list)
    except:
        print("Database issues")

    # Collect Static
    try:
        command = "cd /home/jacksorjacksor/jacksorjacksor-wagtailsite && workon wagtail && python manage.py collectstatic --noinput"
        command_as_list = command.split(" ")
        subprocess.run(command_as_list)

    except:
        print("Collect static issue")

    return HttpResponse("<h1>HI!</h1>")  # probably should have something else here...


import subprocess
