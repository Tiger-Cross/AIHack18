# Standard python packages
import functools
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
from sklearn.externals import joblib

data_folder = Path("../data/processed")

# Set up x values
#inc_df = pd.read_csv(data_folder / "X19_INCOME.csv")
#inc_x_data = inc_df["PER CAPITA INCOME IN THE PAST 12 MONTHS (IN 2016 INFLATION-ADJUSTED DOLLARS): Total: Total population -- (Estimate)"]

# Set up y values
edu_df = pd.read_csv(data_folder / "X15_EDUCATIONAL_ATTAINMENT.csv")
edu_y_data = edu_df["SEX BY AGE BY FIELD OF BACHELOR'S DEGREE FOR FIRST MAJOR FOR THE POPULATION 25 YEARS AND OVER: Total: POPULATION 25 YEARS AND OVER WITH A BACHELOR'S DEGREE OR HIGHER ATTAINMENT -- (Estimate)"]

# Create x and y panda
#inc_edu = pd.concat([inc_x_data, edu_y_data], axis=1)
#inc_edu.columns = ["Income per capita", "Total bachelor's or higher"]


####

# Prepare multi-dim inputs
filenames = ['X19_INCOME', 'X22_FOOD_STAMPS', 'X03_HISPANIC_OR_LATINO_ORIGIN', 'X27_HEALTH_INSURANCE', 'X11_HOUSEHOLD_FAMILY_SUBFAMILIES']

feature_names = ["AGGREGATE HOUSEHOLD INCOME IN THE PAST 12 MONTHS (IN 2016 INFLATION-ADJUSTED DOLLARS): Total: Households -- (Estimate)","RECEIPT OF FOOD STAMPS/SNAP IN THE PAST 12 MONTHS BY DISABILITY STATUS FOR HOUSEHOLDS: Household did not receive Food Stamps/SNAP in the past 12 months: Households with no persons with a disability: Households -- (Estimate)","HISPANIC OR LATINO ORIGIN BY RACE: Not Hispanic or Latino: Total population -- (Estimate)","TYPES OF HEALTH INSURANCE COVERAGE BY AGE: 35 to 64 years: With one type of health insurance coverage: With employer-based health insurance only: Civilian noninstitutionalized population -- (Estimate)","HOUSEHOLDS BY PRESENCE OF NONRELATIVES: Households with no nonrelatives: Households -- (Estimate)"]

# array of inputs
xs = []
for index, name in enumerate(filenames):
    df = pd.read_csv(data_folder / "{}.csv".format(name))
    xs.append(df)

df = functools.reduce(lambda x, y: pd.merge(x, y, on="GEOID"), xs)


# Shrink x and y panda
scaler = MinMaxScaler()
x = df.iloc[:, 3:]
#print(x.iloc[:, 3:])
y = edu_y_data
#print(y)

# Normalise x values
norm_x = scaler.fit_transform(x)
seed = 7
test_size = 0.2

# Separate x and y into training values
x_train, x_test, y_train, y_test = train_test_split(norm_x, y,
        test_size=test_size, random_state=seed)

print("training data size: {}".format(len(x_train)))

model = XGBClassifier(n_jobs=-1, verbose_eval=True)
model.fit(x_train, y_train, verbose=True)
joblib.dump(model, "multi_input_xgboost_model.dat")

y_pred = model.predict(x_test)
#print(y_pred)

mse = mean_squared_error(y_test, y_pred)
print("MSE: {}".format(mse))

for i in range(5):
	plt.scatter(x_test[i], y_test)
	plt.scatter(x_test[i], y_pred)
	plt.savefig("../imgs/multi_boost/multi_input_xgboost" + i + ".png")

plt.show()
