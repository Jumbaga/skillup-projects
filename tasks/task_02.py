import pandas as pd

#Creating a pandas dataframe from the original json
df = pd.read_json("/opt/upskill-projs/assets/covid-data.json")

#Filtering to a smaller dataframe with the days of February 2021
february_2021 = df[(df['date'] > 20210200) & (df['date'] < 20210300)]

#Selecting only the relevant collumns of positive and hospitalized on the February 2021 dataframe
positive_and_hospitalized = february_2021[["positive", "hospitalized"]]

#Defining the path to write the csv to
csv_path = '/opt/upskill-projs/assets/february2021_positive_and_hospitalized'

#Writting the csv, no index
positive_and_hospitalized.to_csv(csv_path,index=False)
