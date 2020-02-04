import celery
import connexion
import pymongo


celery_app = celery.Celery(
    broker="amqp://user:pw@rabbit:5672/vhost",
    include="app.celery_tasks"
)

mongo_client = pymongo.MongoClient('mongo', 27017)
mongo_db = mongo_client.counting_app

connexion_app = connexion.App(__name__, specification_dir="./")
connexion_app.add_api("api.yaml")

flask_app = connexion_app.app  # expose underlying app for WSGI

if __name__ == "__main__":
    connexion_app.run(port=8080)
