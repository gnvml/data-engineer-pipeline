# Data engineer pipeline using MongoDB with Spark and FastAPI

This repository showcases how to leverage MongoDB data in your FastAPI via the MongoDB Spark Connector and PySpark.  We will load factory data contains product information from MongoDB, create a Microservice to get K latest values which order by as fail_rate desc. This repository has the following components:
- Docker files

The Docker files will spin up the following environment:

![Image of docker environment](https://github.com/gnvml/data-engineer-pipeline/blob/master/images/architecture.png)

## Getting the environment up and running

Execute the `run.sh` script file.  This runs the docker compose file which creates a three node MongoDB cluster, configures it as a replica set on prt 27017. 
- Spark is also deployed in this environment with a master node located at port 8080 and two worker nodes listening on ports 8081 and 8082 respectively.
- FastAPI is also deployed in this environment located at port 80.
- The MongoDB cluster will be used for both reading data into Spark and writing data from Spark back into MongoDB.

Note: You may have to mark the .SH file as runnable with the `chmod` command i.e. `chmod +x run.sh`


To verify our components online navigate to:
- Rest API - http://localhost:80/docs
- Spark Master - http://localhost:8080
- Spark Worker 1 - http://localhost:8081
- Spark Worker 2 - http://localhost:8082
- MongoDB Replica Set - port 27017-27019

## For running

Linux/Ubuntu

```
bash run.sh
```

MacOS

```
sh run.sh
```

## Data format
```
{
        "factory_id": 23871,
        "org_id": 2345,
        "country": "VN", 
        "execution_date": "2022-05-01", 
        "fail_rate": "0.5",
        "defect_rate": "0.2"
}

```

## CRUD Example
There are two ways to test the Microservice

1. Using UI: Navigate to http://localhost:80/docs and using UI to query
2. Using command line:

```
#POST METHOD
curl -X POST "http://localhost:80/request_record" -H "accept: text/plain" -H "Content-Type: application/json" -d '{"number_record":100}'

#GET METHOD
curl "http://localhost:80/get_record/100"
```


## Note
- The FastAPI image will be create after the first time run the run.sh file
- If you have trouble with port serving, please change port in docker-compose.yml file
- The data is randomly generate with 'execution_date' and 'fail_rate'
- If you want more computing, please the config of resource on Spark in docker-compose.yml

