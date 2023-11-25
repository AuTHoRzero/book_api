FROM python:3.12.0-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir /opt/Book-api
WORKDIR /opt/Book-api

COPY ./book_api/ /opt/Book-api/
RUN pip3 install -r requirements.txt --no-cache-dir

COPY ./entrypoint.sh /entrypoint.sh



