# Standard python packages
import os
import sys
from pathlib import Path # For portable paths

# Other package imports
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

# Imports for training model
from xgboost import XGBClassifier
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

data_folder = Path("../data/processed")

# Set up x values
hisp_df = pd.read_csv(data_folder / "X03_HISPANIC_OR_LATINO_ORIGIN.csv")
hisp_x_data = hisp_df["HISPANIC OR LATINO ORIGIN BY RACE: Not Hispanic or Latino: Total population -- (Estimate)"] 

# Set up y values
edu_df = pd.read_csv(data_folder / "X15_EDUCATIONAL_ATTAINMENT.csv")
edu_y_data = edu_df["SEX BY AGE BY FIELD OF BACHELOR'S DEGREE FOR FIRST MAJOR FOR THE POPULATION 25 YEARS AND OVER: Total: POPULATION 25 YEARS AND OVER WITH A BACHELOR'S DEGREE OR HIGHER ATTAINMENT -- (Estimate)"]

hisp_edu = pd.concat([hisp_x_data, edu_y_data], axis=1)
hisp_edu.columns = ["Total non-hispanic citizens", "Total bachelor's or higher"]

hisp_edu_small = hisp_edu[:]
scaler = MinMaxScaler()
x = hisp_edu_small["Total non-hispanic citizens"]
y = hisp_edu_small["Total bachelor's or higher"]

# Normalise x values
norm_x = scaler.fit_transform(x.values.reshape(-1, 1))
seed = 7
test_size = 0.2

x_train, x_test, y_train, y_test = train_test_split(norm_x, y,
        test_size=test_size, random_state=seed)

print("training data size: {}".format(len(x_train)))

model = XGBClassifier(n_jobs=-1, verbose_eval=True)
model.fit(x_train, y_train, verbose=True)

y_pred = model.predict(x_test)
print(y_pred)

mse = mean_squared_error(y_test, y_pred)
print("MSE: {}".format(mse))
