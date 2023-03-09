from read_csv import csv_read
from matplotlib import pyplot as plt

#Storing the dataframe we are going to use on a variable using the method we imported
#from read_csv.py 
df = csv_read()

#Transforming the columns positive and hospitalized from the dataframe to lists to plot with
# and creating a list for the days in February for the same reason
positives_lst = df["positive"].values.tolist()
hospitalized_lst = df["hospitalized"].values.tolist()
february_days = [*range(1, 29, 1)]

#Ploting as planned using the positve patients and hospitalized ones with respect to days of February
#added labels and legend
plt.plot(february_days, positives_lst, label = "COV-19 positive patients")
plt.plot(february_days, hospitalized_lst, label = "Hospitalized patients")
plt.legend()
plt.xlabel("Days of February 2021")
plt.ylabel("Patients")
#Showing the plot
plt.show()