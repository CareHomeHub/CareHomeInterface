import requests



def read_http():
    resp = requests.get("http://core_api:8000/location")
    data = resp.json()
    return data


