# image 
FROM python:3

WORKDIR /app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

# COPY app /usr/app

# start the server
# CMD flask run -h 0.0.0.0 
