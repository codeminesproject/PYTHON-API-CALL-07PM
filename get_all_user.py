
import requests
import login

api_url = "http://127.0.0.1:8000/get-all-users"

login_response = login.api_login("rahul@example.com","Rahul@123")

if login_response[0]==200:
    get_response = requests.get(api_url,headers={"Authorization":login_response[1]})
    get_response_data = get_response.json()
    print(get_response_data)
else:
    print(login_response[1])

