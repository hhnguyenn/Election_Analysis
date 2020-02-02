#add our dependencies
import csv
import os
#Assign a variable for the file to load and the path.
file_to_load = os.path.join("..","Election_Analysis","election_results.csv")
#Assign a variable to save the file to a path
file_to_save = os.path.join("..","Election_Analysis","analysis","election_analysis.txt")

#Initialize a total vote counter.
total_votes = 0
#candidate options and candidate votes
candidate_options = []
#declare the empty dictionary
candidate_votes ={}
#track winning candidate, vote count, and percentage
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#Open the election results and read the file.
with open(file_to_load) as election_data:
#read the file object with the reader function
    file_reader = csv.reader(election_data)

    #read the header row.
    headers= next(file_reader)

    #Print each row in the CSV file.
    for row in file_reader:
        #2. Add to the total vote count.
        total_votes += 1

        #get candidate name from each row.
        candidate_name = row[2]

#if the candidate does not match any existing candidate, add
        if candidate_name not in candidate_options:
            #add it to the list of candidates
            candidate_options.append(candidate_name)
            #begin tracking that candidate's vote count
            candidate_votes[candidate_name]=0
        #add a vote to that candidate's count
        candidate_votes[candidate_name]+=1

#save results to text file
with open(file_to_save, "w") as txt_file:
    election_results=(
        f"\nElection Results\n"
        f"--------------------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"......................................\n")
    print(election_results, end="")

    #save final vote count to text file
    txt_file.write(election_results)

    #determine percentage of votes by looping through counts and iterate through candidate list    
    for candidate in candidate_votes:
            #vote count and percentage
        votes=candidate_votes[candidate]
            #retrieve vote count of a candidate
        votes_percentage = float(votes)/float(total_votes) *100
            #print each candidate, their voter count, and percentage to the terminal
            #print(f"{candidate}: {votes_percentage:.1f}% ({votes:,})\n")

    #determine winning vote count, winning percentage, and candidate
        if (votes>winning_count) and (votes_percentage> winning_percentage):
            #if true, then set winning_count=votes and winning_percentage= vote_percentage.
                winning_count = votes
                #winning_candidate = candidate's name
                winning_candidate = candidate
                winning_percentage = votes_percentage
        print(f"{candidate}: {votes_percentage:.1f}% ({votes:,})\n")
    #print winning candidates' results to the terminal.
    winning_candidate_summary = (
        f"...................................\n"
        f"Winning: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"...................................\n")

    print(winning_candidate_summary)    

