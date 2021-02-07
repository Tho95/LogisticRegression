# Thomas Hübscher / 07.02
#Example for Logitic Regression for classification of poisonous/edible mushrooms

import pandas as pd
from sklearn.model_selection import train_test_split

import dataInfo

filePath = 'mushrooms.csv'
X = pd.read_csv(filePath)

y = X['class'] #(target we want to predict)

X.drop('class', axis = 1, inplace=True)
print(X.head())

dataInfo.general(X)
dataInfo.missing_value_per_column(X)
categorical, numerical = dataInfo.colType(X)

X_train, X_valid, y_train, y_valid = train_test_split(X, y, train_size=0.8, test_size=0.2,random_state=0)


#for logistic regression we do not need numerical data alone but can also use categorical data.
#so we do not have to do an encoding

