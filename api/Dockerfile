FROM alpine:latest

WORKDIR /api

EXPOSE 4000

RUN apk update && apk add python3 && apk add py3-pip

RUN  pip3 install flask && pip3 install flask-cors 

RUN pip3 install mysql-connector-python

COPY . .

CMD ["python3", "api.py"]
