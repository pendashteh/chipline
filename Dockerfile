FROM ubuntu:latest

RUN apt update
RUN apt install python3 python3-pip -y

RUN apt install -y rlwrap

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt

CMD ["/app/console"]

