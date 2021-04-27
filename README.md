# Simple Real Time Linear Regression Model with Kafka
This repository contains code to run simple linear regression using sklearn for the linear regression model and Kafka as message broker. (`producer_regression.py`) will generate the data and publish it to Kafka. (`trainer.py`) will consume the published data and train the linear regression model with the consumed data. The training model will be dumped using (`pickle`) and will be loaded by (`predictor.py`). (`predictor.py`) will predict the data using the loaded linear regression model.

## How To Run

1. In terminal #1, run producer
```
python producer_regression.py
```

2. In terminal #2, run trainer
```
python trainer.py
```

2. In terminal #3, run predictor
```
python predictor.py <args separated by space>

example: python predictor.py 10 20 30
```