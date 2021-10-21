import pickle
import numpy as np
import pandas as pd

model = pickle.load(open('thyroid.pkl', 'rb'))
sex_encod = pickle.load(open('sex_lbl.pkl', 'rb'))
scaler = pickle.load(open('scalar.pkl', 'rb'))
surgery_encod= pickle.load(open('surgery.pkl', 'rb'))
class_names = ['Negative','Positive']

def predict(df):
    df = df[['age', 'sex', 'thyroid surgery', 'TSH', 'T3', 'TT4', 'T4U', 'FTI']]
    df.sex = sex_encod.transform(df.sex)
    df['thyroid surgery'] = surgery_encod.transform(df['thyroid surgery'])
    df['age'] = scaler.transform(df[['age']])
    df.TT4 = scaler.transform(df[['TT4']])
    df.FTI = scaler.transform(df[['FTI']])
    numpy_array = df.to_numpy()
    predictions = model.predict(numpy_array)
    output = [class_names[class_predicted] for class_predicted in predictions]
    return output

