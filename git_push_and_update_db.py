import git
import subprocess

# Database dump:
psql_command = "pg_dump --host=localhost --port=5433 --username=jacksorjacksor --format=tar --file=database_dump dbname=jacksorjacksor"

psql_command_as_list = psql_command.split(" ")
subprocess.run(psql_command_as_list)

## Separate action as we'll need to name the commit, BUT!
# Use psycopg2 to make pg_dump

repo = git.Repo("~/wagtail/jacksorjacksor-wagtailsite")
repo.git.add(all=True)

commit_message = input("Commit message: ")

repo.git.commit("-m", commit_message)

origin = repo.remote(name="origin")
origin.push()
