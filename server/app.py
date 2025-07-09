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
    print(post_data['numberOfStates'])
    top_nations = get_data_object.top_nations_data(int(post_data['numberOfStates']))
    print(top_nations)
    return jsonify(data_dictionary)

if __name__ == '__main__':
  app.run(debug=True)