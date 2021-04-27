import sys
import pickle
import numpy as np

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
    args = [float(arg) for arg in sys.argv[1:]]
    result = predict_reg(args)
    print(result)