from flask import Flask, render_template, request, jsonify
import json
from cassandra.cluster import Cluster
import requests
import requests_cache

cluster = Cluster(contact_points=['172.17.0.2'],port=9042)
session = cluster.connect()
requests_cache.install_cache('rm_cache', backend='sqlite', expire_after=36000)
app = Flask(__name__)

get_all_characters = 'https://rickandmortyapi.com/api/character/'

#store all the data into database and show all charactors
@app.route('/', methods =['GET'])
def showall():
    resp = requests.get(get_all_characters)

    if resp.ok:

        response = resp.json()

        for i in range(0, len(response['results'])):
            results_data = response['results'][i]

            get_name = results_data['name']
            get_status = results_data['status']
            get_species = results_data['species']
            get_type = results_data['type']
            get_gender = results_data['gender']

            # store all the data into the database
            sql = "INSERT INTO rm.charactors(rm_name, rm_status, rm_species, rm_type, rm_gender) VALUES({},{},{},{},{}) "
            sql = sql.format(get_name, get_status, get_species, get_type, get_gender)
            session.execute(sql)

        #show all charactors
        rows = session.execute("""Select * From rm.charactors""")
        result = []
        for r in rows:

            result.append({"name": r.rm_name, "status": r.rm_status, "species": r.rm_species, "type": r.rm_type, "gender": r.rm_gender})

        result = str(result)
        return jsonify(result)
    else:
        print(resp.reason)


#create a charactor
#determine whether the character already exists according to the attribute name
@app.route('/createacharactor',  methods=['POST'])
def create():

    # determine whether the character already exists according to the attribute name
    if not request.json or not 'name' in request.json:
        return jsonify({'error':'wrong input'}),200
    name = request.json['name']
    rows = session.execute("""Select * from rm.charactors WHERE rm_name = '{}'""".format(name))
    result = []
    for r in rows:

        result.append({"name": r.rm_name, "status": r.rm_status, "species": r.rm_species, "type": r.rm_type, "gender": r.rm_gender})

    if len(result) != 0:
        return jsonify({'error': 'The charactor already exists'}), 409

    # create a charactor
    else:
        session.execute( """INSERT INTO rm.charactors(rm_name,rm_status,rm_species,rm_type,rm_gender)\
        VALUES({}, {}, {}, {}, {}, {})""".format(request.json['name'], request.json['status'], request.json['species'], request.json['type'], request.json['gender']))
        return jsonify({'message': 'create successfully'}), 200


#read a charactor
@app.route('/readscharactor/<name>',  methods=['GET'])
def read(name):
    rows = session.execute("""Select * from rm.charactors WHERE rm_name = '{}'""".format(name))
    result = []
    for r in rows:

        result.append({"name": r.rm_name, "status": r.rm_status, "species": r.rm_species, "type": r.rm_type, "gender": r.rm_gender})

    if len(result)==0:
        return jsonify({'error':'The charactor is not found'}),404
    else:
        return jsonify(result),200


#update a charactor
#determine whether the character exists according to the attribute name
@app.route('/updateacharactor',  methods=['PUT'])
def update():

    # determine whether the character exists according to the attribute name
    if not request.json or not 'name' in request.json:
        return jsonify({'error':'wrong input'}),200
    name = request.json['name']
    rows = session.execute("""Select * from rm.charactors WHERE rm_name = '{}'""".format(name))
    result = []
    for r in rows:

        result.append({"name": r.rm_name, "status": r.rm_status, "species": r.rm_species, "type": r.rm_type, "gender": r.rm_gender})

    if len(result) == 0:
        return jsonify({'error': 'The charactor not exists'}), 409

    # update a charactor
    else:
        session.execute("""UPDATE rm.charactors SET rm_name= {}, rm_status= {}, rm_species= {}, rm_type= {},rm_gender= {}\
        WHERE rm_name= '{}'""".format(request.json['name'], request.json['status'], request.json['species'], request.json['type'], request.json['gender']))
        return jsonify({'message': 'update successfully'}), 200


#delete a charactor
#determine whether the character exists according to the attribute name
@app.route('/deleteacharactor',  methods=['DELETE'])
def delete():

    # determine whether the character exists according to the attribute name
    if not request.json or not 'name' in request.json:
        return jsonify({'error':'wrong input'}),200
    name = request.json['name']
    rows = session.execute("""Select * from rm.charactors WHERE rm_name = '{}'""".format(name))
    result = []
    for r in rows:

        result.append({"name": r.rm_name, "status": r.rm_status, "species": r.rm_species, "type": r.rm_type, "gender": r.rm_gender})

    if len(result) == 0:
        return jsonify({'error': 'The charactor not exists'}), 409

    # delete a charactor
    else:
        session.execute("""DELETE FROM rm.charactors WHERE rm_name= '{}'""".format(request.json['name']))
        return jsonify({'message': 'delete successfully'}), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)