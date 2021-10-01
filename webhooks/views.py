from django.shortcuts import render
from django.http import request, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import git
import subprocess

## UTIL FUNCTIONS
def print_running(command):
    print(f">>> running {command}")
    return None


def print_completed(command):
    print(f"completed {command}")
    return None


def print_issue(command):
    print(f"issue with {command}")
    return None


# Create your views here.
# @require_POST # This didn't work for some reason, but OK!
@csrf_exempt
def webhook_update(request):
    repo = git.Repo("jacksorjacksor-wagtailsite")
    origin = repo.remote(name="origin")

    command = "git stash"
    try:
        print_running(command)
        repo.git.add(all=True)
        repo.git.stash()
        repo.git.stash("drop")
        print_completed(command)
    except:
        print_issue(command)

    command = "git pull"
    try:
        print_running(command)
        origin.pull()
        print_completed(command)
    except:
        print_issue(command)

    command = "restart server"
    try:
        print_running(command)
        subprocess.run(["touch", "/var/www/www_jacksorjacksor_xyz_wsgi.py"])
        print_completed(command)
    except:
        print_issue(command)

    command = "pg_restore"
    try:
        print_running(command)
        # Database dump - updated
        psql_command = "pg_restore --create --clean --host=jacksorjacksor-119.postgres.eu.pythonanywhere-services.com --port=10119 --no-password --dbname=jacksorjacksor --format=tar --username=jacksorjacksor filename=/home/jacksorjacksor/jacksorjacksor-wagtailsite/database_dump.tar"
        psql_command_as_list = psql_command.split(" ")
        subprocess.run(psql_command_as_list)
        print_completed(command)
    except:
        print_issue(command)

    command = "collectstatic"
    try:
        print_running(command)
        run_static_command = "source /home/jacksorjacksor/.virtualenvs/wagtail/bin/activate && cd /home/jacksorjacksor/jacksorjacksor-wagtailsite && python manage.py collectstatic --noinput"
        run_static_command_as_list = run_static_command.split(" ")
        subprocess.run(run_static_command_as_list)
        print_completed(command)
    except:
        print_issue(command)

    print("Done!")

    return HttpResponse("<h1>HI!</h1>")  # probably should have something else here...
