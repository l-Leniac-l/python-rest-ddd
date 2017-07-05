server:
	gunicorn -b localhost:5000 --reload application:app
