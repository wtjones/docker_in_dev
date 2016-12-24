#!/bin/bash

docker run -d -p 80:80 -v "$(pwd)":/code \
    --name flaskdemo \
    --restart=always \
    wtjones/flaskdemo python3 app.py
