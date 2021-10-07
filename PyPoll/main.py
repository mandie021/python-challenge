## creating a file path and module for reading csv files
import os
import csv

#module for reading csv file
csvpath = os.path.join('Resources', 'election_data.csv')
# Add a text to save the file to a path.
txtfile = os.path.join("analysis", "Analysis.txt")

#create lists
voterid_list = []
county_list = []
canidate_list = []
unique_canidate_list = []
canidate_votes = {}

#final tracking
total_votes = 0
win_canidate = ''
win_count = 0


with open(csvpath, 'r') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    next(csvfile)

# For each row in the CSV file.
    for row in csv_reader:
        total_votes = total_votes + 1
        # Get the candidate name from each row.
        canidate_name = row[2]
        # If the candidate does not match any existing candidate add it to
        # the candidate list
        if canidate_name not in unique_canidate_list:
            # Add the candidate name to the candidate list.
            unique_canidate_list.append(canidate_name)
            # And begin tracking that candidate's voter count.
            canidate_votes[canidate_name] = 0
        # Add a vote to that candidate's count
        canidate_votes[canidate_name] += 1
    #print(canidate_votes) - {'Khan': 2218231, 'Correy': 704200, 'Li': 492940, "O'Tooley": 105630}
# Save the results to our text file.
with open(txtfile, "w+") as txt_file:
    # Print the final vote count (to terminal)
    election_results = (
        f"\nElection Results\n"
        f"---------------------------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"---------------------------------------------\n")
    print(election_results)
    txt_file.write(election_results)
#percentage of vote
    for canidate_name in canidate_votes:
        votes = canidate_votes.get(canidate_name)
        vote_perct = float(votes) / float (total_votes) * 100
        #we are going to store as dict
        canidate_results = (f'{canidate_name}: {vote_perct:.1f}% ({votes:,})\n')
        #print(canidate_results) - came out with correct but will need to write this to term and txt
        print(canidate_results)
        # Save the canidate summary name to the text file
        txt_file.write(canidate_results)
        #winning popular vote
        if (votes>win_count):
            win_count = votes
            win_canidate = canidate_name
    #print(win_canidate)
    # Print the winning candidate (to terminal)
    winner = (
            f"---------------------------------------------\n"
            f"Winner: {win_canidate}\n"
            f"---------------------------------------------\n")
    print(winner)
    # Save the winning candidate's name to the text file
    txt_file.write(winner)

