from fabric import Connection

result = Connection("jacksorjacksor@ssh.eu.pythonanywhere.com").run(
    "workon wagtail && cd jacksorjacksor-wagtailsite && python manage.py migrate"
)
