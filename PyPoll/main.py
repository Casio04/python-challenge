
import csv
import os

election_file = os.path.join("Resources","Resources_election_data.csv")
voters_count = 0
khan = 0
Correy = 0
Li = 0
Tooley = 0
with open(election_file, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    next(csvreader)
    for row in csvreader:
        voters_count = voters_count + 1
        if row[2] == "Khan":
            khan = khan + 1
        elif row[2] == "Correy":
            Correy = Correy + 1
        elif row[2] == "Li":
            Li = Li + 1
        elif row[2] == "O'Tooley":
            Tooley = Tooley + 1
    
    khan_percent = round((khan / voters_count)*100, 2)
    correy_percent = round((Correy / voters_count)*100, 2)
    li_percent = round((Li / voters_count)*100, 2)
    tooley_percent = round((Tooley / voters_count)*100, 2)
    winner = max(khan, Correy, Li, Tooley)
    if winner == khan:
        winner = "Khan"
    elif winner == Correy:
        winner = "Correy"
    elif winner == Li:
        winner = "Li"
    elif winner == Tooley:
        winner = "O'Tooley"


result = f"""
Election Results
-----------------------------
Total Votes: {voters_count}
-----------------------------
Khan: {khan_percent:.3f}% ({khan})
Correy: {correy_percent:.3f}% ({Correy})
Li: {li_percent:.3f}% ({Li})
O'Tooley: {tooley_percent:.3f}% ({Tooley})
-----------------------------
Winner: {winner}
-----------------------------"""

print(result)

output_file = os.path.join("Analysis","election_results.txt")

open(output_file, "w").write(result)

