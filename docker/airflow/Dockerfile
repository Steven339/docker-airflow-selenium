FROM apache/airflow:2.3.3-python3.9
USER airflow
RUN pip install 'apache-airflow[celery]'
RUN pip install 'apache-airflow-providers-apache-spark'
RUN pip install 'apache-airflow-providers-mongo'
RUN pip install 'pymongo'
RUN pip install 'fake_useragent'
RUN pip install 'selenium'
RUN pip install 'beautifulsoup4'
RUN pip install 'docker'
RUN pip install 'lxml'

ARG AIRFLOW_USER_HOME=/opt/airflow
ENV PYTHONPATH=$PYTHONPATH:${AIRFLOW_USER_HOME}

USER root

RUN apt-get update -yqq && \
    apt-get install -y gnupg && \
    apt-get install -y apt-transport-https ca-certificates

RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
RUN curl https://packages.microsoft.com/config/ubuntu/18.04/prod.list > /etc/apt/sources.list.d/mssql-release.list

RUN apt-get update -yqq && \
    apt-get install -y unixodbc unixodbc-dev && \
    ACCEPT_EULA=Y apt-get install -y msodbcsql17 && \
    ACCEPT_EULA=Y apt-get install mssql-tools