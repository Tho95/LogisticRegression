# module for plotting data

# module for plotting the data

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import OrdinalEncoder

#we want to find a way to plot the categorical data
def countplot(X,y):
    '''Function for plotting the variables of input X against the target y'''

    #we want to use ordinalencoder to encode class variable to numeric value
    '''
    ordinal_encoder = OrdinalEncoder(categories=[['e', 'p']])
    ordinal_encoder.fit(X[['class']])
    y_encoded = pd.DataFrame(ordinal_encoder.transform(X[['class']]))
   
    sns.regplot(ax=axes[0,1], x = 'children', y=y, data = X);

    sns.regplot(ax=axes[1,0], x='age', y=y, data=X);

    sns.regplot(ax=axes[1,1], x='age', y=y, data=X);


    ###### encoding of ordinal data
    ordinal_encoder = OrdinalEncoder(categories=[['no', 'yes']])
    ordinal_encoder.fit(X[['smoker']])
    smoker_encoded = pd.DataFrame(ordinal_encoder.transform(X[['smoker']]))
######
    sns.regplot(ax=axes[0,2], x=smoker_encoded, y=y);
    axes[0,2].set_xlabel('smoker(0:No, 1:Yes]')

    ordinal_encoder1 = OrdinalEncoder(categories=[['female', 'male']])
    ordinal_encoder1.fit(X[['sex']])
    sex_encoded = pd.DataFrame(ordinal_encoder1.transform(X[['sex']]))

    sns.regplot(ax=axes[1, 2], x=sex_encoded, y=y);
    axes[1, 2].set_xlabel('sex(0:f, 1:m]')
    axes[1, 2].set_xlim(0,1)
    axes[1, 2].set_ylim(0, 60000)
    '''
    plt.show()

def target(X):
    #y.value_counts()
    sns.countplot(x='class',data= X)
    plt.title('Number of mushrooms in dataset')
    plt.show()

def count(X):
    fig, axes = plt.subplots(2, 4, figsize=(16, 8))
    fig.suptitle('poisonous or edible mushrooms')

    sns.countplot(ax= axes[0,0],x='cap-shape', hue = 'class', data = X)

    sns.countplot(ax=axes[0, 1], x='cap-surface', hue='class', data=X)

    sns.countplot(ax=axes[0, 2], x='cap-color', hue='class', data=X)

    sns.countplot(ax=axes[1, 0], x='gill-color', hue='class', data=X)

    sns.countplot(ax=axes[1, 1], x='gill-attachment', hue='class', data=X)

    sns.countplot(ax=axes[1, 2], x='gill-size', hue='class', data=X)

    sns.countplot(ax=axes[1, 3], x='gill-spacing', hue='class', data=X)
    plt.show()

    fig, axes = plt.subplots(2, 3, figsize=(16, 8))
    fig.suptitle('poisonous or edible mushrooms')

    sns.countplot(ax=axes[0, 0], x='stalk-shape', hue='class', data=X)

    sns.countplot(ax=axes[0, 1], x='stalk-root', hue='class', data=X)

    sns.countplot(ax=axes[0, 2], x='stalk-surface-above-ring', hue='class', data=X)

    sns.countplot(ax=axes[1, 0], x='stalk-surface-below-ring', hue='class', data=X)

    sns.countplot(ax=axes[1, 1], x='stalk-color-above-ring', hue='class', data=X)

    sns.countplot(ax=axes[1, 2], x='stalk-color-below-ring', hue='class', data=X)
    plt.show()

    fig, axes = plt.subplots(2, 3, figsize=(16, 8))
    fig.suptitle('poisonous or edible mushrooms')

    sns.countplot(ax=axes[0, 0], x='ring-number', hue='class', data=X)

    sns.countplot(ax=axes[0, 1], x='ring-type', hue='class', data=X)

    sns.countplot(ax=axes[0, 2], x='spore-print-color', hue='class', data=X)

    sns.countplot(ax=axes[1, 0], x='population', hue='class', data=X)

    sns.countplot(ax=axes[1, 1], x='habitat', hue='class', data=X)

    sns.countplot(ax=axes[1, 2], x='odor', hue='class', data=X)
    plt.show()

    fig, axes = plt.subplots(2, 3, figsize=(16, 8))
    fig.suptitle('poisonous or edible mushrooms')

    sns.countplot(ax=axes[0, 0], x='bruises', hue='class', data=X)

    sns.countplot(ax=axes[0, 1], x='veil-type', hue='class', data=X)

    sns.countplot(ax=axes[0, 2], x='veil-color', hue='class', data=X)
    plt.show()




