import pandas as pd
import numpy as np
import requests
from flask import Flask, request, jsonify

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
print(bills)