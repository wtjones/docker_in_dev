#!/bin/bash

docker run -d -p 80:80 -v "$(pwd)":/code \
    --name flaskdemo \
    wtjones/flaskdemo flask run --host=0.0.0.0 --port 80
