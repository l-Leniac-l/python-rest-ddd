#!/bin/sh

mongodump --gzip --db $MONGODB_DATABASE --host mongo --port 27017 --out /backup
