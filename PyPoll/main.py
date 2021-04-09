#%%
import os
import csv
from collections import Counter
#py Poll
votes_cast = 0
ballot_list= []
canidate_votes= []


poll_info = os.path.join('..', 'PyPoll', 'recources', 'election_data.csv')

with open(poll_info, 'r') as csvfile:
    csv = csv.reader(csvfile, delimiter=',')
    csv.__next__()
    ballot_list= list(csv)
for triad in ballot_list:
    votes_cast += 1
    canidate_votes.append(triad[2])
votes_per = dict(Counter(canidate_votes))
 
print(votes_cast)
print(votes_per)


## %%

# %%
