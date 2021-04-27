from time import sleep
from kafka import KafkaProducer
import random

producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=lambda x:
                         x.encode('utf-8'))

message = ""
x = 1

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
    return (msg + ";" + str(x) + " " + str(y) if msg != "a" else str(x) + " " + str(y))

while True:
    y = reg(x)
    message = append_msg(message, x, y)
    producer.send('regression', value=message)
    sleep(5)
    x = x+1

