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
  def top_nations_data(self, number_of_nations): 
    top_nations = []
    # Group by Nationality and count number of rows (deaths)
    counts = (
        self.data.groupby('Nationality')
        .size()
        .reset_index(name='Death Count')
    )
    # Drop missing or empty Nationality values
    counts = counts[counts['Nationality'].notnull() & (counts['Nationality'] != '')]
    # Sort by Death Count descending and take top 3
    nations = counts.sort_values(by='Death Count', ascending=False).head(number_of_nations)
    count = 0
    while count < number_of_nations:
      rows = []
      state = nations.iloc[count][0]
      deaths = int(nations.iloc[count][1])
      rows.append(state)
      rows.append(deaths)
      top_nations.append(rows)
      count += 1 
    return top_nations
    # [['Nation', 'Deaths'], ['Nepal', 132], ['India', 27], ['Japan', 19]]

  def drilldown_states_graph(self, selected_state):
    drilldown_data = []
    grouped_data = self.data.groupby('Nationality')

  #Histogram of deaths by age 
  def deaths_by_age(self, bin_size):
      # Ensure Age column is numeric
      self.data['Age'] = pd.to_numeric(self.data['Age'], errors='coerce')
      # Drop rows where Age is NaN
      age_data = self.data.dropna(subset=['Age'])
      # Create bins
      min_age = int(age_data['Age'].min()) // bin_size * bin_size
      max_age = int(age_data['Age'].max()) // bin_size * bin_size + bin_size
      bins = list(range(min_age, max_age + bin_size, bin_size))
      # Create labels like "10-19", "20-29", etc.
      labels = [f"{b}-{b + bin_size - 1}" for b in bins[:-1]]
      # Cut into bins
      age_data['Age Group'] = pd.cut(age_data['Age'], bins=bins, labels=labels, right=True)
      # Count per bin and convert to desired format
      counts = age_data['Age Group'].value_counts().sort_index()
      bins_for_age_graph = [[label, int(counts[label])] for label in labels]
      return bins_for_age_graph

  
  #deadliest expeditions 
  def deadliest_expeditions(self, number_of_expeditions=3):
    expeditions_list = []
    # Group by Nationality
    counts = (
        self.data.groupby('Expedition')
        .size()
        .reset_index(name='Death Count')
    )
    # Drop missing or empty Nationality values
    counts = counts[counts['Expedition'].notnull() & (counts['Expedition'] != '')]
    # Sort by Death Count descending and take top 3
    expeditions = counts.sort_values(by='Death Count', ascending=False).head(number_of_expeditions)
    count = 0
    while count <= number_of_expeditions - 1:
      rows = []
      expedition = expeditions.iloc[count][0]
      deaths = int(expeditions.iloc[count][1])
      rows.append(expedition)
      rows.append(deaths)
      expeditions_list.append(rows)
      count += 1 
    print(expeditions_list)
  
  def top_causes_of_death(self, number_of_causes=3):
    cause_of_death_list = []
    columns = ['Cause of Death', 'Deaths']
    cause_of_death_list.append(columns)
    counts = (
        self.data.groupby('Cause_of_Death')
        .size()
        .reset_index(name='Death Count')
    )
    # Drop missing or empty Nationality values
    counts = counts[counts['Cause_of_Death'].notnull() & (counts['Cause_of_Death'] != '')]
    # Sort by Death Count descending and take top 3
    cause_of_deaths_df = counts.sort_values(by='Death Count', ascending=False).head(number_of_causes)
    count = 0
    while count <= number_of_causes - 1:
      rows = []
      cause_of_death = cause_of_deaths_df.iloc[count][0]
      deaths = int(cause_of_deaths_df.iloc[count][1])
      rows.append(cause_of_death)
      rows.append(deaths)
      cause_of_death_list.append(rows)
      count += 1 
    print(cause_of_death_list)
  
  def common_months_for_deaths(self):
    pass

# test_object = ExamineData()
# test_object.deadliest_expeditions()