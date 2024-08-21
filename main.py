import requests

url = 'https://cognitive-dagmar-emekadefirst-156954a7.koyeb.app/applicants'
response = requests.get(url)
data = response.json()

for x in data:
    name = x['fullname']
    print(name)   

       