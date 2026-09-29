
# requests is a module used to help to connect with api

import requests

def api_login(username,password):
    api_url = "http://127.0.0.1:8000/auth"
    body = {"username":username,"password":password}
    response=requests.post(api_url,json=body)
    response_data = response.json()
    
    # if response.status_code==200:
    #     print("Login Success")
    # elif response.status_code==400:
    #     print("Bad Request")
    # elif response.status_code==401:
    #     print("Invalid Credentials")
    # elif response.status_code==500:
    #     print("Something Went Wrong")
    # else:
    #     print("invalid")

    return [response.status_code,response_data["data"]]



    
