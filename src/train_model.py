import pandas as pd
from sklearn import preprocessing
import json

from numpyencoder import NumpyEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import pickle

from sklearn.metrics import accuracy_score

def train():

    print("----------------------")
    print("Training Model...")

    # get data
    base_train = pd.read_csv('src/dataset/challenge_train.csv')    
    
    columns_input = ['mana', 'attack', 'health','type','god']
    columns_output = ['strategy']

    base_train_input_model = base_train[columns_input]
    base_train_output_model = base_train[columns_output]

    x_in = base_train_input_model.iloc[:,0:5].values
    y_out = base_train_output_model.iloc[:,0].values
    
    
    #encode target labels with value between 0 and n_classes-1
    encode = preprocessing.LabelEncoder()

    x_in[:,3] = encode.fit_transform(x_in[:,3])

    keys = encode.classes_
    values = encode.transform(encode.classes_)
    enc_type = dict(zip(keys, values))
    
    et_file = open('src/model/enc_type.json','w')
    et_file.write(json.dumps(enc_type,cls=NumpyEncoder))
    et_file.close()
    
    x_in[:,4] = encode.fit_transform(x_in[:,4])

    keys = encode.classes_
    values = encode.transform(encode.classes_)
    enc_god = dict(zip(keys, values))

    eg_file = open('src/model/enc_god.json','w')
    eg_file.write(json.dumps(enc_god,cls=NumpyEncoder))
    eg_file.close()

   
    x_train, x_test, y_train, y_test = train_test_split(x_in, y_out, test_size = 0.2)
    
    #modeling
    model = LogisticRegression()
    model.fit(x_train, y_train)
    
    forecast = model.predict(x_test)
    
    # save the model to disk
    filename = 'src/model/model.pkl'
    pickle.dump(model, open(filename, 'wb'))    
    
    message1 = 'Training Success'
    message2 = 'Model training score: %s' % accuracy_score(y_test, forecast)
    print(message1)
    print(message2)    
    print("----------------------")    
    
train()    