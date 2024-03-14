# Import in the CSV package so that we can work with the CSV
import csv

# Read the CSV file and then turn candidate specific data into a list of values
with open('./Resources/election_data.csv', 'r') as file:
    reader = csv.reader(file)
    # Reads the headers of the columns into a variable
    header = next(reader)
    candidates = []
    for row in reader:
        candidates.append(row[2])


# Create a separate list that contains only one entry of each candidates name
names = list(set(candidates))

# Creating a variable to contain each candidates name for future use
candidate_1 = names[0]
candidate_2 = names[1]
candidate_3 = names[2]

# Create a dictionary that contains each candidates name as a key and the total number of votes as its value
candidate_votes = {candidate_1: candidates.count(candidate_1),
                   candidate_2: candidates.count(candidate_2),
                   candidate_3: candidates.count(candidate_3)
                   }

# Variables for the total number of votes for each candidate and the total number of votes overall
candidate_1_votes = candidates.count(candidate_1)
candidate_2_votes = candidates.count(candidate_2)
candidate_3_votes = candidates.count(candidate_3)
total_votes = len(candidates)

# Variables for the percentage of votes for each candidate
candidate_1_Percentage = round(candidate_votes[candidate_1]/total_votes*100,3)
candidate_2_Percentage = round(candidate_votes[candidate_2]/total_votes*100,3)
candidate_3_Percentage = round(candidate_votes[candidate_3]/total_votes*100,3)

# Variable for the candidate who received the most votes
winner = max(candidate_votes, key=candidate_votes.get)

# Prints out the election results to the terminal
print("Election Results\n-------------------------")
print("Total Votes: {}\n-------------------------".format(total_votes))
print("{}: {}% ({})".format(candidate_1, candidate_1_Percentage,candidate_1_votes))
print("{}: {}% ({})".format(candidate_2, candidate_2_Percentage,candidate_2_votes))
print("{}: {}% ({})\n-------------------------".format(candidate_3, candidate_3_Percentage,candidate_3_votes))
print("Winner: {}".format(winner))

# Writes out the election results to a text file
with open('./Analysis/Poll_Results.txt', 'w') as f:
    f.write("Results from the Elections:\n")
    f.write("Total Votes: {}\n-------------------------\n".format(total_votes))
    f.write("{}: {}% ({})\n".format(candidate_1, candidate_1_Percentage, candidate_1_votes))
    f.write("{}: {}% ({})\n".format(candidate_2, candidate_2_Percentage, candidate_2_votes))
    f.write("{}: {}% ({})\n-------------------------\n ".format(candidate_3, candidate_3_Percentage,candidate_3_votes))
    f.write("Winner: {}".format(winner))
