import os
import sys
import numpy as np
import pandas as pd
import dill
from src import exception
from sklearn.metrics import r2_score


def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True )
        with open(file_path, "wb") as file_obj:
            dill.dump(obj, file_obj)
    except Exception as e:
        raise exception.CustomException(e, sys)
    


def evaluate_models( x_train,y_train, x_test, y_test, models):
    try:
        report = {}
        #iterating over models 
        for i in range(len(list(models))):

            model = list(models.values())[i]

            model.fit(x_train, y_train) #train model

            y_train_pred = model.predict(x_train)
            y_test_pred = model.predict(x_test)

            train_model_score = r2_score(y_train, y_train_pred)
            test_model_score = r2_score(y_test, y_test_pred)

            report[list(models.keys())[i]] = test_model_score
            
        return report 
    except Exception as e:
        raise exception.CustomException(e, sys)
    
def load_object(file_path):
    try:
        with open(file_path, "rb") as file_obj:
            return dill.load(file_obj)
        
    except Exception as e:
        raise exception.CustomException(e, sys)