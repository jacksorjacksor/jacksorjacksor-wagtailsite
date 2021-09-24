https://help.pythonanywhere.com/pages/RegularPostgresBackups/

Dump: Template
`` pg_dump --host=HOSTNAME --port=PORT --username=super --format=c --file=pgbackup`date +%F-%H%M`.dump mydb ``

Dump: Local
`` pg_dump --host=127.0.0.1 --port=5433 --username=jacksorjacksor --format=c --file=pgbackup`date +%F-%H%M`.dump jacksorjacksor ``

PA: restore
pg-restore --host=jacksorjacksor --port=10119 --username=jacksorjacksor --format=c --file=pg_jacksorjacksor.dump jacksorjacksor

pg_restore --host=jacksorjacksor --port=10119 --username=jacksorjacksor --format=c --file=pg_jacksorjacksor.dump
