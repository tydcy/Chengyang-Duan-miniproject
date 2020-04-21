from flask import Flask, request, jsonify, render_template, redirect
from werkzeug.security import generate_password_hash
from cassandra.cluster import Cluster
from io import BytesIO
import re
import urllib.request
import json
import requests
import os

cluster = Cluster(contact_points=['127.0.0.1'], port=9042)
session = cluster.connect()

app = Flask(__name__)


@app.route('/', methods=['GET'])
def welcome():

    covid_url_summary = 'https://rickandmortyapi.com/api/character/'
    resp = requests.get(covid_url_summary)

    if resp.ok:
        response = resp.json()

        # extracting the relevant variables from the json
        for i in range(0, len(response['results'])):

            results_data = response['results'][i]

            c_id = results_data['id']
            c_name = results_data['name']
            c_status = results_data['status']
            c_species = results_data['species']
            c_type = results_data['type']
            c_gender = results_data['gender']

            # storing the data into the sql table
            sql = "INSERT INTO RM(c_id, c_name, c_status, c_species,c_type,c_gender) VALUES({},{},{},{},{},{}) "
            sql = sql.format(c_id, c_name, c_status, c_species, c_type, c_gender)
            session.execute(sql)


    return render_template('welcome.html'), 200

@app.route('/search', methods=['GET'])
def search():
    f_id = request.form['f_id']
    result = session.execute(
        """SELECT * FROM RM WHERE c_id='{}'""".format(f_id))
    return jsonify(result)
	
if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000)
