# Import modules
import csv
import os

# Load input file
input_file = os.path.join("Resources", "election_data.csv")

########################  PART #1 #####################################

# Initialize
total_votes = 0

candidate_choices = []  # names of candidates to go here in a list
candidate_votes = {} # vote counts to go here in a dictionary

elected_candidate = ""
elected_count = 0

# Read the input file
with open(input_file) as votes_rollup:
    reader = csv.reader(votes_rollup)

    # Pass the header
    header = next(reader)

    # Row by row
    for row in reader:

        # Accumulate votes
        total_votes += 1

        # Initialize candidate names and votes received by them
        if row[2] not in candidate_choices:  # Is this a new name - if so, record it.
            candidate_choices.append(row[2])  # build the list of candidates
            candidate_votes[row[2]] = 0   # key: candidate name, value = 0 (initialized)

        # Increment votes as they roll in for each candidate in the dictionary 
        candidate_votes[row[2]] = candidate_votes[row[2]] + 1

#print(f'{candidate_votes}')

################################ PART #2 ###############################

# Print total votes to terminal
election_results = (
    f"\n\nElection Results\n"
    f"-------------------------\n"
    f"\n"
    f"Total Votes: {total_votes}\n"
    f"\n"
    f"-------------------------\n")
print(election_results)

# Now that we have the dictionary built with candidate name and their votes, loop through each candidate
for candidate in candidate_votes:
    # Tally results
    votes = candidate_votes.get(candidate)  # get() gets the value for the given key, which is candidate here
    vote_percentage = float(votes) / float(total_votes) * 100

    # Determine who won and their vote count
    if (votes > elected_count):
        elected_count = votes
        elected_candidate = candidate

    # Set election results by candidate to variable results_output
    results_output = f"{candidate}: {vote_percentage:.3f}% ({votes})\n"
    print(results_output)

# Print winner to terminal
elected_candidate_summary = (
    f"-------------------------\n"
    f"\n"
    f"Winner: {elected_candidate}\n"
    f"\n"
    f"-------------------------\n")
print(elected_candidate_summary)

# Write to file
output_file = os.path.join("analysis", "election_results.txt")

# Print the results and export the data to election_results.txt
# Use a with statement to get each candidate, their percentage of votes, and votes received through the For loop
with open(output_file, "w") as txt_file:
    txt_file.write(election_results)
    
    for candidate in candidate_votes:
   
        votes = candidate_votes.get(candidate) 
        vote_percentage = float(votes) / float(total_votes) * 100

    
        if (votes > elected_count):
            elected_count = votes
            elected_candidate = candidate

    
        results_output = f"{candidate}: {vote_percentage:.3f}% ({votes})\n"
        txt_file.write(results_output)
        
    txt_file.write(elected_candidate_summary)
