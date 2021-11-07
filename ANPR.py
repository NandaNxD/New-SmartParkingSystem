import requests
from pprint import pprint
regions = ['in'] # Change to your country
with open('l3.jpg', 'rb') as fp:
    response = requests.post(
        'https://api.platerecognizer.com/v1/plate-reader/',
        data=dict(regions=regions),  # Optional
        files=dict(upload=fp),
        headers={'Authorization': 'Token f52c6f2941e5bc78ad0ec88f04080a579f7b4509'})
pprint(response.json())
