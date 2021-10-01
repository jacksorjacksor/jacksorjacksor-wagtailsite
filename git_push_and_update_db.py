import git
import subprocess

# Makes copy of Database as a directory file (password in .pgaccess)
psql_command = "pg_dump --host=localhost --port=5433 --username=jacksorjacksor --format=directory --file=database_dump dbname=jacksorjacksor"
psql_command_as_list = psql_command.split(" ")
subprocess.run(psql_command_as_list)

# Adds, commits and pushes to named repo:
repo = git.Repo("~/wagtail/jacksorjacksor-wagtailsite")
repo.git.add(all=True)
commit_message = input("Commit message: ")
repo.git.commit("-m", commit_message)
origin = repo.remote(name="origin")
origin.push()  # and now
