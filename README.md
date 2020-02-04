A simple REST API executing background tasks on a distributed task queue.

Rest API built using [connexion](https://pypi.org/project/connexion/)
Distributed task queue implemented with [celery](https://pypi.org/project/celery/), using [rabbitmq](https://www.rabbitmq.com/) as its message broker.
Also using MongoDB as our state store.

Instructions:

- Run `make build` to build the docker image for our connexion/celery app.
- Run `make run` to start a docker-compose application, running rabbitmq, mongodb, the web app, and a set of four celery workers.
- Post to the count endpoint to kick off a backgroud task, counting to the number specified in the request body:

```
$ curl --request POST --header "content-type:application/json" --data '{"count_amount": 30}' "http://0.0.0.0:8080/count"                                                                                                                ✔
{
  "job_uuid": "4f143940-b476-41e8-a5ad-c15d64ddf071"
} 
```
- get the /count/{job_uuid} endpoint to get job status:
```
$ curl http://0.0.0.0:8080/count/4f143940-b476-41e8-a5ad-c15d64ddf071                                                                                                                                                                   ✔
{
  "count_amount": 30,
  "elapsed_seconds": null,
  "job_uuid": "4f143940-b476-41e8-a5ad-c15d64ddf071",
  "status": "Running",
  "sum": null
}
``` 

Requirements:

- pipenv
- docker / docker-compose
- gnu make
