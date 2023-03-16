# pull the official base image
FROM ubuntu:20.04

# set work directory
WORKDIR /usr/src/app

# install dependencies
RUN apt-get update
RUN apt-get install python3 -y
RUN apt-get install python3-pip -y
RUN pip install --upgrade pip 
COPY ./requirements.txt /usr/src/app
RUN pip install -r requirements.txt

# copy project
COPY . /usr/src/app

# build up application
# RUN python3 manage.py makemigrations
# RUN python3 manage.py migrate
EXPOSE 8002

# run application
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8002"]