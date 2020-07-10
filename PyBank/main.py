# Import files
import os
import csv

# Path to open csv file
budget_csv = os.path.join(".", "Resources", "budget_data.csv")

#Lists to store month and profit
month = []
profit = []
change_profit = []


# Open and read csv
with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    budget_header = next(csvfile)
    
    for row in csvreader:
        month.append(row[0])
        profit.append(int(row[1]))

    # Define Change in Profits 
    # (stackoverflow.com/questions/7172933/calculate-difference-between-adjacent-items-in-a-python-list)
    for rows in range(1, len(profit)):        
        diff = int(profit[rows])-int(profit[rows-1]) 
    
    # Append diff to change_profit list
        change_profit.append(diff)

# Definte Outputs
month_count = len(month)
total_profit = sum(profit)
total_change = sum(change_profit)
print(total_change)
average_change = (total_change)/(month_count)
greatest_increase = max(change_profit)
greatest_decrease = min(change_profit)

#Print Summary Table
print(f"Total Months: {month_count}")
print(f"Total: ${(total_profit)}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase: {greatest_increase}")
print(f"Greatest Decrease: {greatest_decrease}")
