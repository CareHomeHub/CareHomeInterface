import json


with open('api/src/static/data/loc_marker_list.json') as json_file:
    data = json.load(json_file)
    # for p in data:
    #     print('Name: ' + p['name'])
print(data)

def get_data():
    return data