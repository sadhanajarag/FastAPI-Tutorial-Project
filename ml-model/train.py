import joblib
import pandas as pd
from sklearn.linear_model import LinearRegression

df = pd.read_csv(r'C:\DS_Material\FastAPI_Material\venv\ml-model\housing.csv').iloc[:, :-1].dropna()
print('Read the dataset')

X = df.drop(columns='median_house_value')
y = df.median_house_value.copy()
print('Split the dataset')

model = LinearRegression().fit(X, y)
print('Trained the Model')

joblib.dump(model, 'model.joblib')
print('Saved the Model')