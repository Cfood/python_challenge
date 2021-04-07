#%%
import os
import csv

#Define Variables
budget_data = os.path.join('..', 'PyBank', 'recources', 'budget_data.csv')
month_count = 0
income = 0
monthly = 0
average = 0
month_values = []
month_list = []
p = 0
greatest_month = ''
worst_month = " "
txt_list = ''

#Define Function that uses "month_count" to iterate thru "month list" to get values and print
def da_greatest():
    increase = 0
    decrease = 0
    p = (month_values[0] - month_values[month_count -1]) / (1 - month_count)
    for value in range(len(month_values)):
        if (month_values[value] - month_values[value-1]) < decrease:
            worst_month = month_list[value]
            decrease = (month_values[value] - month_values[value-1])
        elif (month_values[value - 1] - month_values[value]) < increase:
            greatest_month =(month_list[value])
            increase = ((month_values[value - 1] - month_values[value]))
    print ("MONEY REPORT")
    print("_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_")
    print("Total Months: " + str(month_count))
    print("Total Income: $" + str(income))   
    print("Average Rate of Change: $" + str(round(p, 2)))   
    print("Greatest Monthly Increase: " + (greatest_month) +" $"+ str(abs(increase)))
    print("Greatest Monthly Decrease: " + (worst_month) + " $" + str(decrease))
    
    answer = input("Import as TXT? y/n?: ")
    if answer == "y":
        report = open('Report.txt', 'w')
        report.write("MONEY REPORT")
        report.write("\n")
        report.write("_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_")
        report.write("\n")
        report.write("Total Months: " + str(month_count))
        report.write("\n")
        report.write("Total Income: $" + str(income))  
        report.write("\n") 
        report.write("Average Rate of Change: $" + str(round(p, 2))) 
        report.write("\n")  
        report.write("Greatest Monthly Increase: " + greatest_month +" $"+ str(abs(increase)))
        report.write("\n")
        report.write("Greatest Monthly Decrease: " + (worst_month) + " $" + str(decrease))
        report.close()
    elif answer == "n":
        next 
        



#open csv to extract and aggregate data
with open(budget_data, 'r') as csvfile:
    csv = csv.reader(csvfile, delimiter=',')
    csv.__next__( )
    for row in csv: 
        month_count += 1
        income += int(f"{row[1]}")
        monthly = int(f"{row[1]}") 
        month_values.append(monthly)
        month_list.append((f"{row[0]}") )


#use previously defined function on the extracted data and print results
da_greatest()



# %%
