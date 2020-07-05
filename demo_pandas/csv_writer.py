# Chapter - fundamentals
# reference and assignment

import pandas as pd

DATA_PATH = './'

train = pd.read_csv(DATA_PATH+'california_housing_train.csv')


print(train.shape)
print(train.head())

# write to file system with the name of 'california_output.csv'
train.to_csv(DATA_PATH+'california_output.csv')