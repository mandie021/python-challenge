## creating a file path and module for reading csv files
import os
import csv

#module for reading csv file
csvpath = os.path.join('Resources', 'budget_data.csv')

#make lists
monthlist = []
profitlist = []


#open file in read mode
with open(csvpath, "r") as csvfile:

#csvfile reader with delimiter - delimiter did not work so using split in for loop
    csv_reader = csv.reader(csvfile)
    
    #skipping the header
    next(csvfile)
    #print(csv_reader)  

    for row in csv_reader:
        monthlist.append(row[0])
        profitlist.append(int(row[1]))
    #print(monthlist)
#getting the total months
TotalMonths = len(monthlist)

#net the profits
TotalProfits = 0

for i in profitlist:
    TotalProfits = TotalProfits + i
#print(TotalProfits)

#average change
AvMonChangelist= []
PrvMonAmount = 0

for i in range(len(profitlist)):
    if i == 0:
        PrvMonAmount = profitlist[i]
    else:
        MonChange = profitlist[i] - PrvMonAmount
        AvMonChangelist.append(MonChange)
        PrvMonAmount = profitlist[i]

#print monthly changes
Duration = len(AvMonChangelist)
total = sum(AvMonChangelist)
ProfitAverage = total/Duration
#print(ProfitAverage)

#finding min max and corrisponding month


