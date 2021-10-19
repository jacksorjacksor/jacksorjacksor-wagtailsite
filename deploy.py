import argparse
import git
from fabric import Connection

"""
This script works on both the LOCAL and REMOTE computers to synchronise git repos & static files
LOCAL: runs git add/commit/push
REMOTE: runs git pull & python manage.py collectstatic & requirements
>> python manage.py migrate should work now
"""

# COMMAND LINE SETTINGS
"""
If run from command line:
-l: local only
-r: remote only
-np: doesn't run pip install -r requirements.txt
"""

parser = argparse.ArgumentParser()
parser.add_argument("-l", "--local", help="only runs the code locally, not remotely", action="store_true")
parser.add_argument("-r", "--remote", help="only runs the code remotely, not locally", action="store_true")
parser.add_argument("-np", "--nopip", help="doesn't run 'pip install -r requirements.txt'", action="store_true")
args = parser.parse_args()

if args.local or not args.remote:
    print("LOCAL")
    # Adds, commits and pushes to named repo:
    repo = git.Repo("~/wagtail/jacksorjacksor-wagtailsite")
    repo.git.add(all=True)
    commit_message = input("Commit message: ")
    repo.git.commit("-m", commit_message)
    origin = repo.remote(name="origin")
    origin.push()

if args.remote or not args.local:
    print("REMOTE")
    # GIT PULL
    result = Connection("jacksorjacksor@ssh.eu.pythonanywhere.com").run(
        "workon wagtail && cd jacksorjacksor-wagtailsite && git pull"
    )

    # COLLECT STATIC (needed for any CSS change)
    result = Connection("jacksorjacksor@ssh.eu.pythonanywhere.com").run(
        "workon wagtail && cd jacksorjacksor-wagtailsite && python manage.py collectstatic --noinput"
    )

    # PIP INSTALL -R REQUIREMENTS
    if not args.nopip:
        result = Connection("jacksorjacksor@ssh.eu.pythonanywhere.com").run(
            "workon wagtail && cd jacksorjacksor-wagtailsite && pip install -r requirements.txt"
        )

    # PYTHON MANAGE.PY MIGRATE
    result = Connection("jacksorjacksor@ssh.eu.pythonanywhere.com").run(
        "workon wagtail && cd jacksorjacksor-wagtailsite && python manage.py migrate"
    )

    # TOUCH WSGI (restarts the server)
    result = Connection("jacksorjacksor@ssh.eu.pythonanywhere.com").run("touch /var/www/www_jacksorjacksor_xyz_wsgi.py")
