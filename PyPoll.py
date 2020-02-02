#add our dependencies
import csv
import os
#Assign a variable for the file to load and the path.
file_to_load = os.path.join("..","Election_Analysis","election_results.csv")
#Assign a variable to save the file to a path
file_to_save = os.path.join("..","Election_Analysis","analysis","election_analysis.txt")

#Open the election results and read the file.
with open(file_to_load) as election_data:
#read the file object with the reader function
    file_reader = csv.reader(election_data)
#print each row in the csv file.
    headers= next(file_reader)
    print(headers)


