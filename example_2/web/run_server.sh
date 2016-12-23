#!/bin/bash

docker run -it -p 80:80 -v "$(pwd)":/code \
    --name flaskdemo \
    --restart=always \
    wtjones/flaskdemo python3 app.py
