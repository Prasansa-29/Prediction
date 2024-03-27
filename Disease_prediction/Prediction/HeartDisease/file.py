import pandas as pd
import numpy as np
import csv

import matplotlib.pyplot as plt


class Data():
    df= open('Heart_Disease_Prediction.csv')
    type(df)

    csvreader= csv.reader(df)

    df.columns= ['Age', 'Sex', 'Chestpaintype', 'BloodPressure', 'Cholestrol','FastingBloodSugar', 'ECG', 'MaxHr', 'Excercise_angina', 'ST_depression','Slope_of_ST', 'Number_of_vessels_fluro', 'Thallium', 'Heart_Disease']


    dff= df.drop(df.columns[[6,8,9,10,11]], axis=1)


#Redefining Categorical Variables for Better Understanding
    dff['Sex'][dff['Sex']== 0] = 'female'
    dff['Sex'][dff['Sex']== 1] = 'male'


    Obj_Category= ['Sex', 'Chestpaintype', 'BloodPressure', 'FastingBloodSugar', 'Excercise_angina', 'Slope_of_ST']
    for colname in Obj_Category:
     df[colname] = df[colname].astype('category')
    


    