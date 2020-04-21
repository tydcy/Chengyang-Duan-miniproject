# 190470973-Chengyang Duan-ecs781p Cloud computing-miniproject

## Rick and Morty API
This application is developed in Python and Flask, inluding the GET, POST, PUT and delete to achieve CRUD operating.

1. This application provides a dynamically generated REST API. The API have a sufficient set of services for the selected application domain. The REST API responses conform to REST standards.
2. This application makes use of an external REST service to complement its functionality.
3. This application uses a cloud database for accessing persistent information.
4. This application code is well documented.

## 1. REST API Requests
**@app.route('/', methods =['GET'])**
1. extract data from Rick and Morty API(https://rickandmortyapi.com/api/character/)
2. store all the data into Cassandra Database and show all charactors
