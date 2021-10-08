FROM python:3.9

#ARG project_directory
#WORKDIR $project_directory

RUN apt update && \
apt install -y  mariadb-client fish 

RUN pip install flask pymysql python-dotenv

EXPOSE 80