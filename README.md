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

### **@app.route('/readscharactor/<name>',  methods=['GET'])**
1. Read a charactor
  
### **@app.route('/updateacharactor',  methods=['PUT'])**
1. Determine whether the character exists according to the attribute name
2. Update a charactor

### **@app.route('/deleteacharactor',  methods=['DELETE'])**
1. Determine whether the character exists according to the attribute name
2. Delete a charactor

## 2. Deploying Cassandra in Docker
###Pull the Cassandra Docker Image:
```
  sudo apt update
  sudo apt install docker.io
  sudo docker pull cassandra:latest
````
