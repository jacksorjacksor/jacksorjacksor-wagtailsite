import git
import subprocess


# Adds, commits and pushes to named repo:
repo = git.Repo("~/wagtail/jacksorjacksor-wagtailsite")
repo.git.add(all=True)
commit_message = input("Commit message: ")
repo.git.commit("-m", commit_message)
origin = repo.remote(name="origin")
origin.push()


# def database_update():
#     psql_command = "pg_dump --host=localhost --port=5433 --username=jacksorjacksor --format=tar --file=database_dump.tar dbname=jacksorjacksor"
#     psql_command_as_list = psql_command.split(" ")
#     subprocess.run(psql_command_as_list)


# Makes copy of Database as a directory file (password in .pgaccess)
# database_update()
# - No longer doing this as would wipe out any form data! Whoops!
