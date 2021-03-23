FROM python:3.9-slim-buster

RUN pip install fastapi uvicorn pymongo motor requests

EXPOSE 8080

ADD ./app /app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]