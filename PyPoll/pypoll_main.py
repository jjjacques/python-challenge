import os
import csv
import numpy as np

# Path to collect data
csvpath = os.path.join('election_data.csv')

with open(csvpath, newline='') as election_csv:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(election_csv, delimiter=',')

    # Read the header row first (skip this step if there is now header)
    election_header = next(csvreader)

    #print(f"csvreader: {election_header}")

    total_votes = 0
    khan_list = []
    correy_list = []
    li_list = []
    o_tooley_list = []
    khan_count = 0
    correy_count = 0
    li_count = 0
    o_tooley_count = 0
    khan_percent = 0
    correy_percent = 0
    li_percent = 0
    o_tooley_percent = 0
    highest = 0
    winner = 0
    name = ""

    # create array list for each candidate
    for row in csvreader:      
        if(row[2] == 'Khan'):
            khan_list.append(row)
        if(row[2] == 'Correy'):
            correy_list.append(row)
        if(row[2] == 'Li'):
            li_list.append(row)
        if(row[2] == 'O\'Tooley'):
            o_tooley_list.append(row)
    
    # Calculate total votes for each candidate
    khan_count = len(khan_list)
    correy_count = len(correy_list)
    li_count = len(li_list)
    o_tooley_count = len(o_tooley_list)

    # calculate highest number of votes
    highest = np.array([khan_count, correy_count, li_count, o_tooley_count])
    winner = np.amax(highest)
    
    # assign candidate name to highest number of votes
    for x in highest:
        if x == winner and x == khan_count:
            name = "Khan"
        if x == winner and x == correy_count:
            name = "Correy"
        if x == winner and x == li_count:
            name = "Li"
        if x == winner and x == o_tooley_count:
            name = "O'Tooley"
    
    # Calculate total votes
    total_votes = round((khan_count + correy_count + li_count + o_tooley_count),0)
    
    # Calculate percentages for each candidate
    khan_percent = (khan_count / total_votes * 100)
    correy_percent = (correy_count / total_votes * 100)
    li_percent = (li_count / total_votes * 100)
    o_tooley_percent = (o_tooley_count / total_votes * 100)

    # display results    
    print("Election Results")
    print("----------------------------------")
    print(f"Total Votes: {total_votes}")
    print("----------------------------------")
    print("Khan: " + "{0:.3f}%".format(khan_percent) + " (" + str(khan_count) + ")")
    print("Correy: " + "{0:.3f}%".format(correy_percent) + " (" + str(correy_count) + ")")
    print("Li: " + "{0:.3f}%".format(li_percent) + " (" + str(li_count) + ")")
    print("O'Tooley: " + "{0:.3f}%".format(o_tooley_percent) + " (" + str(o_tooley_count) + ")")
    print("----------------------------------")
    print("Winner: " + name)
    print("----------------------------------")