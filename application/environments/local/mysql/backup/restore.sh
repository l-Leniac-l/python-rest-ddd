#!/bin/sh

tar -xzvf /backup/backup.sql.tar.gz
mysql -u root -p$MYSQL_ROOT_PASSWORD -h mysql $MYSQL_DATABASE < /backup/backup.sql
rm /backup/backup.sql
