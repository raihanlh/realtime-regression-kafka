from time import sleep
from kafka import KafkaProducer
import random
import pandas as pd
import numpy as np
from datetime import datetime

producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=lambda x:
                         x.encode('utf-8'))

message = ""
x = 1
min_dt = datetime(2020, 1, 1)

def reg(x):
    """
    generate calculation from input x

    :param  x:  input float or int
    :return:    new float calculated by using x
    """
    return 2*x+3+random.uniform(-2.0,2.0)

def append_msg(msg, x, y):
    """
    append string msg with x and y

    :param  msg:    input string
    :param  x:      input float
    :param  y:      input float
    :return:        appended msg with x and y
    """
    return (msg + ";" + str(x) + " " + str(y) if msg != "" else str(x) + " " + str(y))

if __name__ == "__main__":
    df = pd.read_csv("BTC-USD.csv")

    i = 0

    for j in range(len(df)):
        dt = df.loc[i]["Date"]
        dt = dt.split('-')
        dt = datetime(int(dt[0]), int(dt[1]), int(dt[2]))

        x = (dt.timestamp() - min_dt.timestamp()) / 86400
        y = df.loc[i]["Adj Close"]
        message = append_msg(message, x, y)
        print(message)
        producer.send('regression', value=message)
        sleep(3)
        i += 1
