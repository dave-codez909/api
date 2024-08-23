import requests

API_KEY = "sk_test_4644dce53d1d322fb431eea1b4ce7659f13c3b50"

url = "https://api.paystack.co/bank/validate"

headers = {
    'Authorization': f'Bearer {API_KEY}',
    'Content-Type': 'application/json'
}

# User inputs
user_name = input("Enter your name: ")
account_number = input("Enter your account number: ")

data = {
    "bank_code": "632005",  # Replace with actual bank code if needed
    "country_code": "ZA",
    "account_number": account_number,
    "account_name": user_name,
    "account_type": "personal",
    "document_type": "identityNumber",
    "document_number": "1234567890123"  # Replace with actual document number if needed
}

response = requests.post(url, headers=headers, json=data)

if response.status_code == 200:
    try:
        data = response.json()
        bank_code = data.get("bank_code", "Bank code not found")
        print(f"Hello {user_name}, your bank code is: {bank_code}")
    except Exception as e:
        print(f"An error occurred: {e}")
else:
    print(f"Request failed with status code {response.status_code}")
    print(response.text)
