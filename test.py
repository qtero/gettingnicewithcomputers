# print("Hello World") - First ever python code written

# Assignment 1 Coingecko: Run the program to get the highest value of NDX over the last 5 days

# api.coingecko.com/api/v3 - Host URL
import requests
import json
payload = {'date':'28-03-2021'}
r = requests.get('https://api.coingecko.com/api/v3/coins/indexed-finance/history', params=payload)
json_object = json.loads(r.text)
indexed_USD_Value = float(json.dumps(json_object['market_data']['current_price']['usd'], indent=2)) #Uses "keys" to pull only specifc data within the dict, this this data set we are only looking for the current USD price according to date and then converts that current str into a value

#build statements to rerun code above looking for the highest value in past 5 days
payloads = [{'date':'27-03-2021'},{'date':'28-03-2021'},{'date':'29-03-2021'},{'date':'30-03-2021'},{'date':'31-03-2021'},{'date':'01-04-2021'}]
indexed_USD_values = []
for i in range(len(payloads)):
    specific_date = payloads[i]#change payload one day back, get value for day, store all values within list
    r = requests.get('https://api.coingecko.com/api/v3/coins/indexed-finance/history', params=specific_date)
    json_object = json.loads(r.text)
    indexed_USD_Value = float(json.dumps(json_object['market_data']['current_price']['usd'], indent=2)) 
    indexed_USD_values.append(indexed_USD_Value)

print(max(indexed_USD_values))