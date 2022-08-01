FROM apache/airflow:2.3.3-python3.9
USER airflow
RUN pip install 'pipenv'
RUN pipenv install

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

USER root

#RUN usermod -aG 0 airflow
USER root

#RUN mkdir downloads