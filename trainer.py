from kafka import KafkaConsumer
import numpy as np
from sklearn.linear_model import LinearRegression
import pickle
from datetime import datetime

consumer = KafkaConsumer(
    'regression',
     bootstrap_servers=['localhost:9092'],
     auto_offset_reset='earliest',
     enable_auto_commit=True,
     group_id='my-group',
     value_deserializer=lambda x: x.decode('utf-8'))

model = LinearRegression()
i = 0
dt_0 = datetime(2020, 1, 1)

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
    dt_i = datetime.fromtimestamp(dt_0.timestamp() + i * 86400)
    print("Model {} dengan data tanggal {} s/d {} berhasil dibuat".format(i+1, dt_0.strftime('%Y-%m-%d'), dt_i.strftime('%Y-%m-%d')))
    # print(model.predict(np.array([[10],[20],[30]])))
    i += 1
    pickle.dump(model, open("reg_model.pickle", 'wb'))