import os
import csv


csv_path = os.path.join( "Resources", "election_data.csv")


with open(csv_path, newline="") as file:

    election_data_reader = csv.reader(file, delimiter=",")

    csv_header = next(election_data_reader)

    total_votes = 0

    candidate_list = []

    candidate_votes = []



    for row in election_data_reader:
        total_votes += 1
        if row[2] not in candidate_list:
            candidate_list.append(row[2])
            candidate_index = candidate_list.index(row[2])
            candidate_votes.append(1)
        else:
            candidate_index = candidate_list.index(row[2])
            candidate_votes[candidate_index] += 1

    percent_of_votes = []
    for each in candidate_votes:
        percent_of_votes.append(round(each*100 / total_votes, 2))




    winner = candidate_votes.index(max(candidate_votes))
    winning_candidate = candidate_list[winner]


    print("Election Results")
    print("-------------------------")
    print(f"Total Votes: {total_votes}")
    print("-------------------------")
    for i in range(len(candidate_list)):
        print(f"{candidate_list[i]}: {percent_of_votes[i]}% ({candidate_votes[i]})")
    print("-------------------------")
    print(f"Winner: {winning_candidate}")
    print("-------------------------")


results =  open("Election_Results.txt", 'w')
results.write(f"""Election Results
-------------------------
Total Votes: {total_votes}
-------------------------
""")
for i in range(len(candidate_list)):
    next_line = f"{candidate_list[i]}: {percent_of_votes[i]}% ({candidate_votes[i]})"
    results.write(f"{next_line}\n")

results.write(f"""-------------------------
Winner: {winning_candidate}
-------------------------
""")
