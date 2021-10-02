from django.http import HttpResponse, HttpResponseForbidden, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
import git
import subprocess
from django.core.mail import send_mail
import os
from dotenv import load_dotenv
import hmac
import hashlib
import json

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


def send_email_to_me(reason):
    send_mail(
        f"jacksorjacksor - site issue: {reason}",
        f"Issue with {reason}",
        "rich@jacksorjacksor.xyz",
        ["jacksorjacksor@pm.me"],
        fail_silently=False,
    )


# FYI we're totally going to have to just use the more secure package
@csrf_exempt
def webhook_update(request):
    # AUTH: https://gist.github.com/grantmcconnaughey/6169d8b7a2e770e85c5617bc80ed00a9
    if not "X-Hub-Signature" in request.headers:
        return HttpResponseForbidden("Invalid")

    # from  django-github-webhook
    digest_name, signature = request.META["HTTP_X_HUB_SIGNATURE"].split("=")

    if digest_name != "sha1":
        return HttpResponseBadRequest(f"Unsupported X-HUB-SIGNATURE digest mode found: {digest_name}")

    secret_token = os.getenv("SECRET_TOKEN")

    mac = hmac.new(secret_token.encode("utf-8"), msg=request.body, digestmod=hashlib.sha1)

    if not hmac.compare_digest(mac.hexdigest(), signature):
        return HttpResponseBadRequest("Invalid X-HUB-SIGNATURE header found")

    # CONTENT
    # Global vars:
    repo = git.Repo("jacksorjacksor-wagtailsite")
    origin = repo.remote(name="origin")

    # Commands
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
