from flask import Flask, jsonify, request
from flask_cors import CORS
import math

# Importing files that I made:
from data import *

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

# This route will handle the bar chart graphs. 
@app.route('/getDataBasedOnFilters', methods=['GET', 'POST'])
def getDataBasedOnFilters():
  if request.method == 'POST':
    data_dictionary = {}
    get_data_object = ExamineData()
    post_data = request.get_json()
    top_nations = get_data_object.top_nations_data(post_data['numberOfStates'], post_data['firstDate'], post_data['lastDate'])
    data_dictionary['top_nations'] = top_nations
    bins_for_age_graph = get_data_object.deaths_by_age(post_data['numberOfBins'], post_data['firstDate'], post_data['lastDate'])
    data_dictionary['bins_for_age_graph'] = bins_for_age_graph
    top_Causes_of_death = get_data_object.top_causes_of_death(post_data['numberOfCausesOfDeath'], post_data['firstDate'], post_data['lastDate'])
    data_dictionary['top_Causes_of_death'] = top_Causes_of_death
    return jsonify(data_dictionary)


@app.route('/getDataForDrillDownGraphs', methods=['GET', 'POST'])
def getDataForDrillDownGraphs():
    if request.method == 'POST':
      get_data_object = ExamineData()
      post_data = request.get_json()
      # print(post_data)
      if post_data.get('state'):
        drilldown_data = get_data_object.drilldown_states_graph(post_data['state'], post_data['startDate'], post_data['endDate'])
      elif post_data.get('ageGroup'):
        drilldown_data = get_data_object.drilldown_deaths_by_age_graph(post_data['ageGroup'], post_data['startDate'], post_data['endDate'])
      elif post_data.get('expedition'):
        drilldown_data = get_data_object.drilldown_expedition_graph(post_data['expedition'], post_data['startDate'], post_data['endDate'])
      elif post_data.get('cause_of_death'):
        drilldown_data = get_data_object.drilldown_top_causes_of_death_graph(post_data['cause_of_death'], post_data['startDate'], post_data['endDate'])
      print(drilldown_data)
      return jsonify(drilldown_data) 

if __name__ == '__main__':
  app.run(debug=True)