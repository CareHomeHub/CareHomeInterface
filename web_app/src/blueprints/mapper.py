# -*- coding: utf-8 -*-
from flask import Blueprint, render_template
from flask import current_app
import folium
import requests
import pandas as pd
# from logzero import logger

mapper_blueprint = Blueprint(name='mapper', import_name=__name__, template_folder='templates', url_prefix='/mapper/')

@mapper_blueprint.route('add/<message>', methods=['GET'])
@mapper_blueprint.route('add/', defaults={'message': 'mapper - no add'},methods=['GET'])
@mapper_blueprint.route('/', defaults={'message': 'mapper'}, methods=['GET'])
def mapper(message):
    current_app.logger.info("Curr-BluPrnt mapper add  - with message : {}".format(message))
    return 'mapper - {}'.format(message)


@mapper_blueprint.route('charter/', defaults={'message': 'charter'}, methods=['GET'])
def charter(message):
    current_app.logger.info("Curr charter -")
    return render_template('map/map2.html')

@mapper_blueprint.route('about/', methods=['GET'])
def about():
    current_app.logger.info("Curr ABOUT -")
    return render_template('about.html')

@mapper_blueprint.route('/<loc>', methods=['GET'])
def loc_mapper(loc = ""):
    chur = pd.read_json("./static/data/churches.json")
    care = pd.read_json("./static/data/rec2.json")
    if loc == "":
        locref = (50.804055, -1.980081)
    if loc == "Loc1":
        locref = (50.804055, -1.980081)
    if loc == "Loc2":
        locref = (50.7192, -1.8808)
    if loc == "Loc3":
        locref = (50.7112, -2.4412)

    start_coords = (float(locref[0]), float(locref[1]))
    folium_map = folium.Map(location=start_coords, zoom_start=14)
    
    for row in chur.itertuples():
        uri = "https://www.snu.org.uk"+row.lnk[0]
        print(f"URI = {uri}")
        test = folium.Html(f'<b>{row.church}</b></br> <a href="{uri} "target="_blank"> SNU Link </a>', script=True)
        popup = folium.Popup(test)
        folium_map.add_child(folium.Marker(location=[row.lat,  row.lng],
                 popup=popup, icon=folium.Icon(color='green', icon='leaf')))
        
        
    for row in care.itertuples():
        test1 = folium.Html(f'<b>{row.locationName}</b></br><p>PostCode: {row.postalCode}  Constit: {row.parliamentary_constituency}</p>', script=True)
        popup = folium.Popup(test1)
        folium_map.add_child(folium.Marker(location=[row.lat,  row.lng],
                 popup=popup, icon=folium.Icon(color='green', icon='hand-holding-heart')))
    
    return folium_map._repr_html_()


@mapper_blueprint.route('/cqc', methods=['GET'])
def cqc_mapper(loc = ""):
    locref = (50.7112, -2.4412)
    
    ratings = requests.get("https://carehomehub-platform.herokuapp.com/locations").json()
    current_app.logger.info("Curr-BluPrnt call carehomehub-platform.herokuapp.com  - with json response : {}".format(ratings))
    

    start_coords = (float(locref[0]), float(locref[1]))
    folium_map = folium.Map(location=start_coords, zoom_start=14)

        
    for row in ratings:
        test1 = folium.Html(f'<b>{row["name"]}</b></br><p>cqc_id: {row["loc_id"]} service_type: {row["typ"]} number_of_beds: {row["numberOfBeds"]} PostCode: {row["postcode"]} </p>', script=True)
        popup = folium.Popup(test1)
        folium_map.add_child(folium.Marker(location=[row.lat,  row.lng],
                 popup=popup, icon=folium.Icon(color='green', icon='hand-holding-heart')))
    
    return folium_map._repr_html_()
