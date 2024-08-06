import pandas as pd
import numpy as np
import requests
import json



# Fetch congressional data uaing personal API
api_key = 'fSJL6NcHBIKc2n8oHF1hCOYamxxmchsLWLySG7ON'
congress_url = f'https://api.congress.gov/v3/bill?api_key={api_key}'

params = {
    'congress': '118',
    'limit': 100,
}

response = requests.get(congress_url, params=params)
congress_data = response.json()

# Process congressional data
# Extract relevant information, such as bill titles, summaries, and dates
bills = pd.DataFrame(congress_data['bills'])


#Extract bills relevant to markets 
market_words = ['unemployment', "interest rate", "yield", "bond", "jobs", "war", 'stock', 'economy', 'trade', 'investment', 'sanction', 'geopolitical', 'immigration', 'climate', 'education']

bills_of_interest = []

def keywords_search():
    for index, row in bills.iterrows(): #iterate over each row
        title = row['title'].lower() #lowercase titles
        if any(word in title for word in market_words):
            bills_of_interest.append(row)


keywords_search()


bills_of_interest_pd = pd.DataFrame(bills_of_interest)


print('The bills of interest are:')
print(bills_of_interest_pd)



