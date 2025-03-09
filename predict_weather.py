import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
from config import cleaned_data_file

def train_temperature_model():
	"""Train a simple linear regression model to predict future temperatures"""
	df = pd.read_csv(cleaned_data_file)
	df["date"] = pd.to_datetime(df["date"])
	df["day_of_year"] = df["date"].dt.dayofyear
    
	X = df[["day_of_year"]]
	y = df["temp_day"]
    
	X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
	model = LinearRegression()
	model.fit(X_train, y_train)
    
	y_pred = model.predict(X_test)
	mae = mean_absolute_error(y_test, y_pred)
	print(f"Model trained. MAE: {mae:.2f}°C")
    
	return model

if __name__ == "__main__":
	train_temperature_model()
