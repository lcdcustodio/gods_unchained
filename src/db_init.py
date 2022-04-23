
from datetime import datetime
from flask import json
from app import db, create_app
from app.strategy import Card
import pandas as pd

app = create_app()
app.app_context().push()

def get_dataset():

    columns = ['id', 'name', 'mana', 'attack', 'health','type','god']
    
    dataset = pd.read_csv('src/dataset/challenge_train.csv')    
    db_in = dataset[columns]
    db_in.to_json('src/dataset/challenge_train.json', orient = "records", force_ascii = True, default_handler = None)

    dataset = pd.read_csv('src/dataset/challenge_test.csv')    
    db_in = dataset[columns]
    db_in.to_json('src/dataset/challenge_test.json', orient = "records", force_ascii = True, default_handler = None)
    

def seed_things():

    dataset_json = json.load(open("src/dataset/challenge_train.json"))
    db.session.bulk_insert_mappings(Card, dataset_json)

    dataset_json = json.load(open("src/dataset/challenge_test.json"))
    db.session.bulk_insert_mappings(Card, dataset_json)


class DataSeed():

    def run(self):
        print("Getting DataSet...")
        get_dataset()    
        print("Dropping tables...")
        db.drop_all()
        db.create_all()
        seed_things()
        db.session.commit()
        print("DB successfully seeded.")


DataSeed().run()
