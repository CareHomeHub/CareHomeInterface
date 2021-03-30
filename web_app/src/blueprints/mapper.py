# -*- coding: utf-8 -*-
from flask import Blueprint, render_template
from flask import current_app
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