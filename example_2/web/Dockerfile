FROM alpine:edge

RUN apk add --no-cache bash python3
RUN pip3 install --upgrade pip \
	&& pip3 install flask

RUN mkdir /code

WORKDIR /code
ADD * /code/

ENV FLASK_DEBUG 1
ENV FLASK_APP app.py

EXPOSE 80
