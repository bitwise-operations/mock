FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9-slim

WORKDIR /app

ADD ./ /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    python3-dev gcc libssl-dev default-libmysqlclient-dev && \
    pip install --upgrade pip && \
    pip install --upgrade -r ./requirements.txt
