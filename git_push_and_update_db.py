import git

# Adds, commits and pushes to named repo:
repo = git.Repo("~/wagtail/jacksorjacksor-wagtailsite")
repo.git.add(all=True)
commit_message = input("Commit message: ")
repo.git.commit("-m", commit_message)
origin = repo.remote(name="origin")
origin.push()


# Remotely request the collectstatic (will this interfere with the git pull?)
from fabric import Connection

result = Connection("jacksorjacksor@ssh.eu.pythonanywhere.com").run(
    "workon wagtail && cd jacksorjacksor-wagtailsite && git pull && python manage.py collectstatic --noinput"
)


# TODO: separate "push DB" function - not automatically though!
