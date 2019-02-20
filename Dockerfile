FROM python:3.6

MAINTAINER PeterPan

COPY ./files /opt/FlaskServer/

ENV MYSQL_HOST=
ENV MYSQL_USER=
ENV MYSQL_PASSWORD=
ENV MYSQL_PORT=3306
ENV MYSQL_DB_NAME=
ENV MYSQL_TABLE_NAME=
ENV SERVICE_KEYS=

RUN pip install --no-cache pymysql Flask\
  &&chmod 777 /opt/FlaskServer/start.sh

Entrypoint ./opt/FlaskServer/start.sh

EXPOSE 5000
