#!/bin/sh

mongorestore --gzip --host mongo --port 27017 /backup
