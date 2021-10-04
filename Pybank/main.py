## creating a file path and module for reading csv files
import os
import csv

#module for reading csv file
csvpath = os.path.join('Resources', 'budget_data.csv')

#open file in read mode
with open(csvpath, "r") as f:

#csvfile reader with delimiter
    reader = csv.reader(f, delimiter=",")
    print(reader)

    # count row since each data set is unique, starting at 2nd row
    data = list(reader)
    RowCount = len(data)
    print(RowCount)
