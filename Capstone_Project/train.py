import pickle

import pandas as pd

from sklearn.linear_model import LinearRegression




data = pd.read_csv("https://raw.githubusercontent.com/LygutaKsusha/MLZoomCamp/blob/main/Datasets/Admission_Predict.csv")

data = data.drop("Serial No.", axis=1)

x = data.drop('Chance of Admit ', axis=1)
y = data['Chance of Admit ']

model = LinearRegression(normalize=True)
model.fit(x, y)
print("Model has been trained")

pickle.dump(model, open('prediction.sav', 'wb') )
print("Model has been saved")

