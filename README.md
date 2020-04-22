# 190470973-Chengyang Duan-ECS781p Cloud computing-miniproject

## Rick and Morty API
This application is developed in Python and Flask, inluding the GET, POST, PUT and DELETE to achieve CRUD operating.

1. This application provides a dynamically generated REST API. The API have a sufficient set of services for the selected application domain. The REST API responses conform to REST standards.
2. This application makes use of an external REST service to complement its functionality.
3. This application uses a cloud database for accessing persistent information.
4. This application code is well documented.

## 1. REST API Requests
### **@app.route('/', methods =['GET'])**
1. Extract data from Rick and Morty API(https://rickandmortyapi.com/api/character/)
2. Store all the data into Cassandra Database and show all charactors

### **@app.route('/createacharactor',  methods=['POST'])**
1. Determine whether the character already exists according to the attribute name
2. Create a charactor

### **@app.route('/readacharactor/<name>',  methods=['GET'])**
1. Read a charactor
  
### **@app.route('/updateacharactor',  methods=['PUT'])**
1. Determine whether the character exists according to the attribute name
2. Update a charactor

### **@app.route('/deleteacharactor',  methods=['DELETE'])**
1. Determine whether the character exists according to the attribute name
2. Delete a charactor

## 2. Deploying Cassandra in Docker
### Pull the Cassandra Docker Image:
```
  sudo apt update
  sudo apt install docker.io
  sudo docker pull cassandra:latest
````
### Run a Cassandra instance in Docker:
```
  sudo docker run --name cassandra-instance -p 9042:9042 -d cassandra:latest
```
### Interact with Cassandra via cqlsh using CQL:
```
  sudo docker exec -it cassandra-instance cqlsh
```
### Start Database:
```
  sudo docker start cassandra-instance
```
### Create a keyspace via Cassandra terminal:
```
  CREATE KEYSPACE rm WITH REPLICATION = {'class' : 'SimpleStrategy', 'replication_factor' : 1};
```
### Create a table inside of the keyspace:
```
  CREATE TABLE rm.charactors (rm_name text, rm_status text, rm_species text, rm_type text, rm_gender text, PRIMARY KEY (rm_name)) ;
````

## 3. Serving the application over https
### Creat requirments.txt
```
  pip
  Flask
  cassandra-driver
  requests
  requests_cache
```
### Create the Dockerfile
```
  FROM python:3.7-alpine
  WORKDIR /myapp
  COPY . /myapp
  RUN pip install -U -r requirements.txt
  EXPOSE 8080
  CMD ["python","app.py"]
```
### Bulit imgae and run
```
  cd rm
  sudo docker build . --tag=rm:v4
  sudo docker run -p 8080:8080 rm:v4
```
    
