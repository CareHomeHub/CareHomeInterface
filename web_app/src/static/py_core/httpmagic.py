import requests



def read_http():
    resp = requests.get("http://127.0.0.1:8000/location")
    data = resp.json()
    return data


