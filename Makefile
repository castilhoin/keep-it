install:
	pip3 install -r requirements.txt
	flask create-db

run:
	FLASK_APP=app FLASK_ENV=development flask run