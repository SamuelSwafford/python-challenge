import csv
import os

cwd = os.getcwd()

# Define the path to the election data
election_data_path = cwd + '/PyPoll/Resources/election_data.csv'

# Initialize variables
total_votes = 0
candidates = {}

# Read the CSV file
with open(election_data_path, mode='r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header
    header = next(csvreader)

    # Read each row of data after the header
    for row in csvreader:
        # Count the total of votes
        total_votes += 1

        # Get the candidate name from the current row
        candidate_name = row[2]

        # If the candidate has other votes then add to its count
        if candidate_name in candidates:
            candidates[candidate_name] += 1
        else:
            # If it's the first vote for the candidate, initialize its count
            candidates[candidate_name] = 1

# Prepare the analysis output
analysis_output = "Election Results\n-------------------------\n"
analysis_output += f"Total Votes: {total_votes}\n-------------------------\n"

# Determine the winner and build the output for each candidate
winner = None
max_votes = 0
for candidate, votes in candidates.items():
    # Calculate the percentage of votes
    percentage = (votes / total_votes) * 100
    analysis_output += f"{candidate}: {percentage:.3f}% ({votes})\n"

    # Check for the winner
    if votes > max_votes:
        max_votes = votes
        winner = candidate

analysis_output += "-------------------------\n"
analysis_output += f"Winner: {winner}\n-------------------------\n"

# Print the analysis to the terminal
print(analysis_output)

# Export a text file with the results
output_path = cwd + '/PyPoll/analysis/election_analysis.txt'
with open(output_path, 'w') as file:
    file.write(analysis_output)
