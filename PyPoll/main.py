#%%
import os
import csv
from collections import Counter
import time
#py Poll
votes_cast = 0
ballot_list= []
canidate_votes= []
percent_per = []
index = 0
most_votes = 0
winner = ""
x = ''


poll_info = os.path.join('..', 'PyPoll', 'recources', 'election_data.csv')

with open(poll_info, 'r') as csvfile:
    csv = csv.reader(csvfile, delimiter=',')
    csv.__next__()
    ballot_list= list(csv)
for triad in ballot_list:
    votes_cast += 1
    canidate_votes.append(triad[2])
votes_per = dict(Counter(canidate_votes))

for key in votes_per:
    votes = round((votes_per[key]/votes_cast) * 100,3 )
    percent_per.append(votes)
    if votes_per[key] > most_votes:
        most_votes = int(votes_per[key])
        winner = key





print('''Election Results  
_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_
Total Votes Cast: ''' + str(votes_cast) + ''' 
_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_''')
for key in votes_per:
    print((str(key)) + ": " + str(percent_per[index]) + "% " + "(" + str((votes_per[key])) + ")" )
    x += ((str(key)) + ": " + str(percent_per[index]) + "% " + "(" + str((votes_per[key])) + ") \n" )
    index += 1
print('''_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_''')
time.sleep(1)
print('''The winner is ''')
time.sleep(1)
print('...')
time.sleep(2)
print(str(winner) + "!!!!")



index = 0
save_path = os.path.join('..', 'PyPoll', 'analysis')
reporto = os.path.join(save_path, "Analysis.txt")
report = open(reporto, 'w')
report.write(('''Election Results  
_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_
Total Votes Cast: ''' + str(votes_cast) + ''' 
_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_
''' + str(x) + 
'''_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_
Winner: '''+ str(winner)))











# %%
