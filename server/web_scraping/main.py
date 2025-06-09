# This file will web scrape the data that I need and place it into a CSV file. 
# Site to scrape: https://en.wikipedia.org/wiki/List_of_people_who_died_climbing_Mount_Everest

import requests
from bs4 import BeautifulSoup
import pandas as pd

class Scrape():

  def scrape_site(self):
    url = 'https://en.wikipedia.org/wiki/List_of_people_who_died_climbing_Mount_Everest'
    # Making the request
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    # Find all tables on the page
    tables = soup.find_all('table', {'class': 'wikitable'}) 
    for i, table in enumerate(tables[:2]):
      df = pd.read_html(str(table))[0]
    # Assuming the first table is correct, convert to DataFrame
    deaths_df = pd.read_html(str(tables[0]))[0]
    # Save to CSV
    deaths_df.to_csv('everest_deaths.csv', index=False)

test_obj = Scrape()
test_obj.scrape_site()
  
