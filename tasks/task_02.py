import pandas as pd
from datetime import date

#Creating a pandas dataframe from the original json
df = pd.read_json("/opt/upskill-projs/assets/covid-data.json")

#Filtering to a smaller dataframe with the days of February 2021
february_2021 = df[(df['date'] > 20210200) & (df['date'] < 20210300)]

#Selecting only the relevant collumns of positive and hospitalized on the February 2021 dataframe
positive_and_hospitalized = february_2021[["positive", "hospitalized"]]

#Defining the path to write the csv to
csv_path = '/opt/upskill-projs/assets/february2021_positive_and_hospitalized'

#Writting the csv
positive_and_hospitalized.to_csv(csv_path, index=False)

#Function that calculates the hospitalization rate on a specific date, on this case, only days
#of February 2021 will be accepted with a YYYY-MM-DD format
def hospitalization_rate():
    date_input = input('Enter a date in YYYY-MM-DD format ')
    year, month, day = map(int, date_input.split('-'))
    first_date = date(2021, 2, 1)
    compare_date = date(year, month, day)

#Verifying the input and getting the values of the positive patients and hospitalized,
#calculating the hospitlization rate and printing it
    if compare_date.year == first_date.year and compare_date.month == first_date.month:
        comparisson_frame = pd.read_csv(csv_path)
        positive_patients = comparisson_frame.iloc[compare_date.day - 1].values[0]
        hospitalized_patients = comparisson_frame.iloc[compare_date.day - 1].values[1]
        rate = round(hospitalized_patients/positive_patients * 100, 2)

        print(f'On {compare_date}, {int(positive_patients)} patients tested positive, '
            f'{int(hospitalized_patients)} got hospitalized, '
            f'making it a {rate}% hospitalization rate for the day.')
#Print string for invalid input formats/invalid dates        
    else:
        print('Incorrect format or invalid date, you can only consult the days of February 2021')

hospitalization_rate()



    





