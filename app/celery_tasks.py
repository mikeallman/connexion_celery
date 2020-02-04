import time

from app.server import celery_app, mongo_db


@celery_app.task(name='simple_loop')
def simple_loop(amount: int, job_uuid: str) -> None:

    start = time.time()

    mongo_db.statuses.update_one(
        {"_id": job_uuid},
        {"$set": {"status": "Running"}}
    )

    sum_of_i = 0
    for i in range(amount):
        print(f"job {job_uuid} here, i is {i}")
        time.sleep(2)
        sum_of_i += i

    elapsed = time.time() - start

    mongo_db.statuses.update_one(
        {"_id": job_uuid},
        {"$set": {
            "status": "Complete",
            "sum": sum_of_i,
            "elapsed_seconds": round(elapsed)
        }}
    )

    print(f"job {job_uuid} finished, elapsed time {elapsed}")
