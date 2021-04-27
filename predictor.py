import sys
import pickle
import numpy as np
from datetime import datetime

min_dt = datetime(2020, 1, 1)

def predict_reg(input: list):
    """
    predict data using linear regression model

    :param  input:  list of float to be predicted
    :return:        prediction data
    """
    reg_model = pickle.load(open("reg_model.pickle", 'rb'))
    input = np.array(input).reshape(-1,1)
    return reg_model.predict(input)

if __name__ == "__main__":
    dt = sys.argv[1].split("-")
    dt = datetime(int(dt[0]), int(dt[1]), int(dt[2]))
    x = (dt.timestamp() - min_dt.timestamp()) / 86400

    result = predict_reg([x])
    print(result)