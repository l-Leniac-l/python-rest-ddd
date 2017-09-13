#!/bin/sh

rm /backup/backup.sql.tar.gz
mysqldump -u root -p$MYSQL_ROOT_PASSWORD -h mysql $MYSQL_DATABASE > /backup/backup.sql
tar -czvf /backup/backup.sql.tar.gz /backup/backup.sql
rm /backup/backup.sql
