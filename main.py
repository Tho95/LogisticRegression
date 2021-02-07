# Thomas Hübscher / 07.02
#Example for Logitic Regression for classification of poisonous/edible mushrooms

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OrdinalEncoder

import dataInfo
import plot
import model
import preprocess

filePath = 'mushrooms.csv'
X = pd.read_csv(filePath)

print(X.head())

dataInfo.general(X)
dataInfo.missing_value_per_column(X)
categorical, numerical = dataInfo.colType(X)

#for logistic regression we do not need numerical data alone but can also use categorical data.
#so we just have to encode the target class

ordinal_encoder = OrdinalEncoder(categories=[['e', 'p']])
ordinal_encoder.fit(X[['class']])
y = pd.DataFrame(ordinal_encoder.transform(X[['class']])) #our target variable

X.drop('class', axis = 1, inplace=True) # delte target from dataset

X_cardinality = preprocess.cardinality(X)
print(X_cardinality.columns)
X_train, X_valid, y_train, y_valid = train_test_split(X_cardinality, y, train_size=0.8, test_size=0.2,random_state=0)

model = model.logReg()
#model.fit(X_train, y_train)
#predictions = model.predict(X_valid)
#model.score(X_valid,y_valid)

