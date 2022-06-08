import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from .packages import packages, packages2

model = DecisionTreeClassifier()

def first_model():
    dataset = packages

    dataframe = pd.DataFrame(dataset)
    X = dataframe.drop(columns = ["package"])
    y = dataframe["package"]

    model.fit(X, y)

first_model()

def prediction(vcpu, ram, storage_type, storage_amount, network_bandwidth, processor):
    output = model.predict( [ [vcpu, ram, storage_type, storage_amount, network_bandwidth, processor] ] )
    required_value = output[0]
    return required_value-1

model2 = DecisionTreeClassifier()

def second_model():
    dataset2 = packages2

    dataframe2 = pd.DataFrame(dataset2)
    X2 = dataframe2.drop(columns = ["package"])
    y2 = dataframe2["package"]

    model2.fit(X2, y2)

second_model()

def prediction2(company_size, hits):
    output = model2.predict( [ [company_size, hits] ] )
    required_value = output[0]
    return required_value-1