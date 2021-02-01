FROM python:3.8-alpine
MAINTAINER Rafael S. M. Ferreira
COPY ./airflow/ /var/airflow/
ENV PORT=8080
RUN python -m pip install --upgrade pip
RUN pip install apache-airflow
WORKDIR /var/airflow/
ENTRYPOINT python dag.py
EXPOSE $PORT