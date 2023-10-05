import os
import csv

#C:\Users\naomi\OneDrive\Desktop\Data_Analysis_Bootcamp\
# WeeklyChallenges\Week3Python\Starter_Code\PyPoll\Resources
csv_path = os.path.join('Resources', 'election_data.csv')

#working variables
total_votes = 0 #starting at 0 each new row is one vote
candidate_list = [] #empty list for new candidate names to be added into
votesper_candidate = {} #an empty dictionary to hold {"candidate name": number of votes}
candidate_elect = "" #some string to hold the winners name
elect_tally = 0 #initialize the variable to hold winning vote count


with open(csv_path, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader) #skip header line

#The total number of votes cast
    for row in csvreader:
        total_votes += 1
#A complete list of candidates who received votes
        if row[2] not in candidate_list: #if the name in column 2 is not in the list
            candidate_list.append(row[2]) #add it to the list
            votesper_candidate[row[2]] = 0 #votes per candidate starts at 0 for each new candidate
        #per candidate add one vote to the dictionary as their name appears
        votesper_candidate[row[2]] = votesper_candidate[row[2]] + 1
#print(f'{votesper_candidate}')

################## PRINT TOTAL VOTES #####################
    summary_votes = (
        f"\n\nElection Results\n\n"
        f"----------------------------\n"
        f"Total Votes: {total_votes}\n"
        f"----------------------------\n")
    print(summary_votes)
##########################################################

#The total number and percentage of votes each candidate won
    #working with the newly created dictionary of votes per candidate
for candidate in votesper_candidate:
    vote_tally = votesper_candidate.get(candidate) #.get to retrieve the value of the key
    percent_vote = float(vote_tally) / float(total_votes) * 100 #float because the result could be a decimal

#The winner of the election based on popular vote
    if (vote_tally > elect_tally): 
        elect_tally = vote_tally
        candidate_elect = candidate

################ PRINT CANDIDATE SUMMARY ################
    election_results = (f"{candidate}: {percent_vote:.3f}% ({vote_tally})\n")
    print(election_results) 
#########################################################

################# PRINT ELECTION WINNER #################
summary_elected = (
    f"----------------------------\n"
    f"WINNER: {candidate_elect}\n"
    f"----------------------------\n")
print(summary_elected)

#write to file
output_file = os.path.join("Analysis", "election_results.txt")
with open(output_file, "w") as txt_file:
    txt_file.write(election_results)

output_file = os.path.join("Analysis", "summary_elected.txt")
with open(output_file, 'w') as txt_file:
    txt_file.write(summary_elected)
                   