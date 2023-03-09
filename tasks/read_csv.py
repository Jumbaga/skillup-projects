import pandas as pd

#Function that reads the csv
def csv_read():
#Path to csv file
    csv_path = '/opt/upskill-projs/assets/february2021_positive_and_hospitalized'
#Turning csv to a pandas dataframe
    read_frame = pd.read_csv(csv_path)
#Return the dataframe
    return read_frame