import pandas as pd
import numpy as np
import requests
import json

# Fetch congressional data using personal API
api_key = 'fSJL6NcHBIKc2n8oHF1hCOYamxxmchsLWLySG7ON'
congress_url = f'https://api.congress.gov/v3/bill?api_key={api_key}'

params = {
    'congress': '118',
    'limit': 250,
}

response = requests.get(congress_url, params=params)
congress_data = response.json()

# Process congressional data
# Extract relevant information, such as bill titles, summaries, and dates
bills = pd.DataFrame(congress_data['bills'])


#Extract bills relevant to markets 
market_words = [
    'stock market', 'equity', 'bond', 'securities', 'commodities',
    'economic growth', 'GDP', 'recession', 'inflation', 'unemployment', 'deflation',
    'finance', 'financial services', 'banking', 'credit', 'investment',
    'tax', 'corporate tax', 'capital gains tax', 'fiscal policy',
    'regulation', 'compliance', 'oversight', 'financial regulation',
    'interest rate', 'Federal Reserve', 'monetary policy',
    'trade', 'tariffs', 'export', 'import', 'commerce', 'sanctions',
    'corporate governance', 'shareholder rights', 'mergers and acquisitions',
    'geopolitical', 'foreign policy', 'international relations', 'diplomacy',
    'national security', 'cybersecurity', 'defense',
    'employment', 'unemployment', 'job creation', 'labor laws',
    'climate change', 'environmental policy', 'green energy', 'sustainability',
    'healthcare', 'public health', 'pandemic', 'pharmaceuticals', 'biotech',
    'technology', 'innovation', 'digital economy', 'fintech', 'blockchain', 'AI',
    'infrastructure', 'broadband', 'transportation', 'energy', 'utilities',
    'cryptocurrency', 'digital currency', 'Bitcoin', 'DeFi',
    'COVID-19', 'stimulus', 'economic recovery'
]

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




