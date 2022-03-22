Overview of Election Audit:
The purpose of this exercise was and is to analyze county voting data to determine who of the three congressional candidates won the most recent election and their total votes gained and the percentage of the total vote tally.  A secondary task of determining the breakdown of each of the three counties vote totals and their percentage of the total vote while showing the county with the largest turnout.  All of this was first printed to the terminal and then saved to a .txt file.

Election-Audit Results:
•	The total votes for this congressional election were 369,711.

•	Jefferson county casted 38,855 votes which made up 10.5% of the vote. Denver casted 306,055 votes which made up 82.8% of the vote.  Lastly Arapahoe casted 24,801 votes which made up 6.7% of the vote.
![This is an image]( https://github.com/BMoreland20/Election-Analysis/blob/main/Resources/County_Vote_Breakdown.png)

•	Of the three counties Denver had the largest turnout with 369,711 votes cast. ![This is an image]( https://github.com/BMoreland20/Election-Analysis/blob/main/Resources/Largest_Turnout_County.png)


•	Charles Casper Stockham had 85,213 votes casted in his name making up 23% of the vote. Diana DeGette had 272,892 vostes casted in her name making up 73.8% of the vote.  Lastly Raymon Anthony Doane had 11,697 votes casted in his name making up 3.1% of the vote.  ![This is an image]( https://github.com/BMoreland20/Election-Analysis/blob/main/Resources/Candidate_Vote_Breakdown.png)

•	Diana DeGette won the congressional election with 272,892 votes casted in her name.  ![This is an image]( https://github.com/BMoreland20/Election-Analysis/blob/main/Resources/Winner_Breakdown.png)

Election-Audit Summary: 
The python code that we have developed can help automate all electronic balloting, reducing the time that it takes to determine vote counts per candidate and their percentages.  This code also reduces time it takes to tabulate vote counts from counties, and the percentages of votes that came from each county as well.  This script will still run if the main source of data is updated it will still be able to correctly tabulate the voter data to show vote counts for any candidate and what county votes were received from.

By simply updating the code line ‘file_to_load = os.path.join("Resources", "election_results.csv")’ to show ‘file_to_load = os.path.join("Any file location", "any_election_source_data.csv")’ and ‘file_to_save = os.path.join("analysis", "election_analysis.txt")’ to ‘file_to_save = os.path.join("Any file location", "any_output.txt")’ you will be able to run this analytical program on any election in the future and collect the same descriptive data.
	One additional point of code addition would be to include Bedford’s law to perform statistical analysis of the election data to check for potential anomalies in vote counts.  Here is a brief summary/example of the code that would need to be implemented to do this: first we need to import all of our data sources and set up our dependent libraries
‘#import libraries
import numpy as np
import pandas as pd
import sys
import math
import matplotlib.pyplot as plt’

‘def load_data(filename,var):
        df=pd.read_excel(filename)
        data=df[var]
        return df,data
#Data exploratory       
data.describe()
df.info()
df.describe().transpose
df.isnull().sum()’

Next is to set up the code to look through the data and perform the statistical calculations.
A sample of this code is as follows:
‘chi_square_stat = 0  # chi square test statistic
    for data, expected in zip(data_count,expected_counts):
        chi_square = math.pow(data - expected, 2)
        chi_square_stat += chi_square / expected’
This code was sourced from [Towards Data Science]( https://towardsdatascience.com/frawd-detection-using-benfords-law-python-code-9db8db474cf8) and the remainder of the code can be found here as well.

After applying these changes to our code this script will be able to pull descriptive readouts on voter totals as well as check for potential irregularities at the same time.  Resulting in an overall time savings for all.
