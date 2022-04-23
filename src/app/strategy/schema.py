from marshmallow import fields, Schema


class CardSchema(Schema):

    id      = fields.Integer(attribute="id")
    name    = fields.String(attribute="name")
    mana    = fields.Integer(attribute="mana")
    attack  = fields.Integer(attribute="attack")
    health  = fields.Integer(attribute="health")
    type    = fields.String(attribute="type")
    god     = fields.String(attribute="god")
