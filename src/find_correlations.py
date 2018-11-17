import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def find_educational_attainment_correlation(csv_filepath, truncation_index, education_standard = 'bachelors'):
    '''
    education_standard = 'bachelors' or 'masters'
    '''
    edu_attainment = pd.read_csv(r'C:\Users\Jonas\Desktop\AIhack\data\long_names\edu_attainment.csv')
    characteristic = pd.read_csv(csv_filepath)

    no_bachelors = edu_attainment["EDUCATIONAL ATTAINMENT FOR THE POPULATION 25 YEARS AND OVER: Bachelor's degree: Population 25 years and over -- (Estimate)""]
    no_masters = edu_attainment["EDUCATIONAL ATTAINMENT FOR THE POPULATION 25 YEARS AND OVER: Master's degree: Population 25 years and over -- (Estimate)"]

    edu_population = edu_attainment[edu_attainment.columns[3]]
    char_population = characteristic[characteristic.columns[3]]

    fractional_bachelors = no_bachelors/edu_population
    fractional_masters = no_masters/edu_population

    if education_standard == 'bachelors':
        y = fractional_bachelors[0:truncation_index]
    if education_standard == 'masters':
        y = fractional_masters[0:truncation_index]

    correlations = []

    for column in characteristic.columns[4:]:
        absolute_x = characteristic[column]
        fractional_x = absolute_x[0:truncation_index]/char_population[0:truncation_index]
        correlations.append(np.corrcoef(fractional_x, y)[0][1])

        '''
        returns max correlating factor, all correlations,
        '''
    return [poverty[poverty.columns[correlations.index(max(correlations))]].name, correlations]

find_educational_attainment_correlation(r'C:\Users\Jonas\Desktop\AIhack\data\long_names\poverty.csv', 285, education_standard = 'bachelors')
#%%
N = 285

edu_attainment = pd.read_csv(r'C:\Users\Jonas\Desktop\AIhack\data\long_names\edu_attainment.csv')
poverty = pd.read_csv(r'C:\Users\Jonas\Desktop\AIhack\data\long_names\poverty.csv')

no_bachelors = edu_attainment['EDUCATIONAL ATTAINMENT FOR THE POPULATION 25 YEARS AND OVER: Bachelors degree: Population 25 years and over -- (Estimate)']
no_masters = edu_attainment['EDUCATIONAL ATTAINMENT FOR THE POPULATION 25 YEARS AND OVER: Masters degree: Population 25 years and over -- (Estimate)']
population = edu_attainment['EDUCATIONAL ATTAINMENT FOR THE POPULATION 25 YEARS AND OVER: Total: Population 25 years and over -- (Estimate)']

fractional_bachelors = no_bachelors/population
fractional_masters = no_masters/population
y = fractional_bachelors[0:N]
#y = fractional_masters[0:N]
#poverty['RATIO OF INCOME TO POVERTY LEVEL IN THE PAST 12 MONTHS: Total: Population for whom poverty status is determined -- (Estimate)']

correlations = []
column = poverty.columns[10]



for column in poverty.columns[4:]:
    absolute_x = poverty[column]
    fractional_x = absolute_x[0:N]/poverty['RATIO OF INCOME TO POVERTY LEVEL IN THE PAST 12 MONTHS: Total: Population for whom poverty status is determined -- (Estimate)'][0:N]
    correlations.append(np.corrcoef(fractional_x, y)[0][1])

print(correlations[13])
print(poverty[poverty.columns[correlations.index(max(correlations))]])

plt.plot(fractional_x, y, 'x')
plt.show()
