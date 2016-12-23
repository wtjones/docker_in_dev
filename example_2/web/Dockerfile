FROM alpine:edge

RUN apk add --no-cache bash python3 \
	&& pip3 install --upgrade pip \
	&& pip3 install flask

RUN mkdir /code

WORKDIR /code
ADD * /code/

EXPOSE 80

