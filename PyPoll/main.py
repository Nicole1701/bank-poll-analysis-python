# Import files
import os
import csv


# Path to open csv file
budget_csv = os.path.join(".", "Resources", "election_data.csv")

# Create lists/dictionary to hold values
total_votes = 0
candidate_list = []
candidate_count = {}

# Open and read csv
with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    poll_header = next(csvfile)

    # Add up the total number of votes   
    for row in csvreader:
        total_votes += 1  

        # Count up votes per candidate and place in dictionary
        if row[2] not in candidate_list:
            candidate_list.append(row[2])
            candidate_count[row[2]] = 1
        else:
            candidate_count[row[2]] += 1
    
#Determine winner
#www.geeksforgeeks.org/python-get-key-with-maximum-value-in-dictionary/
winner = max(candidate_count, key=candidate_count.get) 

# Summary Table
print("----------------------------")
print("      Election Results      ")
print("----------------------------")
print(f"Total Votes: {total_votes}")
print("----------------------------")
for candidate, votes in candidate_count.items():
    print(f"{candidate}: {((votes/total_votes)*100):.3f}% ({(candidate_count[candidate])})")
print("----------------------------")
print(f"Winner: {winner}")
print("----------------------------")

#Set output file
output_file =  os.path.join("Analysis", "poll_final.txt")

# Export Data
with open(output_file, "w") as textfile:
    
    textfile.write("----------------------------\n")
    textfile.write("      Election Results      \n")
    textfile.write("----------------------------\n")
    textfile.write(f"Total Votes: {total_votes} \n")
    for candidate, votes in candidate_count.items():
       textfile.write(f"{candidate}: {((votes/total_votes)*100):.3f}% ({(candidate_count[candidate])})\n")
    textfile.write("----------------------------\n")
    textfile.write(f"Winner: {winner} \n")
    textfile.write("----------------------------\n")