# image 
FROM python:3

WORKDIR /usr/app

COPY requirements.txt ./

RUN pip isntall --no-cache-dir -r requirements.txt

COPY src /usr/app 
