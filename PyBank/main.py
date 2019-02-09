import os
import csv


# Path to collect data
csvpath = os.path.join('budget_data.csv')

with open(csvpath, newline='') as budget_csv:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(budget_csv, delimiter=',')

    #print(csvreader)

    # Read the header row first (skip this step if there is now header)
    budget_header = next(csvreader)
    
    #print(f"CSV Header: {budget_header}")
    
           
    # Read each row of data after the header
    total_month = 0
    total_sum = 0
    avg_chg = 0
    row_count = 0

    for row in csvreader:
        total_month = total_month + 1
 
        total_sum = int(row[1]) + total_sum
       
    print("Financial Analysis")
    print("----------------------------------")
    print(f"Total Months: {total_month}")
    print(f"Total: {total_sum}")
  #  print(f"Average Change: {avg_chg}")
    #print(f"length: {length}")
    



# Define the function and have it accept the 'wrestlerData' as its sole parameter
#def getPercentages(wrestlerData):
