import pandas as pd
import json

data = pd.read_json("/Users/colinmoore-hill/Documents/cqc/dropzone/CQC_data_file_multiples_shrt.json")

rows = len(data.index)
marker_list = []
i = 0 
for item in range(31):

    loc_marker = {
    "loc_id" : data.loc[item]["req"]["locationId"],
    "type" : data.loc[item]["loc"]["type"],
    "name" : data.loc[item]["loc"]["name"],
    "rating" : data.loc[item]["loc"]["currentRatings"]["overall"]["rating"],
    "numberOfBeds" : data.loc[item]["loc"]["numberOfBeds"],
    "postcode" : data.loc[item]["postcode"]["result"]["postcode"],
    "lat" : data.loc[item]["postcode"]["result"]["longitude"],
    "lng" : data.loc[item]["postcode"]["result"]["latitude"]
}

    print (f"{i} :  : {loc_marker}")
    marker_list.append(loc_marker)
    i+=1
    
    
# print (marker_list)
 
with open("loc_marker_list.json", "a") as write_file:
    json.dump(marker_list, write_file)