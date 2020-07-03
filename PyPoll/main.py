# PyPoll Election Results

# Import OS Module
import os

# Import CSV module
import csv

# Define path to csv file
csvpath = os.path.join('Resources','election_data.csv')

# Define path to output text file
text_path_out = os.path.join('Analysis', 'election_results.txt')

# Create variables and set to 0
Voter_count = 0
candidate = 0

# Lists
candidates = []
votes = []
candidate_votes = []
percentage = []

# Open csv to read
with open(csvpath,'r') as csvfile:
    # Read csv file
    csvreader = csv.reader(csvfile, delimiter = ',')

    # Skip header row
    csv_header = next(csvreader)

    # Loop through file to count votes and list candidates' names
    for row in csvreader:
        # Count votes cast
        Voter_count = Voter_count + 1

        # Collect list of candidates
        if row[2] not in candidates:
            candidates.append(row[2])

        # Create list of all votes
        votes.append(row[2])

    # Populate votes assigned to each candidate
    for name in candidates:
        candidate_votes.append(votes.count(name))
        percentage.append(round(votes.count(name)/Voter_count*100,3))

    # Identify the winner with the most votes
    winner = candidates[candidate_votes.index(max(candidate_votes))]
    
    # Create a summary of results
    summary_output = ("Election Results"+ "\n"
    "------------------------------------" + "\n"
    f"Total Votes: {Voter_count}\n"
    "------------------------------------" + "\n"
    )

    winner_output = ("\n------------------------------------" + "\n"
    f"Winner: {winner}\n"
    "------------------------------------" + "\n"
    )

# Print summary of election results to terminal
print(summary_output)
for i in range(len(candidates)):
        print(f"{candidates[i]}: {percentage[i]}% {candidate_votes[i]}")
print(winner_output)

# Write to the text path
with open(text_path_out, "w") as text_file:
    text_file.write(summary_output)
    for i in range(len(candidates)):
        text_file.write(f"\n{candidates[i]}: {percentage[i]}% {candidate_votes[i]}")
    text_file.write(winner_output)