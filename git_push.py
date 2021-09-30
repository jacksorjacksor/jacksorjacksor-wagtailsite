import git

## Separate action as we'll need to name the commit, BUT!
# Use psycopg2 to make pg_dump
# Add all

repo = git.Repo(".")
repo.git.add(all=True)

commit_message = input("Commit message:")

repo.git.commit("-m", commit_message)

origin = repo.remote(name="origin")
origin.push()
