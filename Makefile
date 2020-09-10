install:
	pip3 install -r requirements.txt

run:
	FLASK_APP=app FLASK_ENV=development flask run