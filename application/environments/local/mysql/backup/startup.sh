#!/bin/sh
if [ "$1" = "backup" ]; then
  /scripts/backup.sh
elif [ "$1" = "restore" ]; then
  /scripts/restore.sh
else echo "Call with 'backup' or 'restore' $1"
fi
