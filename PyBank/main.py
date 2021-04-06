#%%
import os
import csv

budget_data = os.path.join('..', 'PyBank', 'recources', 'budget_data.csv')
month_count = 0
income = 0
monthly = 0
average = 0
month_values = []
month_list = []
p = 0
greatest_month = " "



def avg_rate_of_change():
    p = (month_values[0] - month_values[month_count -1]) / (1 - month_count)
    print("Average Rate of Change: $" + str(round(p, 2)))

def da_greatest():
    increase = 0
    decrease = 0
    for value in range(len(month_values)):
        if value > 0:
            decrease = 8
        elif (month_values[value - 1] - month_values[value]) < increase:
            increase = ((month_values[value - 1] - month_values[value]))
            greatest_month = (month_list[value])
    print("Greatest Monthly Increase: " + str(greatest_month) +" $"+ str(abs(increase)))
    print("Greatest Monthly Decrease: $" + str(decrease))

with open(budget_data, 'r') as csvfile:
    csv = csv.reader(csvfile, delimiter=',')
    csv.__next__( )
    for row in csv: 
        month_count += 1
        income += int(f"{row[1]}")
        monthly = int(f"{row[1]}") 
        month_values.append(monthly)
        month_list.append((f"{row[0]}") )

        

print ("MONEY REPORT")
print("_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_")
print("Total Months: " + str(month_count))
print("Total Income: $" + str(income))
avg_rate_of_change()
da_greatest()


#return all in the terminal and export as a text file y/n

# %%
