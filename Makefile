build:
	docker-compose build

server:
	docker-compose up

stop:
	docker-compose down

backup:
	docker-compose run --rm \
		mysql_backup \
		/scripts/startup.sh backup
