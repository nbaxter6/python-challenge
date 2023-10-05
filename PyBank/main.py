import os
import csv
#C:\Users\naomi\OneDrive\Desktop\Data_Analysis_Bootcamp\WEEK3-Python-Start\
# Class_3_Activities\python-challenge\PyBank\Resources
bank_file = os.path.join('Resources', 'budget_data.csv')

#Variables
Total_Months = 1
Total_Sum = 0
Month_List = []
Change_List = []
Max_Rise = ["", 0] #set at 0 to capture greater than values
Max_Fall = ["", 9999999999999] #set high to capture less than values


with open(bank_file, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader) #skip header line

    #because theres no preceeding month before the first month, treat the first line differently
    First_line = next(csvreader)
    Total_Sum += int(First_line[1]) #total_sum = total_sum + first_line[1]
    Prev_Amount = int(First_line[1]) #previous amount = first_line[1]


    for row in csvreader:

        #The total number of months included in the dataset
        Total_Months += 1

        #The net total amount of "Profit/Losses" over the entire period
        Total_Sum += int(row[1])

        #List of revenue change per month
        Change = int(row[1]) - Prev_Amount
        Prev_Amount = int(row[1])

        Change_List += [Change] #Add the determined changes to the change list
        Month_List += [row[0]] #capture the value in the month column

        #The greatest increase in profits (date and amount) over the entire period
        if Change > Max_Rise[1]:
            Max_Rise[0] = row[0]
            Max_Rise[1] = Change

        #The greatest decrease in profits (date and amount) over the entire period
        if Change < Max_Fall[1]:
            Max_Fall[0] = row[0]
            Max_Fall[1] = Change

Ave_Change = sum(Change_List) / len(Change_List)

print_statement = (f"\nFinancial Analysis\n\n"
                   f"-------------------------------\n"
                   f"Total Months: {Total_Months}\n\n"
                   f"Total: ${Total_Sum}\n\n"
                   f"Average Change: ${Ave_Change}\n\n"
                   f"Greatest Increase in Profits: {Max_Rise[0]} ${Max_Rise[1]}\n\n"
                   f"Greatest Decrease in Profits: {Max_Fall[0]} ${Max_Fall[1]}\n\n")
print(print_statement)

output_file = os.path.join("budget_data_output.txt")

with open(output_file, "w") as txt_file:
    txt_file.write(print_statement)