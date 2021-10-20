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

age = 40
sex = 'F'
th_surgery = 'f'
tsh = 1.30
t3=2.500
tt4 = 125
t4u = 1.140
fti = 109

df = pd.DataFrame({ 
    'age':[age],
    'sex':[sex], 
    'thyroid surgery':[th_surgery], 
    'TSH':[tsh], 
    'T3':[t3],
    'TT4':[tt4],
    'T4U':[t4u], 
    'FTI':[fti]

})
print(predict(df))