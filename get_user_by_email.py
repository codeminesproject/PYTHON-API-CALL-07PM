
import requests

email = "rahul@example.com"
api_url = "http://127.0.0.1:8000/get-user-by-email?email="+email

response = requests.get(api_url)

response_json = response.json()

print(response_json["data"])


