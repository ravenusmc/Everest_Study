from flask import Flask, jsonify, request
from flask_cors import CORS

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
    print(post_data)
    top_nations = get_data_object.top_nations_data(post_data['numberOfStates'])
    data_dictionary['top_nations'] = top_nations
    bins_for_age_graph = get_data_object.deaths_by_age(post_data['numberOfBins'])
    data_dictionary['bins_for_age_graph'] = bins_for_age_graph
    print(bins_for_age_graph)
    return jsonify(data_dictionary)

if __name__ == '__main__':
  app.run(debug=True)