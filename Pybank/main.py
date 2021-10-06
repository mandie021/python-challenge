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

#print(MonChange)
Duration = len(AvMonChangelist)
total = sum(AvMonChangelist)
ProfitAverage = total/Duration
#print(ProfitAverage)

#finding min max and corrisponding month
MonGincrease = ''
AmoGincrease = 0
MonGdecrease = ''
AmoGdecrease = 0

for i in range(len(AvMonChangelist)):
    if AvMonChangelist [i] > AmoGincrease:
        AmoGincrease = AvMonChangelist[i]
        MonGincrease = monthlist[i +1]
    elif AvMonChangelist[i] < AmoGdecrease:
        MonGdecrease = monthlist[i +1]
        AmoGdecrease = AvMonChangelist[i]
#print(AmoGdecrease)
#print(MoGincrease)

#to print the text to terminal
print("Financial Analysis")
print("----------------------")
print(f'Total Months:  {TotalMonths}')
print(f'Total Profits/Losses:  {TotalProfits}')
print(f'Greatest Increase in Profits:  {MonGincrease}  {(AmoGincrease)}')
print(f'Greatest Decrease in Profits:  {MonGdecrease}  {(AmoGdecrease)}')

    

