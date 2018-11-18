# Standard python packages
import os
import sys
from pathlib import Path # For portable paths

# Other package imports
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

# Imports for training model
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import mean_squared_error

data_folder = Path("../data/processed")

# Set up x values
inc_df = pd.read_csv(data_folder / "X19_INCOME.csv")
inc_x_data = inc_df["PER CAPITA INCOME IN THE PAST 12 MONTHS (IN 2016
        INFLATION-ADJUSTED DOLLARS): Total: Total population -- (Estimate)"]

# Set up y values
edu_df = pd.read_csv(data_folder / "X15_EDUCATIONAL_ATTAINMENT.csv")
edu_y_data = edu_df["SEX BY AGE BY FIELD OF BACHELOR'S DEGREE FOR FIRST MAJOR FOR THE POPULATION 25 YEARS AND OVER: Total: POPULATION 25 YEARS AND OVER WITH A BACHELOR'S DEGREE OR HIGHER ATTAINMENT -- (Estimate)"]

inc_edu = pd.concat([inc_x_data, edu_y_data], axis=1)
inc_edu.columns = ["Income per capita", "Total bachelor's or higher"]

inc_edu_small = inc_edu[:]
scaler = MinMaxScaler()
x = inc_edu_small["Income per capita"]
y = inc_edu_small["Total bachelor's or higher"]

# Normalise x values
norm_x = scaler.fit_transform(x.values.reshape(-1, 1))
seed = 7
test_size = 0.2

x_train, x_test, y_train, y_test = train_test_split(norm_x, y,
        test_size=test_size, random_state=seed)

print("training data size: {}".format(len(x_train)))

logreg = LogisticRegression(C=1e5, solver='lbfgs', multi_class='multinomial')
logreg.fit(x_train, y_train)

## sklearn.linear_model.LogisticRegressionCV

y_pred = logreg.predict(x_test)
print(y_pred)

mse = mean_squared_error(y_test, y_pred)
print("MSE: {}".format(mse))
