FROM python:3.9

#ARG project_directory
#WORKDIR $project_directory

RUN apt update && \
apt install -y  mariadb-client fish 

RUN pip install flask pymysql python-dotenv

WORKDIR /tmp
COPY ./app.py /tmp/
COPY ./.env /tmp

# RUN python3 app.py

EXPOSE 80