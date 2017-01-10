#!/bin/bash

docker run --rm -it -p 80:80 -v "$(pwd)":/code \
    --name flaskdemo \
    wtjones/flaskdemo flask run --host=0.0.0.0 --port 80
