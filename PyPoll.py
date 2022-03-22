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

#County options.
county_options = []

#Candidate votes.
candidate_votes = {}

#County votes
county_votes = {}

#Winning Candidate and Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#County turnout
winning_turnout = ""
county_count = 0
county_percentage = 0

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
        county_name = row[1]

# Add the candidate name to the candidate list if not already added.
        if candidate_name not in candidate_options:
#Add to list of candidates
            candidate_options.append(candidate_name)
#Begin tracking candidate vote count
            candidate_votes[candidate_name] = 0
#Add vote to candidate's count
        candidate_votes[candidate_name] += 1
        
        # If the couty does not match any existing candidate...
        if county_name not in county_options:
            # Add it to the list of countie.
            county_options.append(county_name)

           # Begin tracking that candidate's vote count.
            county_votes[county_name] = 0

        # Add a vote to that candidate's count
        county_votes[county_name] += 1

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
#print(winning_candidate_summary)

# Add a vote to that candidate's count
candidate_votes[candidate_name] += 1

# 1. Iterate through the county list.
for county_name in county_votes:
    # 2. Retrieve vote count in county.
    votes = county_votes[county_name]
    # 3. Calculate the percentage of votes.
    vote_percentage = float(votes) / float(total_votes) * 100

#Winning County and Count
    if (votes > county_count) and (vote_percentage > county_percentage):
#If true then set winning_count = votes and winning_percent = vote_percentage.        
        county_count = votes
        county_percentage = vote_percentage
#Set the winning county to the counties name
        winning_turnout = county_name
#County results
    county_results = (f"{county_name}: {vote_percentage:.1f}% ({votes:,})\n")
#print(county_results)

winning_county_summary = (
    f"-------------------------\n"
    f"Largest County Turnout: {winning_turnout}\n"
    f"Winning Vote Count: {county_count:,}\n"
    f"Winning Percentage: {county_percentage:.1f}%\n"
    f"-------------------------\n")
#print(winning_county_summary)
    
# Create a filename variable to a direct or indirect path to the file.
with open(election_save, "w") as txt_file:
    
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n\n")

    print(election_results, end="")
    
    # After printing the final vote count to the terminal save the final vote count to the text file.
    txt_file.write(election_results)
    
#County Calculations
    txt_file.write("County votes:\n")

    for county_name in county_votes:
        votes = county_votes[county_name]
        vote_percentage = float(votes) / float(total_votes) * 100
        county_results = (
            f"{county_name}: {vote_percentage:.1f}% ({votes:,})\n")
        print(county_results)
	
        txt_file.write(county_results)

#Determine winning vote count by County and percentage
    if (votes > county_count) and (vote_percentage > county_percentage):        
        county_count = votes
        county_percentage = vote_percentage
        winning_turnout = county_name

    #Largest county turnout        
    county_turnout_summary = (
        f"\n-------------------------\n"
        f"Largest County Turnout: {winning_turnout}\n"
        f"-------------------------\n\n")
    
    print(county_turnout_summary, end ="")

    txt_file.write(county_turnout_summary)

# After opening the file print the final vote count to the terminal.
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
        f"\n-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    # Save the winning candidate's results to the text file.
    txt_file.write(winning_candidate_summary)