FROM python:3.8-alpine3.14

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# WAITER
ENV WAIT_VERSION 2.7.2
ADD https://github.com/ufoscout/docker-compose-wait/releases/download/$WAIT_VERSION/wait /wait
RUN chmod +x /wait


# Django
COPY ./dj_app /app/

RUN pip install --upgrade pip \
    && pip install -r app/requirements.txt \
    $$ pip install daphne

WORKDIR /app/
