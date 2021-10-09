# Import modules needed
import csv
import os

#set file path
csvpath = os.path.join("Resources", "election_data.csv").replace("\\", "/")


#open csv using with and saving it into a variable
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile)

    #strip and store header
    csv_header = next(csvreader)

    #create empty lists
    voter_id = []
    county_list = []
    candidate_choice = []
    votes_for_each_cand = []
    percentage_of_votes = []

    #populating empty lists
    for row in csvreader:
        voter_id.append(row[0])
        county_list.append(row[1])
        candidate_choice.append(row[2])
    
    #find number of votes
    total_votes = len(voter_id)

    #list of candidates
    candidates = list(set(candidate_choice))

    #total votes for each cand
    for cand in candidates:
        votes_for_each_cand.append(candidate_choice.count(cand))
    

    #percentage of votes for each candidate
    for votes in votes_for_each_cand:
        percentage_of_votes.append(round(votes/total_votes*100))
    
    
    #find winner
    winner = candidates[percentage_of_votes.index(max(percentage_of_votes))]

    #zip candidates with perecentage of votes
    cand_pairs = zip(candidates, percentage_of_votes, votes_for_each_cand)

    #convert zip into list
    list_of_cand_pairs = list(cand_pairs)

    #sort list based on percentages
    list_of_cand_pairs.sort(key=lambda x:x[1], reverse=True)
        

    #print results to terminal
    print(f"Election Results\n"
            "-------------------------\n"
            f"Total Votes: {total_votes}\n"
            "-------------------------\n"
            f"{list_of_cand_pairs[0][0]}: {list_of_cand_pairs[0][1]}.000% ({list_of_cand_pairs[0][2]})\n"
            f"{list_of_cand_pairs[1][0]}: {list_of_cand_pairs[1][1]}.000% ({list_of_cand_pairs[1][2]})\n"
            f"{list_of_cand_pairs[2][0]}: {list_of_cand_pairs[2][1]}.000% ({list_of_cand_pairs[2][2]})\n"
            f"{list_of_cand_pairs[3][0]}: {list_of_cand_pairs[3][1]}.000% ({list_of_cand_pairs[3][2]})\n"
            "-------------------------\n"
            f"Winner: {winner}\n"
            "-------------------------"
                    "")

    #writing to a text file
    #setting path for file
    results_path = os.path.join("analysis", "results.txt").replace("\\", "/")
    with open(results_path, 'w') as file:
        file.write(f"Election Results\n"
                    "-------------------------\n"
                    f"Total Votes: {total_votes}\n"
                    "-------------------------\n"
                    f"{list_of_cand_pairs[0][0]}: {list_of_cand_pairs[0][1]}.000% ({list_of_cand_pairs[0][2]})\n"
                    f"{list_of_cand_pairs[1][0]}: {list_of_cand_pairs[1][1]}.000% ({list_of_cand_pairs[1][2]})\n"
                    f"{list_of_cand_pairs[2][0]}: {list_of_cand_pairs[2][1]}.000% ({list_of_cand_pairs[2][2]})\n"
                    f"{list_of_cand_pairs[3][0]}: {list_of_cand_pairs[3][1]}.000% ({list_of_cand_pairs[3][2]})\n"
                    "-------------------------\n"
                    f"Winner: {winner}\n"
                    "-------------------------"
                            "")
    

    
    
    
    
    
    
    
    
    


    



