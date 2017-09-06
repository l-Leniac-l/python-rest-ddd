server: export APP_DB_HOST=127.0.0.1
	export APP_DB_PORT=3306
	export APP_DB_USER=root
	export APP_DB_PASSWORD=123456
	export APP_DB_DATABASE=falcon
server:
	gunicorn -b localhost:5000 --reload application:app
