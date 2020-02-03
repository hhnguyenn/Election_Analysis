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
#county names 
county_options=[]
#declare empty county dictionary
county_votes={}
Cwin_county=""
Cwin_count=0
Cwin_percentage=0

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
        #get county name from each row
        county_name =row[1]

#if the candidate does not match any existing candidate, add
        if candidate_name not in candidate_options:
            #add it to the list of candidates
            candidate_options.append(candidate_name)
            #begin tracking that candidate's vote count
            candidate_votes[candidate_name]=0
        #add a vote to that candidate's count
        candidate_votes[candidate_name]+=1

        if county_name not in county_options:
            county_options.append(county_name)
            county_votes[county_name]=0
        county_votes[county_name]+=1
        
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

    county_data=(f"\nCounty Votes:\n")
    print(county_data)
    txt_file.write(county_data)

    for county in county_votes:
        Cvotes=county_votes[county]
        Cvotes_percentage = float(Cvotes)/float(total_votes) * 100
        County_results=(f"{county}: {Cvotes_percentage:.1f}% ({Cvotes:,})\n")
        
        print(County_results)
        txt_file.write(County_results)

        if (Cvotes>Cwin_count) and (Cvotes_percentage> Cwin_percentage):
                Cwin_count=Cvotes
                Cwin_county = county
                Cwin_percentage=Cvotes_percentage

    Largest_turnout=(
        f"\n..............................\n"
        f"Largest County Turnout: {Cwin_county}"
        f"\n...............................\n")
    print(Largest_turnout)
    txt_file.write(Largest_turnout)

with open(file_to_save, "a") as txt_file:
    #determine percentage of votes by looping through counts and iterate through candidate list    
    for candidate in candidate_votes:
            #vote count and percentage
        votes=candidate_votes[candidate]
            #retrieve vote count of a candidate
        votes_percentage = float(votes)/float(total_votes) *100
            #print each candidate, their voter count, and percentage to the terminal
        candidate_results=(f"{candidate}: {votes_percentage:.1f}% ({votes:,})\n")
        print(candidate_results)
        txt_file.write(candidate_results)

    #determine winning vote count, winning percentage, and candidate
        if (votes>winning_count) and (votes_percentage> winning_percentage):
            #if true, then set winning_count=votes and winning_percentage= vote_percentage.
            winning_count = votes
            winning_candidate = candidate
            winning_percentage = votes_percentage
    
    #print winning candidates' results to the terminal.
    winning_candidate_summary = (
        f"...................................\n"
        f"Winning: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"...................................\n")

    print(winning_candidate_summary)    
#save winning candidate's results to text file
    txt_file.write(winning_candidate_summary)
