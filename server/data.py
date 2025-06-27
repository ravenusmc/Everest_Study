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
  def top_three_nations_data(self, number_of_nations=3): 
    top_nations = []
    columns = ['Nation', 'Deaths']
    top_nations.append(columns)
    # Group by Nationality and count number of rows (deaths)
    counts = (
        self.data.groupby('Nationality')
        .size()
        .reset_index(name='Death Count')
    )
    # Drop missing or empty Nationality values
    counts = counts[counts['Nationality'].notnull() & (counts['Nationality'] != '')]
    # Sort by Death Count descending and take top 3
    top_three = counts.sort_values(by='Death Count', ascending=False).head(number_of_nations)
    count = 0
    while count <= number_of_nations:
      rows = []
      state = top_three.iloc[count][0]
      deaths = int(top_three.iloc[count][1])
      rows.append(state)
      rows.append(deaths)
      top_nations.append(rows)
      count += 1 
    print(top_nations)
    # [['Nation', 'Deaths'], ['Nepal', 132], ['India', 27], ['Japan', 19]]

  #Histogram of deaths by age 
  def deaths_by_age(self, bin_size=10): 
    # Ensure Age column is numeric (coerce errors to NaN)
    self.data['Age'] = pd.to_numeric(self.data['Age'], errors='coerce')
    # Drop rows where Age is NaN (unknown)
    age_data = self.data.dropna(subset=['Age'])
    # Create bins: from min age to max age, in steps of 'bin_size'
    min_age = int(age_data['Age'].min()) // bin_size * bin_size
    max_age = int(age_data['Age'].max()) // bin_size * bin_size + bin_size
    bins = list(range(min_age, max_age + bin_size, bin_size))
    # Cut the ages into bins
    age_data['Age Group'] = pd.cut(age_data['Age'], bins=bins, right=True)
    # Count how many deaths per bin
    counts = age_data['Age Group'].value_counts().sort_index()
    print(counts)
  
  #deadliest expeditions 
  def deadliest_expeditions(self, number_of_expeditions=3):
    expeditions_list = []
    columns = ['Expeditions', 'Deaths']
    expeditions_list.append(columns)
    # Group by Nationality and count number of rows (deaths)
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
    print(expeditions)
  
  def top_causes_of_death(self, number_of_causes=3):
    cause_of_death_list = []
    columns = ['Cause of Death', 'Deaths']
    expeditions_list.append(columns)
    counts = (
        self.data.groupby('Cause_of_Death')
        .size()
        .reset_index(name='Death Count')
    )
        # Drop missing or empty Nationality values
    counts = counts[counts['Cause_of_Death'].notnull() & (counts['number_of_causes'] != '')]

test_object = ExamineData()
test_object.deadliest_expeditions()