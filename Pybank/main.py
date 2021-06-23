import os
import csv

#path to collect teh data from the resources folder
budget_csv = os.path.join("..","resources","budget_data.csv")

#list variables
Total_Months = 0
Total_Profit_or_Loss = 0
Monthofchange = []
Net_Change = []
Greatest_Increase = ["",0]
Greatest_Decrease = ["",0]

with open(budget_csv) as csvfile:
    csv_reader=csv.reader(csvfile,delimeter=",")

    #read the header row first
    csv_header=next(csv_reader)
    print(f"Header:{csv_header}")

    #read each row of data after the header
    Firstrow = next(csv_reader)
    Total_Months = Total_Months + 1
    Total_Profit_or_Loss = Total_Profit_or_Loss + int(Firstrow[1])
    Previous_Net = int(Firstrow[1])

    for row in csv_reader:

        Total_Months = Total_Months + 1
        Total_Profit_or_Loss = Total_Profit_or_Loss + int(row[1])


        #Calculate the changes in Profit/Losses, then find the average of the changes
        