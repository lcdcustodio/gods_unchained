from flask import request
from flask_accepts import accepts, responds
from flask_restx import Namespace, Resource, fields
from flask.wrappers import Response
from typing import List

from .schema import CardSchema
from .service import CardService
from .model import Card

api = Namespace("Card", description="Strategy prediction for a card")


@api.route("/<int:id>")
@api.param("id", "Type a valid card id")
class CardNameResource(Resource):
    
    @api.response(200, 'Success')
    @api.response(404, 'Not Found')
    def get(self, id) -> Card:
        """Get Prediction"""

        resp = CardService.find_by_card(id)  
        if resp.get('success'):
            return {'result':resp.get('result'),'success':resp.get('success')},resp.get('code')
        else:
            return {'message':resp.get('result'),'success':resp.get('success')},resp.get('code')


