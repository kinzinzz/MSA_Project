FROM python:3.11.2-alpine3.17

ENV PYTHONUNBUFFERED 1
COPY . /app
WORKDIR /app
COPY ./requirements.txt /requirements.txt

RUN apk add --update --no-cache postgresql-client build-base postgresql-dev \
    musl-dev zlib zlib-dev linux-headers

RUN pip install -r requirements.txt


CMD python manage.py runserver 0.0.0.0:8000