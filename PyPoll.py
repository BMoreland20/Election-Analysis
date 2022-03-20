# The data we need to retrieve
# 1) The total number of votes cast
# 2) A complete list of candidates who recieve votes
# 3) The percentage of votes each candidate won
# 4) The total number of votes each candidate won
# 5) The winner of the election based on popular vote

# Add our dependencies.
import csv
import os

# Assign a variable for the file to load and the path.
election_file = 'c:\\Users\\Blaine\\Documents\\College\\Bootcamp\\Election_Analysis\\Resources\\election_results.csv'
election_save = 'c:\\Users\\Blaine\\Documents\\College\\Bootcamp\\Election_Analysis\\Resources\\election_analysis.txt'

#Initialize a total vote counter.
total_votes = 0

#Candidate options.
candidate_options = []

#Candidate votes.
candidate_votes = {}

#Winning Candidate and Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(election_file) as election_data:
    election_reader = csv.reader(election_data)

#Read the header row.
    headers = next(election_reader)

#Print each row in the CSV file.
    for row in election_reader:
        total_votes += 1
        
# Print the candidate name from each row.
        candidate_name = row[2]

# Add the candidate name to the candidate list if not already added.
        if candidate_name not in candidate_options:
#Add to list of candidates
            candidate_options.append(candidate_name)
#Begin tracking candidate vote count
            candidate_votes[candidate_name] = 0
#Add vote to candidate's count
        candidate_votes[candidate_name] += 1

# Determine the percentage of votes for each candidate by looping through the counts.
# 1. Iterate through the candidate list.
for candidate_name in candidate_votes:
    # 2. Retrieve vote count of a candidate.
    votes = candidate_votes[candidate_name]
    # 3. Calculate the percentage of votes.
    vote_percentage = float(votes) / float(total_votes) * 100
    # 4. Print the candidate name and percentage of votes.
    
#Winning Candidate and Count
    if (votes > winning_count) and (vote_percentage > winning_percentage):
#If true then set winning_count = votes and winning_percent = vote_percentage.        
        winning_count = votes
        winning_percentage = vote_percentage
#Set the winning candidate to the candidate's name
        winning_candidate = candidate_name
#Candidate results
    candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)

# Add a vote to that candidate's count
candidate_votes[candidate_name] += 1

        # 4a: Write an if statement that checks that the
        # county does not match any existing county in the county list.


            # 4b: Add the existing county to the list of counties.


            # 4c: Begin tracking the county's vote count.


        # 5: Add a vote to that county's vote count.

# Create a filename variable to a direct or indirect path to the file.
with open(election_save, "w") as txt_file:

# After opening the file print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    # After printing the final vote count to the terminal save the final vote count to the text file.
    txt_file.write(election_results)

    # 6a: Write a for loop to get the county from the county dictionary.

        # 6b: Retrieve the county vote count.

        # 6c: Calculate the percentage of votes for the county.


         # 6d: Print the county results to the terminal.

         # 6e: Save the county votes to a text file.

         # 6f: Write an if statement to determine the winning county and get its vote count.


    # 7: Print the county with the largest turnout to the terminal.


    # 8: Save the county with the largest turnout to a text file.

    for candidate_name in candidate_votes:
        # Retrieve vote count and percentage.
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate's voter count and percentage to the terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)
        # Determine winning vote count, winning percentage, and winning candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage
    # Print the winning candidate's results to the terminal.
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    # Save the winning candidate's results to the text file.
    txt_file.write(winning_candidate_summary)