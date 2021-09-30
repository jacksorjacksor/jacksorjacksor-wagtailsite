import subprocess

# Database dump:
psql_command = (
    "pg_dump --host=localhost --port=5433 --username=jacksorjacksor --format=t --file=dump dbname=jacksorjacksor"
)

psql_command_as_list = psql_command.split(" ")

subprocess.run(psql_command_as_list)
