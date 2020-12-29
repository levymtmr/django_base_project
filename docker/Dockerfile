FROM python:3.8-alpine AS django-dev

ENV PYTHONUNBUFFERED 1

COPY . /opt/app
RUN pip install -U pip \
    && pip install pipenv \
    && cd /opt/app \
    && pipenv install --system --deploy --dev

WORKDIR /opt/app/src