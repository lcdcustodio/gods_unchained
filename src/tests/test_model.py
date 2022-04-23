from app.strategy.model import Card
from flask_sqlalchemy import SQLAlchemy


def test_card_create(card: Card):
    assert card

def test_Card_retrieve(card: Card, db: SQLAlchemy):
    db.session.add(card)
    db.session.commit()
    s = Card.query.first()

    assert s.__dict__ == card.__dict__
