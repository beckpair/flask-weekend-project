import json
from flask import Blueprint, request, jsonify
from tarot_project.models import db, Card, card_schema, cards_schema
from tarot_project.helpers import token_required

api = Blueprint('api', __name__, url_prefix = '/api')

@api.route('/getdata')
@token_required
def getdata(current_user_token):
    return{'some': 'value'}

@api.route('/cards', methods = ['POST'])
@token_required
def create_card(current_user_token):
    Name = request.json['Name']
    Zodiac = request.json['Zodiac']
    Element = request.json['Element']
    Arcana = request.json['Arcana']
    Upright = request.json['Upright']
    Reversed_ = request.json['Reversed_']
    Gender = request.json['Gender']
    user_token = current_user_token.token

    print (f"User token: {current_user_token}.")

    card = Card(Name, Zodiac, Element, Arcana, Upright, Reversed_, Gender, user_token=user_token)

    db.session.add(card)
    db.session.commit()

    response = card_schema.dump(card)

    return jsonify(response)

@api.route('/cards/<id>', methods = ['GET'])
@token_required
def get_card(current_user_token, id):
    owner = current_user_token.token
    if owner == current_user_token.token:
        card = Card.query.get(id)
        response = card_schema.dump(card)
        return jsonify(response)
    else:
        return jsonify({'message': 'Valid Token Required'}), 401

@api.route('/cards', methods = ['GET'])
@token_required
def get_cards(current_user_token):
    owner = current_user_token.token
    cards = Card.query.filter_by(user_token = owner).all()
    response = cards_schema.dump(cards)
    return jsonify(response)

@api.route('/cards/<id>', methods = ['GET', 'POST'])
@token_required
def update_card(current_user_token, id):
    card = Card.query.get(id)

    card.Name = request.json['Name']
    card.Zodiac = request.json['Zodiac']
    card.Element = request.json['Element']
    card.Arcana = request.json['Arcana']
    card.Upright = request.json['Upright']
    card.Reversed_ = request.json['Reversed_']
    card.Gender = request.gender['Gender']
    card.user_token = current_user_token.token

    db.session.commit()
    response = card_schema.dump(card)
    return jsonify(response)

@api.route('/cards/<id>', methods = ['DELETE'])
@token_required
def delete_card(current_user_token, id):
    card = Card.query.get(id)
    db.session.delete(card)
    db.session.commit()
    response = card_schema.dump(card)
    return jsonify(response)