import requests



def read_http():
    resp = requests.get("http://localhost:8000/location")
    data = resp.json()
    return data


