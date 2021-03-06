# Thomas Hübscher / 07.02
#Example for Logitic Regression for classification of poisonous/edible mushrooms

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OrdinalEncoder
from sklearn.metrics import confusion_matrix
from sklearn.linear_model import LogisticRegression

import dataInfo
import plot
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

#plot.target(X)
#plot.count(X)
#### with help of the plot we see some information for further preprocessing
print(X['veil-type'].unique())   # just one unique value. Variable can be dropped
X.drop('veil-type', axis = 1, inplace=True)

X.drop('class', axis = 1, inplace=True) # delte target from dataset

###
X_later = X # we will use X_later after we created the first model for some more tests
###
X = preprocess.dummies(X)
print('len',len(X.columns))

X_cardinality = preprocess.cardinality(X)
#print(X_cardinality.columns)
X_train, X_valid, y_train, y_valid = train_test_split(X_cardinality, y, train_size=0.8, test_size=0.2,random_state=0)

model = LogisticRegression()
model.fit(X_train, y_train)
predictions = model.predict(X_valid)
print('\n Logistic Regression Score', model.score(X_valid,y_valid))
print(confusion_matrix(y_valid, predictions))

############################################
#we want to predict the model with less values.
#With help of the plots we can choose some important variables to predict the target...

X_later.drop(['cap-color','cap-shape', 'cap-surface', 'bruises', 'odor', 'gill-attachment',
    'stalk-shape', 'stalk-root', 'veil-color',
    'ring-number', 'ring-type', 'spore-print-color', 'population','habitat'],axis=1, inplace=True)

X = preprocess.dummiesSome(X_later)
#print(len(X.columns))
X_train, X_valid, y_train, y_valid = train_test_split(X, y, train_size=0.8, test_size=0.2,random_state=0)
model = LogisticRegression()
model.fit(X_train, y_train)
predictions = model.predict(X_valid)
print('\n Logistic Regression Score with 8 variables', model.score(X_valid,y_valid))
print(confusion_matrix(y_valid, predictions))
