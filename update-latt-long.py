import requests
import json

# Send HTTP GET request to geocoder.ca
url = 'https://geocoder.ca/'
params = {'locate': 'V5H4N8', 'json': '2'}
response = requests.get(url, params=params)

# Parse JSON response
data = json.loads(response.text)

# Extract Dissemination_Area and standard fields
longt = data['longt']
latt = data['latt']

# Print extracted fields
print('longt:', longt)
print('latt:', latt)