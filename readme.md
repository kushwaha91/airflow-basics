# check the memory
docker run --rm "debian:buster-slim" bash -c 'numfmt --to iec $(echo $(($(getconf _PHYS_PAGES) * $(getconf PAGE_SIZE))))'

# fetch docker compose yaml
curl -LfO 'https://airflow.apache.org/docs/apache-airflow/2.2.3/docker-compose.yaml'

# use for powershell:
Invoke-WebRequest https://airflow.apache.org/docs/apache-airflow/2.2.3/docker-compose.yaml -OutFile docker/docker-compose.yaml


chmod -R 777 logs

# start the service : Initialize db and then run all services 
docker-compose up airflow-init 
docker-compose up

# use the following vloumes to avoid the access denied issues
    - ./dags:/usr/local/airflow/dags
    - ./logs:/usr/local/airflow/logs
    - ./plugins:/usr/local/airflow/plugins