
import requests

api_url = "https://jsonplaceholder.typicode.com/posts"

response = requests.get(api_url)

response_json = response.json()

print(response_json)


