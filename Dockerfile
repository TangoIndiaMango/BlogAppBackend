FROM python:3.9

RUN mkdir /blogsite

WORKDIR /blogsite

COPY . /blogsite/

RUN pip install -r requirements.txt
