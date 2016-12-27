FROM alpine:edge

RUN apk add --no-cache bash python3
RUN pip3 install --upgrade pip \
	&& pip3 install redis \
	&& pip3 install celery[redis]

RUN mkdir /code

WORKDIR /code
ADD * /code/


