## creating a file path and module for reading csv files
import os
import csv

#module for reading csv file
csvpath = os.path.join('Resources', 'budget_data.csv')

#open file in read mode
with open(csvpath, "r") as f:

#csvfile reader with delimiter
    csv_reader = csv.reader(f, delimiter=",")
    
    #skipping the header
    next(f)

    #making iteration for line count ---print outdented with the for statement to print complete total
    LineCount = 0
    TotalSum = 0
    for line in f:
        #print(line)
        LineCount = LineCount + 1
        TotalSum = sum + line[1]
    print(LineCount)
    print(TotalSum)

            
    


    # render object to list 
    #RowList = list(reader)
    

