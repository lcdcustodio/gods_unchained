from sqlalchemy import Integer, Column, String
from app import db


class Card(db.Model):

    __tablename__ = "cards"

    id      = db.Column(Integer(), primary_key=True)
    name    = db.Column(String(80), nullable=False, unique=True)
    mana    = db.Column(Integer(), primary_key=False)
    attack  = db.Column(Integer(), primary_key=False)
    health  = db.Column(Integer(), primary_key=False)
    type    = db.Column(String(80), nullable=False)
    god     = db.Column(String(80), nullable=False)



    def __init__(self, id, name, mana, attack, health, type, god):

        self.id     = id
        self.name   = name
        self.mana   = mana
        self.attack = attack
        self.health = health
        self.type   = type
        self.god    = god


    def __repr__(self):
        return f'Card(id={self.id}, name={self.name}, mana={self.mana}, attack={self.attack}, health={self.health}, type={self.type}, god={self.god})'

    def json(self):
        return {'id': self.id, 'name': self.name, 'mana': self.mana, 'attack': self.attack, 'health': self.health, 'type': self.type, 'god': self.god}
