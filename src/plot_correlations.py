import pandas as pd
import matplotlib.pyplot as plt
import scipy as sp
import numpy as np


filenames = ['X01_AGE_AND_SEX', 'X02_RACE', 'X03_HISPANIC_OR_LATINO_ORIGIN',\
 'X07_MIGRATION', 'X08_COMMUTING', 'X09_CHILDREN_HOUSEHOLD_RELATIONSHIP',\
 'X11_HOUSEHOLD_FAMILY_SUBFAMILIES', 'X12_MARITAL_STATUS_AND_HISTORY',\
  'X14_SCHOOL_ENROLLMENT', 'X16_LANGUAGE_SPOKEN_AT_HOME', 'X19_INCOME', 'X20_EARNINGS',\
   'X21_VETERAN_STATUS', 'X22_FOOD_STAMPS', 'X23_EMPLOYMENT_STATUS',\
    'X27_HEALTH_INSURANCE', 'X99_IMPUTATION']

dfs = []

plots_per_df = 3

for name in filenames:
    df = pd.read_csv((r'C:\Users\Jonas\Desktop\AIhack\AIHack18\data\processed\correlations\%s_correlation.csv' %name))
    df['origin_file'] = name
    dfs.append(df)

top_correlations = []
min_correlations = []
bottom_correlations = []

for df in dfs:
    df = df[df['Unnamed: 0'].str.contains('Estimate')]
    df = df.dropna()
    top_correlations.append(df[0:plots_per_df])
    bottom_correlations.append(df[-3:])
    min_correlations.append(df.sort_values('abs_correlation', ascending = False)[-3:])

min_correlations[5]

top_labels = []
bottom_labels = []
min_labels = []

top_values = []
bottom_values = []
min_values = []

for df in top_correlations:
    top_labels.append(df['Unnamed: 0'].tolist())
    top_values.append(df['correlation'].tolist())

for df in bottom_correlations:
    bottom_labels.append(df['Unnamed: 0'].tolist())
    bottom_values.append(df['correlation'].tolist())

for df in min_correlations:
    min_labels.append(df['Unnamed: 0'].tolist())
    min_values.append(df['correlation'].tolist())

min_correlations[5]

sorting_df = pd.DataFrame([top_values, top_labels], index=['top_values', 'top_labels']).transpose()
means = []
for i in range(len(sorting_df['top_values'])):
    means.append(np.mean(sorting_df['top_values'][i]))

sorting_df['average_value'] = means
sorted_top_values_df = sorting_df.sort_values('average_value', ascending = False)





bottom_sorting_df = pd.DataFrame([bottom_values, bottom_labels], index=['bottom_values', 'bottom_labels']).transpose()

bottom_means = []
for i in range(len(bottom_sorting_df['bottom_values'])):
    bottom_means.append(np.mean(bottom_sorting_df['bottom_values'][i]))

bottom_sorting_df['average_value'] = bottom_means
sorted_bottom_values_df = bottom_sorting_df.sort_values('average_value', ascending = False)




min_sorting_df = pd.DataFrame([min_values, min_labels], index=['min_values', 'min_labels']).transpose()

min_means = []
for i in range(len(min_sorting_df['min_values'])):
    abs_min_sorting_df = list(map(abs, min_sorting_df['min_values'][i]))
    min_means.append(np.mean(abs_min_sorting_df))

min_sorting_df['average_value'] = min_means
sorted_min_values_df = min_sorting_df.sort_values('average_value', ascending = False)





sorted_bottom_values = []
sorted_bottom_labels = []
sorted_min_values = []
sorted_min_labels = []
sorted_top_values = []
sorted_top_labels = []
sorted_top_values_df
sorted_bottom_values_df

for values in sorted_top_values_df['top_values']:
    for value in values:
        sorted_top_values.append(value)

for values in sorted_bottom_values_df['bottom_values']:
    for value in values:
        sorted_bottom_values.append(value)

for values in sorted_min_values_df['min_values']:
    for value in values:
        sorted_min_values.append(value)


for labels in sorted_top_values_df['top_labels']:
    for label in labels:
        #label = label.split(":", 1)[1].split("--")[0]
        sorted_top_labels.append(label)

for labels in sorted_bottom_values_df['bottom_labels']:
    for label in labels:
        #label = label.split(":", 1)[1].split("--")[0]
        sorted_bottom_labels.append(label)

for labels in sorted_min_values_df['min_labels']:
    for label in labels:
        #label = label.split(":", 1)[1].split("--")[0]
        sorted_min_labels.append(label)


x = sp.linspace(0, 51, 51)
#%%
plt.figure(figsize=(18, 18/1.61))
for i in range(len(sorted_top_values))[0::3]:

    plt.barh(x[i:i+3], sorted_top_values[i:i+3], label = sorted_top_labels[i:i+3])
plt.yticks(x, sorted_top_labels)
plt.show()



#%%
plt.figure(figsize=(18, 18/1.61))
for i in range(len(sorted_bottom_values))[0::3]:

    plt.barh(x[i:i+3], sorted_bottom_values[i:i+3], label = sorted_bottom_labels[i:i+3])
plt.yticks(x, sorted_bottom_labels)
plt.show()

#%%

plt.figure(figsize=(18, 18/1.61))
for i in range(len(sorted_min_values))[0::3]:

    plt.barh(x[i:i+3], sorted_min_values[i:i+3], label = sorted_min_labels[i:i+3])
plt.yticks(x, sorted_min_labels)
plt.show()
