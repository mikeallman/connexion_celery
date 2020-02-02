A simple REST API executing background tasks on a distributed task queue.

Rest API built using [connexion](https://pypi.org/project/connexion/)
Distributed task queue implemented with [celery](https://pypi.org/project/celery/), using [rabbitmq](https://www.rabbitmq.com/) as its message broker.

Instructions:

- Run `make build` to build the docker image for our connexion/celery app.
- Run `make run` to start a docker-compose application, running rabbitmq, the web app, and a set of four celery workers.
- Hit the `go/{n}` endpoint to kick things off, with something like `curl http://0.0.0.0:8080/go/1`

Requirements:

- pipenv
- docker / docker-compose
- gnu make
