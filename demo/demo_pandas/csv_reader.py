# Chapter - fundamentals
# reference and assignment

import pandas as pd

DATA_PATH = '/'

train = pd.read_csv(DATA_PATH+'california_housing_train.csv')


print(train.shape)
print(train.head())

features = [f for f in train.columns.values if f!='median_house_value']
# train_x = train[features]
print(features)