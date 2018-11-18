import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import inspect
import os

def find_educational_attainment_correlation(characteristic_csv_filepath, edu_attainment_csv_filepath, truncation_index = False, education_standard = 'bachelors'):
    '''
    education_standard = 'bachelors' or 'masters' or 'higher_education'
    '''



    edu_attainment = pd.read_csv(edu_attainment_csv_filepath)
    characteristic = pd.read_csv(characteristic_csv_filepath)

    no_bachelors = edu_attainment["EDUCATIONAL ATTAINMENT FOR THE POPULATION 25 YEARS AND OVER: Bachelor's degree: Population 25 years and over -- (Estimate)"]
    no_masters = edu_attainment["EDUCATIONAL ATTAINMENT FOR THE POPULATION 25 YEARS AND OVER: Master's degree: Population 25 years and over -- (Estimate)"]
    no_higher_ed = no_masters + no_bachelors

    edu_population = edu_attainment[edu_attainment.columns[3]]
    char_population = characteristic[characteristic.columns[3]]

    if truncation_index == False:
        truncation_index = len(no_masters)

    fractional_bachelors = no_bachelors/edu_population
    fractional_masters = no_masters/edu_population

    if education_standard == 'bachelors':
        y = no_bachelors[0:truncation_index]
    if education_standard == 'masters':
        y = no_masters[0:truncation_index]
    else:
        y = no_higher_ed[0:truncation_index]

    correlations = []
    column_name = []


    for column in characteristic.columns[4:]:
        absolute_x = characteristic[column][0:truncation_index]
        fractional_x = absolute_x/char_population[0:truncation_index]
        correlations.append(np.corrcoef(absolute_x, y)[0][1])
        column_name.append(characteristic[column].name)

    df = pd.DataFrame(correlations, column_name, columns = ['correlation'])
    '''
    returns max correlating factor, all correlations,
    '''

    return df.sort_values('correlation', ascending = False)


poverty_corr = find_educational_attainment_correlation(r'C:\Users\Jonas\Desktop\AIhack\AIHack18\data\processed\X17_POVERTY.csv', r'C:\Users\Jonas\Desktop\AIhack\AIHack18\data\processed\X15_EDUCATIONAL_ATTAINMENT.csv', truncation_index = False, education_standard = 'higher_education')
age_and_sex_corr = find_educational_attainment_correlation(r'C:\Users\Jonas\Desktop\AIhack\AIHack18\data\processed\X01_AGE_AND_SEX.csv', truncation_index = False, education_standard = 'higher_education')
race_corr = find_educational_attainment_correlation(r'C:\Users\Jonas\Desktop\AIhack\AIHack18\data\processed\X02_RACE.csv', r'C:\Users\Jonas\Desktop\AIhack\AIHack18\data\processed\X15_EDUCATIONAL_ATTAINMENT.csv', truncation_index = False, education_standard = 'higher_education')
hispanic_corr = find_educational_attainment_correlation(r'C:\Users\Jonas\Desktop\AIhack\AIHack18\data\processed\X03_HISPANIC_OR_LATINO_ORIGIN.csv', r'C:\Users\Jonas\Desktop\AIhack\AIHack18\data\processed\X15_EDUCATIONAL_ATTAINMENT.csv', truncation_index = False, education_standard = 'higher_education')
migration_corr = find_educational_attainment_correlation(r'C:\Users\Jonas\Desktop\AIhack\AIHack18\data\processed\X07_MIGRATION.csv', r'C:\Users\Jonas\Desktop\AIhack\AIHack18\data\processed\X15_EDUCATIONAL_ATTAINMENT.csv', truncation_index = False, education_standard = 'higher_education')
commuting_corr = find_educational_attainment_correlation(r'C:\Users\Jonas\Desktop\AIhack\AIHack18\data\processed\X08_COMMUTING.csv', r'C:\Users\Jonas\Desktop\AIhack\AIHack18\data\processed\X15_EDUCATIONAL_ATTAINMENT.csv', truncation_index = False, education_standard = 'higher_education')
children_household_relationship_corr = find_educational_attainment_correlation(r'C:\Users\Jonas\Desktop\AIhack\AIHack18\data\processed\X09_CHILDREN_HOUSEHOLD_RELATIONSHIP.csv', r'C:\Users\Jonas\Desktop\AIhack\AIHack18\data\processed\X15_EDUCATIONAL_ATTAINMENT.csv', truncation_index = False, education_standard = 'higher_education')
household_family_subfamilies_corr = find_educational_attainment_correlation(r'C:\Users\Jonas\Desktop\AIhack\AIHack18\data\processed\X11_HOUSEHOLD_FAMILY_SUBFAMILIES.csv', r'C:\Users\Jonas\Desktop\AIhack\AIHack18\data\processed\X15_EDUCATIONAL_ATTAINMENT.csv', truncation_index = False, education_standard = 'higher_education')
marital_status_corr = find_educational_attainment_correlation(r'C:\Users\Jonas\Desktop\AIhack\AIHack18\data\processed\X12_MARITAL_STATUS_AND_HISTORY.csv', r'C:\Users\Jonas\Desktop\AIhack\AIHack18\data\processed\X15_EDUCATIONAL_ATTAINMENT.csv', truncation_index = False, education_standard = 'higher_education')
enrollment_corr = find_educational_attainment_correlation(r'C:\Users\Jonas\Desktop\AIhack\AIHack18\data\processed\X14_SCHOOL_ENROLLMENT.csv', r'C:\Users\Jonas\Desktop\AIhack\AIHack18\data\processed\X15_EDUCATIONAL_ATTAINMENT.csv', truncation_index = False, education_standard = 'higher_education')
language_spoken_at_home_corr = find_educational_attainment_correlation(r'C:\Users\Jonas\Desktop\AIhack\AIHack18\data\processed\X16_LANGUAGE_SPOKEN_AT_HOME.csv', r'C:\Users\Jonas\Desktop\AIhack\AIHack18\data\processed\X15_EDUCATIONAL_ATTAINMENT.csv', truncation_index = False, education_standard = 'higher_education')
income_corr = find_educational_attainment_correlation(r'C:\Users\Jonas\Desktop\AIhack\AIHack18\data\processed\X19_INCOME.csv', r'C:\Users\Jonas\Desktop\AIhack\AIHack18\data\processed\X15_EDUCATIONAL_ATTAINMENT.csv', truncation_index = False, education_standard = 'higher_education')
earnings_corr = find_educational_attainment_correlation(r'C:\Users\Jonas\Desktop\AIhack\AIHack18\data\processed\X20_EARNINGS.csv', r'C:\Users\Jonas\Desktop\AIhack\AIHack18\data\processed\X15_EDUCATIONAL_ATTAINMENT.csv', truncation_index = False, education_standard = 'higher_education')
veteran_status_corr = find_educational_attainment_correlation(r'C:\Users\Jonas\Desktop\AIhack\AIHack18\data\processed\X21_VETERAN_STATUS.csv', r'C:\Users\Jonas\Desktop\AIhack\AIHack18\data\processed\X15_EDUCATIONAL_ATTAINMENT.csv', truncation_index = False, education_standard = 'higher_education')
food_stamps_corr = find_educational_attainment_correlation(r'C:\Users\Jonas\Desktop\AIhack\AIHack18\data\processed\X22_FOOD_STAMPS.csv', r'C:\Users\Jonas\Desktop\AIhack\AIHack18\data\processed\X15_EDUCATIONAL_ATTAINMENT.csv', truncation_index = False, education_standard = 'higher_education')
employment_status_corr = find_educational_attainment_correlation(r'C:\Users\Jonas\Desktop\AIhack\AIHack18\data\processed\X23_EMPLOYMENT_STATUS.csv', r'C:\Users\Jonas\Desktop\AIhack\AIHack18\data\processed\X15_EDUCATIONAL_ATTAINMENT.csv', truncation_index = False, education_standard = 'higher_education')
health_insurance_corr = find_educational_attainment_correlation(r'C:\Users\Jonas\Desktop\AIhack\AIHack18\data\processed\X27_HEALTH_INSURANCE.csv', r'C:\Users\Jonas\Desktop\AIhack\AIHack18\data\processed\X15_EDUCATIONAL_ATTAINMENT.csv', truncation_index = False, education_standard = 'higher_education')
imputation = find_educational_attainment_correlation(r'C:\Users\Jonas\Desktop\AIhack\AIHack18\data\processed\X99_IMPUTATION.csv', r'C:\Users\Jonas\Desktop\AIhack\AIHack18\data\processed\X15_EDUCATIONAL_ATTAINMENT.csv', truncation_index = False, education_standard = 'higher_education')
