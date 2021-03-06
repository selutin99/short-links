FROM python:3.6

RUN apt-get update
RUN mkdir /app

WORKDIR /app
COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

ENV FLASK_ENV="config.DevelopmentConfig"
ENV POSTGRES_URL="postgres"

EXPOSE 5000