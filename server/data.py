#Main file to examine the CSV data. 

# importing supporting libraries
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

class ExamineData():
    
  def __init__(self):
    self.data = pd.read_csv('./data/everest_deaths.csv')
  
  def min_values(self): 
    self.data['Date_clean'] = pd.to_datetime(self.data['Date'].str.extract(r'(\w+ \d{1,2}, \d{4})')[0], errors='coerce')
    min_date = self.data['Date_clean'].min()
    max_date = self.data['Date_clean'].max()
    print(f"Min date: {min_date}") #Min date: 1921-06-05 00:00:00
    print(f"Max date: {max_date}")  #Max date: 2025-05-15 00:00:00
  
  #Top 3 nationalies
  def top_nations_data(self, number_of_nations, startDate, endDate): 
    top_nations = []
    # Clean and parse the Date column (if not already cleaned)
    self.data['Date_clean'] = pd.to_datetime(
        self.data['Date'].str.extract(r'(\w+ \d{1,2}, \d{4})')[0],
        errors='coerce'
    )
    # Convert input start/end dates to datetime
    start_dt = pd.to_datetime(startDate)
    end_dt = pd.to_datetime(endDate)
    # Filter rows by date range
    filtered_data = self.data[
        (self.data['Date_clean'] >= start_dt) & (self.data['Date_clean'] <= end_dt)
    ]
    # Group by Nationality and count number of rows (deaths)
    counts = (
        filtered_data.groupby('Nationality')
        .size()
        .reset_index(name='Death Count')
    )
    # Drop rows with missing or empty nationality values
    counts = counts[counts['Nationality'].notnull() & (counts['Nationality'] != '')]
    # Sort by Death Count descending and take top N
    nations = counts.sort_values(by='Death Count', ascending=False).head(number_of_nations)
    # Convert result to list format
    for _, row in nations.iterrows():
        top_nations.append([row['Nationality'], int(row['Death Count'])])
    print(top_nations)
    return top_nations

  def drilldown_states_graph(self, selected_state, startDate, endDate):
    # Clean and parse the Date column
    self.data['Date_clean'] = pd.to_datetime(
        self.data['Date'].str.extract(r'(\w+ \d{1,2}, \d{4})')[0],
        errors='coerce'
    )
    # Convert input start/end dates to datetime
    start_dt = pd.to_datetime(startDate)
    end_dt = pd.to_datetime(endDate)
    # Filter by state and date range
    filtered_data = self.data[
        (self.data['Date_clean'] >= start_dt) &
        (self.data['Date_clean'] <= end_dt) &
        (self.data['Nationality'] == selected_state) &
        (self.data['Date_clean'].notnull())
    ]
    # Define the columns you want to keep
    selected_columns = [
        'Name', 'Date', 'Age', 'Expedition',
        'Cause_of_Death', 'Location', 'Remains status'
    ]
    filtered = filtered_data[selected_columns]
    # Convert to list of dictionaries and replace NaNs with None
    drilldown_data = filtered.to_dict(orient='records')
    for row in drilldown_data:
        for key in row:
            if pd.isna(row[key]):
                row[key] = None
    return drilldown_data

  #Histogram of deaths by age 
  def deaths_by_age(self, bin_size, startDate, endDate):
    # Clean and parse the Date column
    self.data['Date_clean'] = pd.to_datetime(
        self.data['Date'].str.extract(r'(\w+ \d{1,2}, \d{4})')[0],
        errors='coerce'
    )
    # Convert input start/end dates to datetime
    start_dt = pd.to_datetime(startDate)
    end_dt = pd.to_datetime(endDate)
    # Ensure Age column is numeric
    self.data['Age'] = pd.to_numeric(self.data['Age'], errors='coerce')
    # Filter for both date range AND non-null age
    age_data = self.data[
        (self.data['Date_clean'] >= start_dt) &
        (self.data['Date_clean'] <= end_dt)
    ].dropna(subset=['Age'])
    # Create bins
    min_age = int(age_data['Age'].min()) // bin_size * bin_size
    max_age = int(age_data['Age'].max()) // bin_size * bin_size + bin_size
    bins = list(range(min_age, max_age + bin_size, bin_size))
    labels = [f"{b}-{b + bin_size - 1}" for b in bins[:-1]]
    # Bin ages
    age_data['Age Group'] = pd.cut(age_data['Age'], bins=bins, labels=labels, right=True)
    # Count per bin
    counts = age_data['Age Group'].value_counts().sort_index()
    bins_for_age_graph = [[label, int(counts[label])] for label in labels]
    return bins_for_age_graph
  
  def drilldown_deaths_by_age_graph(self, age_group, startDate, endDate):
    # Clean and parse the Date column
    self.data['Date_clean'] = pd.to_datetime(
        self.data['Date'].str.extract(r'(\w+ \d{1,2}, \d{4})')[0],
        errors='coerce'
    )
    # Convert input start/end dates to datetime
    start_dt = pd.to_datetime(startDate)
    end_dt = pd.to_datetime(endDate)
    # Ensure Age is numeric
    self.data['Age'] = pd.to_numeric(self.data['Age'], errors='coerce')
    # Extract lower and upper bounds
    try:
        lower, upper = map(int, age_group.split('-'))
    except ValueError:
        raise ValueError("age_group must be a string like '40-49'")

    # Filter by state and date range
    filtered_df = self.data[
        (self.data['Date_clean'] >= start_dt) &
        (self.data['Date_clean'] <= end_dt) &
        (self.data['Age'] >= lower) &
        (self.data['Age'] <= upper) &
        (self.data['Date_clean'].notnull())
    ]
    # Select desired columns
    selected_columns = [
        'Name', 'Date', 'Age', 'Expedition',
        'Cause_of_Death', 'Location', 'Remains status'
    ]
    result = filtered_df[selected_columns].copy()
    # Optional: fill missing with 'Unknown'
    result = result.fillna('Unknown')
    # Return as list of dicts for easy use in frontend
    return result.to_dict(orient='records')

  #deadliest expeditions 
  def deadliest_expeditions(self, number_of_expeditions, startDate, endDate):
    # Clean and parse the Date column
    self.data['Date_clean'] = pd.to_datetime(
        self.data['Date'].str.extract(r'(\w+ \d{1,2}, \d{4})')[0],
        errors='coerce'
    )
    # Convert input start/end dates to datetime
    start_dt = pd.to_datetime(startDate)
    end_dt = pd.to_datetime(endDate)
        # Filter rows by date range
    filtered_data = self.data[
        (self.data['Date_clean'] >= start_dt) & (self.data['Date_clean'] <= end_dt)
    ]
    # Group by Nationality
    counts = (
        filtered_data.groupby('Expedition')
        .size()
        .reset_index(name='Death Count')
    )
    expeditions_list = []
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
    return expeditions_list
  
  def drilldown_expedition_graph(self, expedition, startDate, endDate):
    # Clean and parse the Date column
    self.data['Date_clean'] = pd.to_datetime(
        self.data['Date'].str.extract(r'(\w+ \d{1,2}, \d{4})')[0],
        errors='coerce'
    )
    # Convert input start/end dates to datetime
    start_dt = pd.to_datetime(startDate)
    end_dt = pd.to_datetime(endDate)
    
    # Filter by state and date range
    filtered_data = self.data[
        (self.data['Date_clean'] >= start_dt) &
        (self.data['Date_clean'] <= end_dt) &
        (self.data['Expedition'] == expedition) &
        (self.data['Date_clean'].notnull())
    ]
    # The columns that I'm using
    selected_columns = [
        'Name', 'Date', 'Age', 'Expedition',
        'Cause_of_Death', 'Location', 'Remains status'
    ]
    filtered = filtered_data[selected_columns]
    # Convert to list of dictionaries and replace NaNs with None
    drilldown_data = filtered.to_dict(orient='records')
    for row in drilldown_data:
        for key in row:
            if pd.isna(row[key]):
                row[key] = None
    return drilldown_data
  
  def top_causes_of_death(self, number_of_causes, startDate, endDate):
    cause_of_death_list = []
    # Clean and parse the Date column (if not already cleaned)
    self.data['Date_clean'] = pd.to_datetime(
        self.data['Date'].str.extract(r'(\w+ \d{1,2}, \d{4})')[0],
        errors='coerce'
    )
    # Convert input start/end dates to datetime
    start_dt = pd.to_datetime(startDate)
    end_dt = pd.to_datetime(endDate)
    # Filter rows by date range
    filtered_data = self.data[
        (self.data['Date_clean'] >= start_dt) & (self.data['Date_clean'] <= end_dt)
    ]
    counts = (
        filtered_data.groupby('Cause_of_Death')
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
    return cause_of_death_list

  def drilldown_top_causes_of_death_graph(self, cause_of_death, startDate, endDate):
    # Clean and parse the Date column
    self.data['Date_clean'] = pd.to_datetime(
        self.data['Date'].str.extract(r'(\w+ \d{1,2}, \d{4})')[0],
        errors='coerce'
    )
    # Convert input start/end dates to datetime
    start_dt = pd.to_datetime(startDate)
    end_dt = pd.to_datetime(endDate)

    # Filter by cause of death and date range
    filtered_data = self.data[
        (self.data['Date_clean'] >= start_dt) &
        (self.data['Date_clean'] <= end_dt) &
        (self.data['Cause_of_Death'] == cause_of_death) &
        (self.data['Date_clean'].notnull())
    ]
    print(filtered_data)
    # The columns that I'm using
    selected_columns = [
        'Name', 'Date', 'Age', 'Expedition',
        'Cause_of_Death', 'Location', 'Remains status'
    ]
    filtered = filtered_data[selected_columns]
    # Convert to list of dictionaries and replace NaNs with None
    drilldown_data = filtered.to_dict(orient='records')
    for row in drilldown_data:
        for key in row:
            if pd.isna(row[key]):
                row[key] = None
    return drilldown_data
  
  def common_months_for_deaths(self):
      # This list will hold the data 
      deaths_by_month_list = []

      # Ensure 'Date' is parsed into datetime objects
      self.data['Date_clean'] = pd.to_datetime(self.data['Date'], errors='coerce')

      # Drop rows where date parsing failed
      clean_data = self.data.dropna(subset=['Date_clean'])

      # Extract month number and month name
      clean_data['Month_Num'] = clean_data['Date_clean'].dt.month
      clean_data['Month_Name'] = clean_data['Date_clean'].dt.month_name()

      # Count deaths per month and sort by Month_Num
      month_counts = clean_data.groupby(['Month_Num', 'Month_Name']).size().sort_index()
      # Convert to list
      for (month_num, month_name), count in month_counts.items():
          deaths_by_month_list.append([month_name, count])
      print(deaths_by_month_list)
      return deaths_by_month_list


# test_object = ExamineData()
# test_object.common_months_for_deaths()