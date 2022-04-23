from app import db
from flask import request, json, jsonify
from .schema import CardSchema

import sys

from sqlalchemy.exc import IntegrityError

from typing import List
from .model import Card
import pickle
import numpy as np


card_schema = CardSchema(many=True)

class CardService:
    
    @staticmethod
    def find_by_card(id) -> Card:

        result = {}


        if Card.query.filter_by(id=id).first():

           strategy = GetForecast(Card.query.filter_by(id=id).one().json()).run()
           
           result.update({'result': strategy})
           
           result.update({'success': True})
           result.update({'code': 200})   
           return result      

        result.update({'result': 'Card id \'%s\' not found' % id})
        result.update({'success': False})
        result.update({'code': 404})
        return result


class GetForecast:

    def __init__(self, attrs): 
        self.attrs = attrs


    def run(self):
    
        x_in = []
        #------------------------------
        type_enc = json.load(open("src/model/enc_type.json"))        
        god_enc = json.load(open("src/model/enc_god.json"))
        
        x_in.append(self.attrs.get('mana'))
        x_in.append(self.attrs.get('attack'))
        x_in.append(self.attrs.get('health'))
        x_in.append(type_enc.get(self.attrs.get('type')))
        x_in.append(god_enc.get(self.attrs.get('god')))
        
        # load the model from disk
        loaded_model = pickle.load(open("src/model/model.pkl", 'rb'))           
        
        prediction = loaded_model.predict(np.array(x_in, dtype=object).reshape(1, -1))
        
        return {'id': self.attrs.get('id'), 'name':self.attrs.get('name'), 'strategy' : prediction[0]}
        