#!/bin/bash

sudo service docker start
source ./env/Scripts/activate
docker-compose up -d	&&
docker-compose run mypython pytest --alluredir=results tests_cases/test_suite_demo.py --browser docker-remote &&
deactivate