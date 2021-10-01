import git

# Adds, commits and pushes to named repo:
repo = git.Repo("~/wagtail/jacksorjacksor-wagtailsite")
repo.git.add(all=True)
commit_message = input("Commit message: ")
repo.git.commit("-m", commit_message)
origin = repo.remote(name="origin")
origin.push()

# TODO: separate "push DB" function - not automatically though!
