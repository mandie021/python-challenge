## creating a file path and module for reading csv files
import os
import csv

#module for reading csv file
csvpath = os.path.join('Resources', 'budget_data.csv')




#open file in read mode
with open(csvpath, "r") as csvfile:

#csvfile reader with delimiter - delimiter did not work so using split in for loop
    csv_reader = csv.reader(csvfile)
    #ListofRows = list(csv_reader)

    #skipping the header
    next(csvfile)
    #print(csv_reader)
    #making iteration for line count ---print outdented with the for statement to print complete total
    LineCount = 0
    TotalSum = 0
    AvChange = 0
    #Row = 0
    
    for line in csvfile:
        line = line.split(',')
        date = line[0]
        profits = int(line[1])
        LineCount = LineCount + 1
        TotalSum = TotalSum + (profits)
        CurLine = int(line[1])
        


    #AvChange = (CurLine + PrvLine)/2
        print(CurLine)
    
    #print(LineCount)
    #print(TotalSum)
    #for row in CurLine:
        #if CurLine != 


       

            
    


    # render object to list 
    #RowList = list(reader)
    

