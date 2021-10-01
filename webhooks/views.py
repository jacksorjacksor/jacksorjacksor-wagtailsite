from django.http.response import HttpResponseBadRequest
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import git
import subprocess
from django.core.mail import send_mail
import os
from dotenv import load_dotenv
import hmac

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


def run_list_of_commands(command, tuple_of_python_lines):
    success = True
    print_running(command)
    for line in tuple_of_python_lines:
        try:
            exec(line)
        except:
            send_email_to_me(command, line)
            success = False
    if success:
        print_completed(command)
    else:
        print_issue(command)


def send_email_to_me(reason, line):
    send_mail(
        f"jacksorjacksor - site issue: {reason}",
        f"Issue with {reason}: {line}",
        "rich@jacksorjacksor.xyz",
        ["jacksorjacksor@pm.me"],
        fail_silently=False,
    )


# Global var:
repo = git.Repo("jacksorjacksor-wagtailsite")
origin = repo.remote(name="origin")

# @require_POST # This didn't work for some reason, but OK!
@csrf_exempt
def webhook_update(request):
    print("********************************")
    print("********************************")
    print("********************************")
    print(f"{request.headers=}")
    if not "X-Hub-Signature" in request.headers:
        return HttpResponse("<h1>NO! - X-Hub-Signature</h1>")

    signature = request.headers["X-Hub-Signature"]
    print(f"{signature=}")
    # create the hex digest and append prefix to match the GitHub request format
    digest = "sha1=" + os.getenv("SECRET_TOKEN_FULL")  #
    print(f"{digest=}")
    if not hmac.compare_digest(digest, signature):
        return HttpResponse("<h1>NO! - compare digest</h1>")
    print("*****AUTHDONE*******************")
    print("********************************")
    # run_list_of_commands("git pull", ("origin.pull()", 'subprocess.run(["git", "status"])'))
    # run_list_of_commands("restart server", (subprocess.run(["touch", "/var/www/www_jacksorjacksor_xyz_wsgi.py"])))

    print("Done!")

    return HttpResponse("<h1>HI!</h1>")  # probably should have something else here...
