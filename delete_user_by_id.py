
import requests

api_url = "http://127.0.0.1:8000/delete-user?id=4"

response = requests.delete(api_url)

response_json = response.json()

print(response_json["data"])


