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
#Print winners name
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)


# Create a filename variable to a direct or indirect path to the file.
#with open(election_save, "w") as txt_file:

    # Write some data to the file.
    #txt_file.write("Hello World")