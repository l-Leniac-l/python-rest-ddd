#!/bin/sh

tar -xzvf /seed/seed.sql.tar.gz -C /seed
mysql -u root -p$MYSQL_ROOT_PASSWORD -h mysql $MYSQL_DATABASE < /seed/seed.sql
rm /seed/seed.sql
