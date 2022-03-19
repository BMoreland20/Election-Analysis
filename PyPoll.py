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

# Open the election results and read the file.
with open(election_file) as election_data:
     election_reader = csv.reader(election_data)
#Read the header row.
     headers = next(election_reader)
     print(headers)
#Print each row in the CSV file.
     for row in election_reader:
          total_votes += 1
     print(total_votes)


# Create a filename variable to a direct or indirect path to the file.
with open(election_save, "w") as txt_file:

    # Write some data to the file.
    txt_file.write("Hello World")