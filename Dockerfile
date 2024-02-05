FROM python:3.10

WORKDIR /app

COPY requirements.txt /app/

RUN pip install -r requirements.txt

COPY ./src /app/

#Exposing port 5000 from the container
EXPOSE 5000
#Starting the Python application

WORKDIR /app/api

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "server:app"]