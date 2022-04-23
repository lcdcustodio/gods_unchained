from app.strategy.model import Card
from flask_sqlalchemy import SQLAlchemy

def test_card_create(card: Card):
    assert card

def test_request_return_404(client):
    assert client.get("/url_does_not_exist").status_code == 404      

def test_request_return_200(client):
    response = client.get("/") 
    assert client.get("/").status_code == 200      


def test_get_card(client, card: Card, db: SQLAlchemy):
    db.session.add(card)
    db.session.commit()
    response = client.get("/api/v1/predict/273").get_json()['result']   
    print (response)

    payload = {'id':273,'name': 'Rampaging Leviathan', 'strategy': 'late'} 
    assert payload == response



def test_get_card_error(client, card: Card, db: SQLAlchemy):
    db.session.add(card)
    db.session.commit()
    response = client.get("/api/v1/predict/101010").get_json() 
    
    payload = {'message':'Card id \'101010\' not found','success': False} 
    assert payload == response