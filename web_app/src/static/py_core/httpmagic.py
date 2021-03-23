import requests



def read_http():
    resp = requests.get("http://core_api:8000/locations")
    data = resp.json()
    return data


