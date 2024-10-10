# -*- coding: UTF-8 -*-
"""PyPoll Homework Starter File."""

# Import necessary modules
import csv
import os

# Files to load and output (update with correct file paths)
# updated 'Resources' to 'Resource' due to a naming error in my file path
file_to_load = os.path.join("Resource", "election_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "election_analysis.txt")  # Output file path

# Initialize variables to track the election data
total_votes = 0  # Track the total number of votes cast

# Define lists to track candidate names
candidates_list = []

# Create a dictionary to track each candididate's vote count
candidate_vote_tracker = {}

# Winning Candidate and Winning Count Tracker
# I didn't see the need to declare a winning candidate variable here if it doesn't compare to anything else
# Thus it is declared later on
winning_count = 0

# Open the CSV file and process it
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Skip the header row
    header = next(reader)

    # Loop through each row of the dataset and process it
    for row in reader:

        # Print a loading indicator (for large datasets)
        # Added a new line so the toal vote count will print after all the loading indicators
        print(". ", end="")

        # Increment the total vote count for each row
        total_votes += 1

        # Get the candidate's name from the row
        candidate = row[2]

        # If the candidate is not already in the candidate list, add them
        if candidate not in candidates_list:
            candidates_list.append(candidate)

            # Initialize the vote for the candidate in the vote tracker dictionary
            candidate_vote_tracker[candidate] = 0

        # Add a vote to the candidate's count
        candidate_vote_tracker[candidate] += 1



# Open a text file to save the output
with open(file_to_output, "w") as txt_file:

    # Print the total vote count (to terminal)
    # I made the code output to the terminal match what is on the txt_file
    print(
        'Election Results\n'
        '------------------------------------\n'
    )
    print(
        f'Total Votes: {total_votes}\n'
        '------------------------------------\n'
    )

    # Set up the beginning of the text document
    txt_file.write(
        'Election Results\n'
        '------------------------------------\n'
    )
    # Write the total vote count to the text file
    txt_file.write(
        f'Total Votes: {total_votes}\n'
        '------------------------------------\n'
    )

    # Loop through the candidates to determine vote percentages and identify the winner
    for candidate in candidates_list:

        # Get the vote count for the current candidate and save it in a variable
        votes = candidate_vote_tracker[candidate]
        
        # Calculate the percentage of that candidates votes
        vote_percentage = round((votes / total_votes) * 100, 3)

        # Update the winning candidate if this one has more votes
        if votes > winning_count:
            winning_count = votes
            winning_candidate = candidate

        # Print and save each candidate's vote count and percentage
        print(f'{candidate}: {vote_percentage}% ({votes})')

        # Output the same line into the txt_file
        # Also adds a new line so the loop will atomatically populate in the next line
        txt_file.write(f'{candidate}: {vote_percentage}% ({votes})\n')

    # Generate and print the winning candidate summary
    print(
        f'------------------------------------\n'
        f'Winner: {winning_candidate}\n'
        f'------------------------------------\n'
    )

    # Save the winning candidate summary to the text file
    txt_file.write(
        f'------------------------------------\n'
        f'Winner: {winning_candidate}\n'
        f'------------------------------------\n'
    )