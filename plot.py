# module for plotting data

import seaborn as sns
import matplotlib.pyplot as plt

#we want to find a way to plot the categorical data

def target(X):
    '''function to plot how often the target variable is p or e'''
    sns.countplot(x='class',data= X)
    plt.title('Number of mushrooms in dataset')
    plt.show()

def count(X):
    '''function to plot the count of the state of variables against the target'''
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




