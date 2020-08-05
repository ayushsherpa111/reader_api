# image 
FROM python:3

WORKDIR /usr/app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY src /usr/app/src

# expose a container port
EXPOSE 5000 

ENV FLASK_APP=src/app.py
ENV FLASK_ENV=development

# start the server
CMD flask run 
