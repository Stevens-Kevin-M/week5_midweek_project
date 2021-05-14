from flask import Blueprint, request, jsonify
from ship_inventory.helpers import token_required
from ship_inventory.models import User, Ship, ship_schema, ship_schemas, db

api = Blueprint('api', __name__, url_prefix='/api')

@api.route('getdata')
def getdata():
    return{'some_value': 52, 'another_value': 73}

    #CREATE SHIP ENDPOINT
@api.route('/ships', methods = ['POST'])
@token_required
def create_ship(current_user_token): #coming from token_required decorator
    name = request.json['name']
    description = request.json['description']
    price = request.json['price']
    cam_quality = request.json['cam_quality']
    flight_time = request.json['flight_time']
    max_speed = request.json['max_speed']
    dimensions = request.json['dimensions']
    weight = request.json['weight']
    cost_of_prod = request.json['cost_of_prod']
    series = request.json['series']
    user_token = current_user_token.token

    ship = Ship(name,description,price,cam_quality,flight_time,max_speed,dimensions,weight,cost_of_prod,series,user_token=user_token)

    db.session.add(ship)
    db.session.commit()

    response = ship_schema.dump(ship)
    return jsonify(response)

# RETRIEVE ALL SHIPS
@api.route('ships', methods = ['GET'])
@token_required
def get_ships(current_user_token):
    owner = current_user_token.token
    ships = Ship.query.filter_by(user_token = owner).all()
    response = ship_schemas.dump(ships)
    return jsonify(response)

# RETRIEVE ONE SHIP ENDPOINT
@api.route('/ships/<id>', methods = ['GET'])
@token_required
def get_ship(current_user_token, id):
    ship = Ship.query.get(id)
    response = ship_schema.dump(ship)
    return jsonify(response)