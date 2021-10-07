## creating a file path and module for reading csv files
import os
import csv

#module for reading csv file
csvpath = os.path.join('Resources', 'election_data.csv')

#create lists
voterid_list = []
county_list = []
canidate_list = []
unique_canidate_list = []
canidate_votes = []

#final tracking
total_votes = 0
win_canidate = ''
win_count = 0
win_percent = 0

with open(csvpath, 'r') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    next(csvfile)

# For each row in the CSV file.
    for row in csv_reader:
        total_votes = total_votes + 1
        # Get the candidate name from each row.
        candidate_name = row[2]
        # If the candidate does not match any existing candidate add it to
        # the candidate list
        if candidate_name not in unique_canidate_list:
            # Add the candidate name to the candidate list.
            unique_canidate_list.append(candidate_name)
            # And begin tracking that candidate's voter count.
            canidate_votes.append[candidate_name] = 0
        # Add a vote to that candidate's count
        canidate_votes.append[candidate_name] += 1

    print(canidate_votes)
      


# Save the results to our text file.
#with open(file_to_save, "w") as txt_file:
