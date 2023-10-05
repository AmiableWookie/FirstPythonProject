# Import modules
import csv
import os

# Load input file
input_file = os.path.join("INPUT_DATA", "election_data.csv")

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

# Now that we have the dictionary built with candidate name and their votes, loop through each candidate

for candidate in candidate_votes:
    # Tally results
    votes = candidate_votes.get(candidate)  # get() gets the value for the given key, which is candidate here
    vote_percentage = float(votes) / float(total_votes) * 100

    # Determine who won and their vote count
    if (votes > elected_count):
        elected_count = votes
        elected_candidate = candidate

    # Print to terminal
    results_output = f"{candidate}: {vote_percentage:.3f}% ({votes})\n"
    print(results_output)

################################ PART #3 ###############################

# Print to terminal
election_results = (
    f"\n\nElection Results\n"
    f"-------------------------\n"
    f"Total Votes: {total_votes}\n"
    f"-------------------------\n")
print(election_results)

# Print to terminal
elected_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {elected_candidate}\n"
    f"-------------------------\n")
print(elected_candidate_summary)


################################ PART #4 ###############################

# Write to file
output_file = os.path.join("OUTPUT_DATA", "election_results.txt")

# Print the results and export the data to our text file
with open(output_file, "w") as txt_file:

    # Save the final vote count to the text file
    txt_file.write(election_results)


# Write to file
output_file = os.path.join("OUTPUT_DATA", "winning_candidate_summary.txt")

# Print the results and export the data to our text file
with open(output_file, "w") as txt_file:

    # Save the winning candidate's name to the text file
    txt_file.write(elected_candidate_summary)
