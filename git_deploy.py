import git
from fabric import Connection

"""
This script works on both the LOCAL and REMOTE computers to synchronise git repos & static files
LOCAL: runs git add/commit/push
REMOTE: runs git pull & python manage.py collectstatic
"""

print("LOCAL")
# Adds, commits and pushes to named repo:
repo = git.Repo("~/wagtail/jacksorjacksor-wagtailsite")
repo.git.add(all=True)
commit_message = input("Commit message: ")
repo.git.commit("-m", commit_message)
origin = repo.remote(name="origin")
origin.push()

print("REMOTE")
# Remotely request the collectstatic (will this interfere with the git pull?)
result = Connection("jacksorjacksor@ssh.eu.pythonanywhere.com").run(
    "workon wagtail && cd jacksorjacksor-wagtailsite && git pull && python manage.py collectstatic --noinput"
)


# TODO: separate "push DB" function - not automatically though!
