import requests

api_key = "sk_test_cad7ad2626bb47d8c2d99e72c8dce4c4ca487f5d"
domain = 'https://api.paystack.co'
endpoint = 'transaction/initialize'

headers = {
    'Authorization': f'Bearer {api_key}',
    'Content-Type': 'application/json',
}

data = {
    'amount': 10000,
    'email': 'uzoechidavid09@gmail.com',
}

response = requests.post(f'{domain}/{endpoint}', headers=headers, json=data)

# Check if the request was successful
if response.status_code == 200:
    try:
        data = response.json()
        print(data)
    except requests.exceptions.JSONDecodeError:
        print("Error decoding JSON:", response.text)
else:
    print(f"Request failed with status code {response.status_code}")
    print("Response text:", response.text)
