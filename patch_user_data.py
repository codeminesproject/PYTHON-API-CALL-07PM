
import requests

api_url = "http://127.0.0.1:8000/update-user"

body = {
    "id":12,
    "password":"pass@123456789"
}

response = requests.patch(api_url,json=body)

response_json = response.json()

print(response_json["data"])


