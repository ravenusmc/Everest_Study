from flask import Flask, jsonify, request
from flask_cors import CORS
import math

# Importing files that I made:
from data import *
from db import *

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

# Some of the graphs will need the data grabbed as soon as the page loads.


@app.route('/getInitialDataForGraphs', methods=['GET'])
def getInitialDataForGraphs():
    if request.method == 'GET':
        data_dictionary = {}
        get_data_object = ExamineData()
        # post_data = request.get_json()
        heat_map_location_cause_of_death_data = get_data_object.heat_map_location_cause_of_death()
        data_dictionary['Heat_Map_Data'] = heat_map_location_cause_of_death_data
        return jsonify(data_dictionary)

# Route to sign up user
@app.route('/signUpUser', methods=['OPTIONS', 'POST'])
def signUpUser():
    if request.method == 'OPTIONS':  # Handle preflight request
        return jsonify({'message': 'Preflight request successful'}), 200
    if request.method == 'POST':
        db_obj = Connection()
        post_data = request.get_json()
        hashed = db_obj.encrypt_pass(post_data)
        db_obj.insert(post_data, hashed)
        return jsonify('5')

#Route to login
@app.route('/login', methods=['OPTIONS', 'POST'])
def login():
    if request.method == 'OPTIONS':  # Handle preflight request
        return jsonify({'message': 'Preflight request successful'}), 200
    if request.method == 'POST':
        db_obj = Connection()
        post_data = request.get_json()
        email = post_data['username']
        password = post_data['password']  
        # # Checking to see if the user is in the database
        login_flag, not_found, password_no_match, user = db_obj.verify_user(
            email, password)
        flags = [login_flag, not_found, password_no_match, user]
        return jsonify('5')

# This route will handle the bar chart graphs.
@app.route('/getDataBasedOnFilters', methods=['GET', 'POST'])
def getDataBasedOnFilters():
    if request.method == 'POST':
        data_dictionary = {}
        get_data_object = ExamineData()
        post_data = request.get_json()
        # deaths by nations
        top_nations = get_data_object.top_nations_data(
            post_data['numberOfStates'], post_data['firstDate'], post_data['lastDate'])
        data_dictionary['top_nations'] = top_nations
        # Deaths by Age
        bins_for_age_graph = get_data_object.deaths_by_age(
            post_data['numberOfBins'], post_data['firstDate'], post_data['lastDate'])
        data_dictionary['bins_for_age_graph'] = bins_for_age_graph
        # Deaths by expedition
        data_for_expeditions = get_data_object.deadliest_expeditions(
            post_data['numberOfExpeditions'], post_data['firstDate'], post_data['lastDate'])
        data_dictionary['data_for_expeditions'] = data_for_expeditions
        # Top causes of death
        top_Causes_of_death = get_data_object.top_causes_of_death(
            post_data['numberOfCausesOfDeath'], post_data['firstDate'], post_data['lastDate'])
        data_dictionary['top_Causes_of_death'] = top_Causes_of_death
        # Deaths by Month
        deaths_by_month = get_data_object.common_months_for_deaths(
            post_data['firstDate'], post_data['lastDate'])
        data_dictionary['deaths_by_month'] = deaths_by_month
        return jsonify(data_dictionary)


@app.route('/getDataForDrillDownGraphs', methods=['GET', 'POST'])
def getDataForDrillDownGraphs():
    if request.method == 'POST':
        get_data_object = ExamineData()
        post_data = request.get_json()
        if post_data.get('state'):
            drilldown_data = get_data_object.drilldown_states_graph(
                post_data['state'], post_data['startDate'], post_data['endDate'])
        elif post_data.get('ageGroup'):
            drilldown_data = get_data_object.drilldown_deaths_by_age_graph(
                post_data['ageGroup'], post_data['startDate'], post_data['endDate'])
        elif post_data.get('expedition'):
            drilldown_data = get_data_object.drilldown_expedition_graph(
                post_data['expedition'], post_data['startDate'], post_data['endDate'])
        elif post_data.get('cause_of_death'):
            drilldown_data = get_data_object.drilldown_top_causes_of_death_graph(
                post_data['cause_of_death'], post_data['startDate'], post_data['endDate'])
        elif post_data.get('month'):
            drilldown_data = get_data_object.common_months_for_death_drilldown(
                post_data['month'], post_data['startDate'], post_data['endDate'])
        # print(drilldown_data)
        return jsonify(drilldown_data)


if __name__ == '__main__':
    app.run(debug=True)
