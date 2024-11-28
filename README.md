 SaaS application for tracking freelancer billable hours and generating invoices.



***
### Project Build
- To start the required containers and run the directly on the docker env use the following commands;
```bash
docker-compose -f local/docker-compose.yml -p time-tracker build
docker-compose -f local/docker-compose.yml -p time-tracker up -d
```
or if you want to work on your local computer, check the below section.
### Project Build For Working in Local Computer
- Change directory to /Local 
```bash
cd local
```
- To start containers with a specific name and run the app
```bash
docker-compose -p time-tracker up -d
```
- Then you can simply run the below command to work on the local environment while the dependencies are installed and working in the Docker.
```bash
.venv/bin/uvicorn app:app --reload
```
- To stop and remove containers
```bash
docker-compose -p time-tracker down
```


