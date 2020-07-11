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
    
    # Append month and profit data into lists
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
month_count = len(month) - 1
total_profit = sum(profit)
total_change = sum(change_profit)
average_change = round((total_change)/(month_count), 2)

# Find greatest increase in profits & month
greatest_increase = max(change_profit)
gi_index = change_profit.index(greatest_increase)

# Find greatest decrease in profits & month
greatest_decrease = min(change_profit)
gd_index =  change_profit.index(greatest_decrease)


# Create Summary Table    
print("----------------------------")
print("     Financial Analysis     ")
print("----------------------------")
print(f"Total Months: {len(month)}")
print(f"Total: ${(total_profit)}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase: {month[gi_index+1]}  {greatest_increase}")
print(f"Greatest Decrease: {month[gd_index+1]} {greatest_decrease}")

#Set output file
output_file =  os.path.join("Analysis", "bank_final.txt")

# Export Data
with open(output_file, "w") as textfile:
    
    textfile.write("----------------------------\n")
    textfile.write("     Financial Analysis     \n")
    textfile.write("----------------------------\n")
    textfile.write(f"Total Months: {len(month)} \n")
    textfile.write(f"Total: ${(total_profit)} \n")
    textfile.write(f"Average Change: ${average_change} \n")
    textfile.write(f"Greatest Increase: {month[gi_index+1]}  {greatest_increase} \n")
    textfile.write(f"Greatest Decrease: {month[gd_index+1]} {greatest_decrease} \n")


