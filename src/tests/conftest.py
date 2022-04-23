import pytest
from app import create_app

from app.strategy.model import Card


@pytest.fixture
def app():
    """Instance of Main flask app"""
    app = create_app("test")
    return app


@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def card() -> Card:
    return Card(id=273, name="Rampaging Leviathan", mana=7, attack=5, health=5, type="creature", god = "nature")    

@pytest.fixture
def db(app):

    from app import db

    with app.app_context():
        db.drop_all()
        db.create_all()
        yield db
        db.drop_all()
        db.create_all()
        db.session.commit()    
