# New airflow docker component 2.2.3 with additional dag in place
Most of the steps are not necessary to follow as everything is already accommodated in the setup. The steps are just necessary ones to avail airflow with docker from scratch
## Check the memory : required more than 4GB of space
```sh 
docker run --rm "debian:buster-slim" bash -c 'numfmt --to iec $(echo $(($(getconf _PHYS_PAGES) * $(getconf PAGE_SIZE))))'
```

## Fetch docker compose yaml
```sh
curl -LfO 'https://airflow.apache.org/docs/apache-airflow/2.2.3/docker-compose.yaml' 
```
## Use for powershell:
```cmd
Invoke-WebRequest https://airflow.apache.org/docs/apache-airflow/2.2.3/docker-compose.yaml -OutFile docker/docker-compose.yaml
```
## Create a .env file where docker-compose exists. Keep the following configurations inside
```config
AIRFLOW_UID=501
AIRFLOW_GID=0
```
## Start the service : Initialize db and then run all services, 
```sh
docker-compose up airflow-init 
docker-compose up
docker-conpose down --rmi all
```
### Some helpful links
#### Link for webserver :: http://localhost:8080
#### Link for celery flower :: http://localhost:5555
#### Ref :: http://www.marknagelberg.com/getting-started-with-airflow-using-docker/

Look for "simple dag example" DAG to run