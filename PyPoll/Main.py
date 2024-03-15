# Import in the CSV package so that we can work with the CSV
import csv

# Reads the CSV file and then turn candidate specific data into a list of values
with open('./Resources/election_data.csv', 'r') as file:
    reader = csv.reader(file)
    # Reads the headers of the columns into a variable
    header = next(reader)
    # Creates a list of all candidates votes
    candidates = [row[2] for row in reader]


# Creates a separate list that contains only one entry of each candidates name
names = list(set(candidates))

# Creating a variable to contain each candidates name for future use
candidate_1 = names[0]
candidate_2 = names[1]
candidate_3 = names[2]

# Variables for the total number of votes for each candidate and the total number of votes overall
candidate_1_votes = candidates.count(candidate_1)
candidate_2_votes = candidates.count(candidate_2)
candidate_3_votes = candidates.count(candidate_3)
total_votes = len(candidates)

# Creates a dictionary that contains each candidates name as a key and the total number of votes as its value
candidate_votes = {candidate_1: candidate_1_votes,
                   candidate_2: candidate_2_votes,
                   candidate_3: candidate_3_votes
                   }

# Variables for the percentage of votes for each candidate
candidate_1_Percentage = round(candidate_votes[candidate_1]/total_votes*100,3)
candidate_2_Percentage = round(candidate_votes[candidate_2]/total_votes*100,3)
candidate_3_Percentage = round(candidate_votes[candidate_3]/total_votes*100,3)

# Variable for the candidate who received the most votes
winner = max(candidate_votes, key=candidate_votes.get)

# Prints out the election results to the terminal
print("Election Results\n-------------------------")
print(f"Total Votes: {total_votes}\n-------------------------")
print(f"{candidate_1}: {candidate_1_Percentage}% ({candidate_1_votes})")
print(f"{candidate_2}: {candidate_2_Percentage}% ({candidate_2_votes})")
print(f"{candidate_3}: {candidate_3_Percentage}% ({candidate_3_votes})\n-------------------------")
print(f"Winner: {winner}")

# Writes out the election results to a text file
with open('./Analysis/Poll_Results.txt', 'w') as f:
    f.write("Results from the Elections:\n")
    f.write(f"Total Votes: {total_votes}\n-------------------------\n")
    f.write(f"{candidate_1}: {candidate_1_Percentage}% ({candidate_1_votes})\n")
    f.write(f"{candidate_2}: {candidate_2_Percentage}% ({candidate_2_votes})\n")
    f.write(f"{candidate_3}: {candidate_3_Percentage}% ({candidate_3_votes})\n-------------------------\n")
    f.write(f"Winner: {winner}")
