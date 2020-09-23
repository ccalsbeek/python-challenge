#Dependencies
import os
import csv

#define variables
months = 0

net_profitloss = 0
profit = 0
profit_log = []

totalchange = 0
change = 0
avg_change = 0

gincrease = "0"
gdecrease = "0"
i_month = ""
d_month = ""

#define path to csv data
path = os.path.join("Resources", "budget_data.csv")

#read csv
with open (path) as budget_data:
    data = csv.reader(budget_data)
    
    #skip header
    header = next(data)
    #set condition to skip first row in looping
    skip = True

    #start for loop to iterate through rows
    for row in data:
        #skip first row and set skip to False for loop calcs
        if skip is True:
            profit = int(row[1])
            skip = False

        #start counters and calcs
         #calculate total months
        months += 1  # <--add month for each loop
         #calculate total profits and losses
        net_profitloss += profit  # <-- totals profits and losses each loop
        profit_log = int(row[1])  # <-- tracks profits
        date = str(row[0])  # <-- tracks month 
        change = profit_log - profit  # <-- tracks changes between months

         #calculate greatest increase in profits/losses
        if float(gincrease) < change:  # <-- stores value of change if it's larger than gincrease variable
            gincrease = change
            i_month = date

         #calculate greatest decrease in profits/losses
        if float(gdecrease) > change:
            gdecrease = change
            d_month = date
        
        totalchange += change  # <-- tracks total for avg calc
        profit = profit_log  # <-- sets value for next loop

#Calculate average change
avg_change = totalchange / (months - 1)

#print and save analysis output
output = (
    f"Financial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {months}\n" 
    f"Total Profits: ${net_profitloss}\n"
    f"Average Change: $ {avg_change:.2f}\n"
    f"Greatest Increase: {i_month} (${gincrease})\n"
    f"Greatest Decrease: {d_month} (${gdecrease})\n"
        )

print(output)

o_path = os.path.join("Analysis", "budget_analysis.txt")

with open(o_path, "w") as analysis:
    analysis.write(output)



