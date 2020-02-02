import time

from app.server import celery_app


@celery_app.task(name='simple_loop')
def simple_loop(n):
    start = time.time()
    for i in range(10):
        print(f"worker {n} here, i is {i}")
        time.sleep(2)
    elapsed = time.time() - start
    print(f"worker {n} finished, elapsed time {elapsed}")
