FROM python:3.7-buster

WORKDIR /
COPY app /app

RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install -r requirements.txt

CMD ["gunicorn", "-c", "/app/gunicorn.config.py", "app.server:flask_app"]
