from django.shortcuts import render
from django.http import request, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import git
import subprocess
import os
from django.core.mail import send_mail


def send_email_to_me(reason):
    pass
    # send_mail(
    #     f"jacksorjacksor - site issue: {reason}",
    #     f"Issue with {reason}",
    #     "rich@jacksorjacksor.xyz",
    #     ["jacksorjacksor@pm.me"],
    #     fail_silently=False,
    # )


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


def database_restore():
    command = "pg_restore"
    try:
        print_running(command)
        psql_command = "pg_restore --create --clean --host=jacksorjacksor-119.postgres.eu.pythonanywhere-services.com --port=10119 --no-password --dbname=jacksorjacksor --format=tar --username=jacksorjacksor --no-password /home/jacksorjacksor/jacksorjacksor-wagtailsite/database_dump.tar"
        psql_command_as_list = psql_command.split(" ")
        subprocess.run(psql_command_as_list)
        print_completed(command)
    except:
        print_issue(command)


# Create your views here.
# @require_POST # This didn't work for some reason, but OK!
@csrf_exempt
def webhook_update(request):
    repo = git.Repo("jacksorjacksor-wagtailsite")
    origin = repo.remote(name="origin")

    send_email_to_me("hi!!!")

    # command = "git stash"
    # try:
    #     print_running(command)
    #     repo.git.add(all=True)
    #     repo.git.stash()
    #     repo.git.stash("drop")
    #     print_completed(command)
    # except:
    #     print_issue(command)

    command = "git pull"
    try:
        print_running(command)
        origin.pull()
        subprocess.run(["git", "status"])
        print_completed(command)
    except:
        send_email_to_me("git pull")
        print_issue(command)

    # database_restore()
    # Removed this as would wipe out existing materials

    command = "activate venv"
    try:
        print_running(command)
        run_static_command = "source /home/jacksorjacksor/.virtualenvs/wagtail/bin/activate"
        run_static_command_as_list = run_static_command.split(" ")
        subprocess.run(run_static_command_as_list)
        print_completed(command)
    except:
        print_issue(command)

    command = "check django"
    try:
        print_running(command)
        run_static_command = "python ~/wagtail/jacksorjacksor-wagtailsite/manage.py check"
        run_static_command_as_list = run_static_command.split(" ")
        subprocess.run(run_static_command_as_list)
        print_completed(command)
    except:
        print_issue(command)

    command = "activate venv"
    try:
        print_running(command)
        run_static_command = "python ~/wagtail/jacksorjacksor-wagtailsite/manage.py collectstatic --noinput"
        run_static_command_as_list = run_static_command.split(" ")
        subprocess.run(run_static_command_as_list)
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

    print("Done!")

    return HttpResponse("<h1>HI!</h1>")  # probably should have something else here...
