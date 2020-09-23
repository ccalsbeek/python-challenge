#dependencies
import os
import csv

#create empty list and dictionary to store data
votes = []
results = {}
total_votes = 0
winner=""
#print opening lines
print("Election Results")
print("---------------------")

# create path to collect data from csv
path = os.path.join('Resources', 'election_data.csv')

#read csv
with open(path) as election_data:
    
    data = csv.reader(election_data)

    #skip header
    header = next(data)

        #count votes and total
    for row in data:
        votes.append(row[2])  # <--add candidate votes to list

    total_votes = len(votes)  # <--count list to get total number of votes
    print("Total Votes: ", total_votes)

    #loop through list of candidate votes and add counts and names for each to dictionary
    for v in votes:
        if v in results:
            results[v] +=1
        else:
            results[v] = 1

    #loop through dictionary and calc total and percentages for each candidate
    for candidate in results:
        if results[candidate] >=1:
            total_votes = len(votes)
            percent = (results[candidate]*100/total_votes)
            print(candidate + ": ", percent, "%", results[candidate])
        
    #find the largest value for votes and get candidate for winner
    winner = max(results, key=results.get)
    print("Winner: ", winner)

#write to output file
    o_path = os.path.join("Analysis", "election_analysis.txt")

    with open(o_path, "w") as analysis:
        analysis.write(f"Election Results\n")
        analysis.write(f"---------------------\n")
        analysis.write(f"Total Votes: {total_votes}\n")
        for key, value in results.items():
            analysis.write(f"{key}: {format(value/total_votes, '.3%')} ({value})\n")
        analysis.write(f"Winner: {winner}\n")
        analysis.close

    





