server:
	docker-compose up

stop:
	docker-compose down

backup:
	docker run --rm \
		--volumes-from falcon_mysql \
		-v $(shell pwd)/mysql:/backup \
		-e DBUSER=root \
		-e DATABASES="falcon" \
		-e DBPASS=ckBuZG9tcDRzc3dvcmQK \
		-e BACKUP_NAME=db_backup \
		thomass/mysqldump backup
