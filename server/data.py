#Main file to examine the CSV data. 

# importing supporting libraries
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

class ExamineData():
    
  def __init__(self):
    self.data = pd.read_csv('./data/everest_deaths.csv')
  
  #Top 3 nationalies
  def top_three_nations_data(self): 
    top_three_nations = []
    columns = ['Nation', 'Deaths']
    top_three_nations.append(columns)
    # Group by Nationality and count number of rows (deaths)
    counts = (
        self.data.groupby('Nationality')
        .size()
        .reset_index(name='Death Count')
    )
    # Drop missing or empty Nationality values
    counts = counts[counts['Nationality'].notnull() & (counts['Nationality'] != '')]
    # Sort by Death Count descending and take top 3
    top_three = counts.sort_values(by='Death Count', ascending=False).head(3)
    count = 0
    while count <= 2:
      rows = []
      state = top_three.iloc[count][0]
      deaths = int(top_three.iloc[count][1])
      rows.append(state)
      rows.append(deaths)
      top_three_nations.append(rows)
      count += 1 
    print(top_three_nations)

test_object = ExamineData()
test_object.top_three_nations_data()