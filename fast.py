import requests

url = 'https://api.coindesk.com/v1/bpi/currentprice.json'
response = requests.get(url)
data = response.json()  

rate = data['time']['updated']
currency = data['bpi']['USD']['symbol']
price = data['bpi']['USD']['rate']

print(f'{rate}: {currency} {price}')
