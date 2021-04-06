#%%
import os
import csv

#get csv
budget_data = os.path.join('..', 'PyBank', 'recources', 'budget_data.csv')
month_count = 0
avg_change  = 0
income = 0
daily = 0
increase = 0
decrease = 0
average = 0

def avg():
    average = income / month_count
    
    return average


# count rows and add months and income
with open(budget_data, 'r') as csvfile:
    csv = csv.reader(csvfile, delimiter=',')
    csv.__next__( )
    for row in csv: 
        month_count += 1
        income += int(f"{row[1]}")
        daily = int(f"{row[1]}") 
    avg()
    



print ("MONEY REPORT")
print("_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_")

print("Total Months: " + str(month_count))
print("Total Income: $" + str(income))
print(avg())





#Greatest increase in profits

#Greatest decrease in profits


#return all in the terminal and export as a text file y/n

# %%
