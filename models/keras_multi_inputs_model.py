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

# keras
from keras.layers import Input
from keras.layers import Dense
from keras.models import Model
from keras.utils import plot_model

# Prepare multi-dim input
filenames = ['X19_INCOME', 'X22_FOOD_STAMPS', 'X03_HISPANIC_OR_LATINO_ORIGIN', 'X27_HEALTH_INSURANCE', 'X11_HOUSEHOLD_FAMILY_SUBFAMILIES']

feature_names = ["AGGREGATE HOUSEHOLD INCOME IN THE PAST 12 MONTHS (IN 2016 INFLATION-ADJUSTED DOLLARS): Total: Households -- (Estimate)","RECEIPT OF FOOD STAMPS/SNAP IN THE PAST 12 MONTHS BY DISABILITY STATUS FOR HOUSEHOLDS: Household did not receive Food Stamps/SNAP in the past 12 months: Households with no persons with a disability: Households -- (Estimate)","HISPANIC OR LATINO ORIGIN BY RACE: Not Hispanic or Latino: Total population -- (Estimate)","TYPES OF HEALTH INSURANCE COVERAGE BY AGE: 35 to 64 years: With one type of health insurance coverage: With employer-based health insurance only: Civilian noninstitutionalized population -- (Estimate)","HOUSEHOLDS BY PRESENCE OF NONRELATIVES: Households with no nonrelatives: Households -- (Estimate)"]

data_folder = Path("../data/processed")

# Set up y values
edu_df = pd.read_csv(data_folder / "X15_EDUCATIONAL_ATTAINMENT.csv")
edu_y_data = edu_df["SEX BY AGE BY FIELD OF BACHELOR'S DEGREE FOR FIRST MAJOR FOR THE POPULATION 25 YEARS AND OVER: Total: POPULATION 25 YEARS AND OVER WITH A BACHELOR'S DEGREE OR HIGHER ATTAINMENT -- (Estimate)"]

# array of inputs
xs = []
for index, name in enumerate(filenames):
    df = pd.read_csv(data_folder / "{}.csv".format(name))
    xs.append(df[feature_names[index]])

print(xs)

### Returns a trained model. Args: shape of one input, the array of inputs, the Ys (?)
def keraModel(single_input_shape, inputs_array, y_train):
	# Define dimension of input
	inputs = []
	for i in range(5):
		inputs.append(Input(shape=single_input_shape))

	# creating hidden outputs
	'''
	hidden1 = Dense(10, activation='relu')(merge)
	hidden2 = Dense(20, activation='relu')(hidden1)
	hidden3 = Dense(10, activation='relu')(hidden2)
	output = Dense(1, activation='sigmoid')(hidden3)
	'''
	regs = []
	for i in range(5):
		 regs.append(LSTM(40,return_sequences=False)(x[i]))

	out = concatenate(regs)

	print(out)

	# Creating output. activation='sigmoid' (?)
	output = Dense(1, activation='sigmoid')(out)

	# Create model
	model = Model(inputs=inputs, outputs=output)

	model.compile(optimizer='rmsprop', loss='binary_crossentropy') # ?

	# summarize layers
	print(model.summary())

	return model.fit(inputs_array, y_train, verbose=True, epochs=10)

keraModel(xs[0].shape, xs, edu_y_data)


# plot graph
# plot_model(model, to_file='multi_input_model.png')