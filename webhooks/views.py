from django.http import HttpResponse, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt
import git
import subprocess
from django.core.mail import send_mail
import os
from dotenv import load_dotenv
import hmac
import hashlib

load_dotenv()


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


def send_email_to_me(reason, line):
    send_mail(
        f"jacksorjacksor - site issue: {reason}",
        f"Issue with {reason}: {line}",
        "rich@jacksorjacksor.xyz",
        ["jacksorjacksor@pm.me"],
        fail_silently=False,
    )


# @require_POST # This didn't work for some reason, but OK!
@csrf_exempt
def webhook_update(request):
    # AUTH: https://gist.github.com/grantmcconnaughey/6169d8b7a2e770e85c5617bc80ed00a9
    if not "X-Hub-Signature" in request.headers:
        return HttpResponseForbidden("Invalid")

    github_signature = request.META["HTTP_X_HUB_SIGNATURE"]
    signature = hmac.new(os.getenv("SECRET_TOKEN"), request.body, hashlib.sha1)
    expected_signature = "sha1=" + signature.hexdigest()

    if not hmac.compare_digest(github_signature, expected_signature):
        return HttpResponseForbidden("Invalid signature header")

    # CONTENT
    # Global var:
    repo = git.Repo("jacksorjacksor-wagtailsite")
    origin = repo.remote(name="origin")

    command = "git pull"
    try:
        print_running(command)
        origin.pull()
        subprocess.run(["git", "pull"])
        print_completed(command)
    except:
        send_email_to_me(command)
        print_issue(command)

    command = "restart server"
    try:
        print_running(command)
        subprocess.run(["touch", "/var/www/www_jacksorjacksor_xyz_wsgi.py"])
        print_completed(command)
    except:
        send_email_to_me(command)
        print_issue(command)

    print("Done!")  # final check

    return HttpResponse("<h1>Ah! You shouldn't be seeing this! How very rude!</h1>")
