build:
	docker-compose build

server:
	docker-compose up

stop:
	docker-compose down

mysql_backup:
	docker-compose run --rm \
		mysql_backup \
		/scripts/startup.sh backup

mongo_backup:
	docker-compose run --rm \
		mongo_backup \
		/scripts/startup.sh backup
