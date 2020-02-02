from app.celery_tasks import simple_loop


def get(n):
    simple_loop.delay(n)
    return f"You said {n}", 200
