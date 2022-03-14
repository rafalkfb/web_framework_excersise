sudo service docker start &&
docker-compose up -d	&&
docker-compose run mypython pytest --alluredir=results tests_cases/test_suite_demo.py --browser docker-remote