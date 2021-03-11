# print("Hello World") - First 
# api.coingecko.com/api/v3 - Host URL
import requests
import json
payload = {'date':'11-03-2021'}
r = requests.get('https://api.coingecko.com/api/v3/coins/indexed-finance/history', params=payload)
json_object = json.loads(r.text)
json_formatted_str = json.dumps(json_object, indent=2)
print(json_formatted_str)
