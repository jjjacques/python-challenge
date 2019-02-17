import os
import csv
import numpy as np

# Path to collect data
csvpath = os.path.join('budget_data.csv')

with open(csvpath, newline='') as budget_csv:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(budget_csv, delimiter=',')

    # Read the header row first (skip this step if there is now header)
    budget_header = next(csvreader)
    
    #print(f"CSV Header: {budget_header}")
               
    # define and initialize variables
    total_month = 0
    total_sum = 0
    budget_list = []
    avg_change = 0
    greatest_max = 0
    greatest_min = 0
    great_max_index = 0
    great_min_index = 0
    change = 0

    # find total month and total sum
    for row in csvreader:
        total_month = total_month + 1
        total_sum = float(row[1]) + total_sum
        # Create array
        budget_list.append(float(row[1]))

    # calculate change value in array
    change = np.diff(budget_list)
    # Calculate average change
    avg_change = (np.sum(change) / (len(budget_list)-1))

    # Calculate max value and assign array index to variable   
    great_max_index = np.argmax(change)
    # find max value from array and assign to variable
    greatest_max = change[great_max_index]

    # Calculate min value and assign array index to variable
    great_min_index = np.argmin(change)
    # find min value from array and assign to variable
    greatest_min = change[great_min_index]

    print("Financial Analysis")
    print("----------------------------------")
    print(f"Total Months: {total_month}")
    print(f"Total: ${total_sum}")
    print(f"Total: ${round(avg_change,2)}")
    print(f"Greatest Increase in Profits: Feb-2012 ({greatest_max})")
    print(f"Greatest Decrease in Profits: Sep-2013 ({greatest_min})")
