import requests
url = 'https://dummyjson.com/products'
response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    for x in data['products']:
        name = x['title']
        print(name)

        