import argparse
import git
from fabric import Connection

"""
This script works on both the LOCAL and REMOTE computers to synchronise git repos & static files
LOCAL: runs git add/commit/push
REMOTE: runs git pull & python manage.py collectstatic & requirements
"""

parser = argparse.ArgumentParser()
parser.add_argument("-l", "--local", help="only runs the code locally, not remotely", action="store_true")
parser.add_argument("-r", "--remote", help="only runs the code remotely, not locally", action="store_true")
args = parser.parse_args()

if args.local:
    print("LOCAL")
    # Adds, commits and pushes to named repo:
    repo = git.Repo("~/wagtail/jacksorjacksor-wagtailsite")
    repo.git.add(all=True)
    commit_message = input("Commit message: ")
    repo.git.commit("-m", commit_message)
    origin = repo.remote(name="origin")
    origin.push()

if args.remote:
    print("REMOTE")
    # Remotely request the collectstatic (will this interfere with the git pull?)
    result = Connection("jacksorjacksor@ssh.eu.pythonanywhere.com").run(
        "workon wagtail && cd jacksorjacksor-wagtailsite && git pull && python manage.py collectstatic --noinput && pip install -r requirements.txt"
    )
