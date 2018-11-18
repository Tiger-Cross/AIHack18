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
from sklearn.externals import joblib

filenames = ['X19_INCOME', 'X22_FOOD_STAMPS', 'X03_HISPANIC_OR_LATINO_ORIGIN', 'X27_HEALTH_INSURANCE', 'X11_HOUSEHOLD_FAMILY_SUBFAMILIES']

feature_names = ["AGGREGATE HOUSEHOLD INCOME IN THE PAST 12 MONTHS (IN 2016 INFLATION-ADJUSTED DOLLARS): Total: Households -- (Estimate)","RECEIPT OF FOOD STAMPS/SNAP IN THE PAST 12 MONTHS BY DISABILITY STATUS FOR HOUSEHOLDS: Household did not receive Food Stamps/SNAP in the past 12 months: Households with no persons with a disability: Households -- (Estimate)","HISPANIC OR LATINO ORIGIN BY RACE: Not Hispanic or Latino: Total population -- (Estimate)","TYPES OF HEALTH INSURANCE COVERAGE BY AGE: 35 to 64 years: With one type of health insurance coverage: With employer-based health insurance only: Civilian noninstitutionalized population -- (Estimate)","HOUSEHOLDS BY PRESENCE OF NONRELATIVES: Households with no nonrelatives: Households -- (Estimate)"]

data_folder = Path("../data/processed")

xs = []
for index, name in enumerate(filenames):
    df = pd.read_csv(data_folder / "{}.csv".format(name))
    xs.append(df[feature_names[index]])

print(xs)

# Set up y values
edu_df = pd.read_csv(data_folder / "X15_EDUCATIONAL_ATTAINMENT.csv")
edu_y_data = edu_df["SEX BY AGE BY FIELD OF BACHELOR'S DEGREE FOR FIRST MAJOR FOR THE POPULATION 25 YEARS AND OVER: Total: POPULATION 25 YEARS AND OVER WITH A BACHELOR'S DEGREE OR HIGHER ATTAINMENT -- (Estimate)"]


xs_df = pd.concat(xs, axis=1)
xs_df.columns = ["Income", "Food Stamps", "Hispanic", "Health Insurance", "Household"]

xs_small = xs[:]
scaler = MinMaxScaler()
x = xs_small["Income per capita"]
y = inc_edu_small["Total bachelor's or higher"]

# Normalise x values
norm_x = scaler.fit_transform(x.values.reshape(-1, 1))
seed = 7
test_size = 0.3

x_train, x_test, y_train, y_test = train_test_split(norm_x, y,
        test_size=test_size, random_state=seed)

print("training data size: {}".format(len(x_train)))

logreg = LogisticRegression(C=1e5, solver='lbfgs', multi_class='multinomial',
        n_jobs=-1)
logreg.fit(x_train, y_train)

joblib.dump(logreg, "inc_bach_log_model.dat")

## sklearn.linear_model.LogisticRegressionCV

y_pred = logreg.predict(x_test)
print(y_pred)

mse = mean_squared_error(y_test, y_pred)
print("MSE: {}".format(mse))

plt.scatter(x_test, y_test)
plt.scatter(x_test, y_pred)

plt.savefig("../imgs/inc_bach_pred_log.png")

plt.show()
'''
