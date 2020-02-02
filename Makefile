all: build run

build:
	pipenv lock -r > requirements.txt
	docker build . -t local/celery_application:latest
	rm requirements.txt

run:
	docker-compose up --scale celery_worker=4
