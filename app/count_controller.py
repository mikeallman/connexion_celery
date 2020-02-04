import connexion
from typing import Tuple, Dict
from uuid import uuid4

from app.celery_tasks import simple_loop
from app.server import mongo_db


def get(job_uuid: str) -> Tuple[Dict, int]:

    job = mongo_db.statuses.find_one({
        "_id": job_uuid
    })

    if not job:
        response = {
            "job_uuid": job_uuid,
            "status": "Not Found",
            "count_amount": None,
            "sum": None,
            "elapsed_seconds": None
        }
        return response, 404

    response = {
        "job_uuid": job.get("_id"),
        "status": job.get("status"),
        "count_amount": job.get("count_amount"),
        "sum": job.get("sum"),
        "elapsed_seconds": job.get("elapsed_seconds")
    }
    return response, 200


def post() -> Tuple[Dict, int]:

    count_amount = connexion.request.json.get('count_amount')
    job_uuid = str(uuid4())

    mongo_db.statuses.insert_one({
        "_id": job_uuid,
        "status": "Queued",
        "count_amount": count_amount,
        "sum": None,
        "elapsed_seconds": None
    })

    simple_loop.delay(count_amount, job_uuid)

    response = {'job_uuid': job_uuid}
    return response, 202
