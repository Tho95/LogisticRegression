# a module for preprocessing the data

def cardinality(X):
    '''This function gets a DataFrame and return only those columns with Cardinality < 2 (binary)'''
    x_binary_cols= [cname for cname in X.columns if X[cname].nunique() < 10]
    print("binary columns: ", len(x_binary_cols))
    non_binary_cols = list(set(X.columns)-set(x_binary_cols))  #
    print("non-binary columns: ", non_binary_cols)
    X.drop(non_binary_cols, axis = 1, inplace=True) # delte non_binary columns from dataset
    return X

def oneHot(X):
    pass
