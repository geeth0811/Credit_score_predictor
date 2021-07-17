import numpy as np
import pandas as pd
import copy
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier

#Using the South German Credit (UPDATE) Data Set
#Dataset Link : https://archive.ics.uci.edu/ml/datasets/South+German+Credit+%28UPDATE%29

# define a RandomForestClassifier classifier
clf = RandomForestClassifier(n_estimators = 60, max_depth = 12, random_state = 7)

# define the class encodings and reverse encodings
classes = {0: "Bad Risk", 1: "Good Risk"}
r_classes = {y: x for x, y in classes.items()}

# function to train and load the model during startup
def load_model():
    # load the dataset from the official sklearn datasets
    #X, y = datasets.load_iris(return_X_y=True)
    df = pd.read_csv("SouthGermanCredit/SouthGermanCredit.asc",skiprows=4,encoding="gbk",engine='python',sep=' ',delimiter=None, index_col=False,header=None,skipinitialspace=True)
    last_ix = len(df.columns) - 1
    X, y = df.drop(last_ix, axis=1), df[last_ix]
    # do the test-train split and train the model
    #Splitting the data for training and testing
    X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2) #80% and 20%
    clf.fit(X_train, y_train)

    # calculate and the print the accuracy score
    acc = accuracy_score(y_test, clf.predict(X_test))
    print(f"Model trained with accuracy: {round(acc, 3)}")

# function to predict the Credit score using the model
def predict(query_data):
    x = list(query_data.dict().values())
    prediction = clf.predict([x])[0]
    print(f"Model prediction: {classes[prediction]}")
    return classes[prediction]

# function to retrain the model as part of the feedback loop
def retrain(data):
    # pull out the relevant X and y from the FeedbackIn object
    X = [list(d.dict().values())[:-1] for d in data]
    y = [r_classes[d.Cost_Matrix_Risk] for d in data]
    # fit the classifier again based on the new data obtained
    clf.fit(X, y)
