# syntax=docker/dockerfile:1.4
FROM python:slim

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
RUN pip install gunicorn

COPY app app
COPY riftboundfaq.py boot.sh ./
RUN chmod a+x boot.sh

ENV FLASK_APP riftboundfaq.py

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]