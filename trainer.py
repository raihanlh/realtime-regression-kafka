from kafka import KafkaConsumer
import numpy as np
from sklearn.linear_model import LinearRegression
import pickle

consumer = KafkaConsumer(
    'regression',
     bootstrap_servers=['localhost:9092'],
     auto_offset_reset='earliest',
     enable_auto_commit=True,
     group_id='my-group',
     value_deserializer=lambda x: x.decode('utf-8'))

model = LinearRegression()

for message in consumer:
    message = message.value.split(";")
    x = []
    y = []
    for pair in message:
        if pair != "":
            pair = pair.split(" ")
            x.append(float(pair[0]))
            y.append(float(pair[1]))
    
    model.fit(np.array(x).reshape(-1,1), np.array(y))
    print(model.predict(np.array([[10],[20],[30]])))
    
    pickle.dump(model, open("reg_model.pickle", 'wb'))