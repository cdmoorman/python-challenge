# PyBank Financial Analysis

# Import OS Module
import os

# Import CSV module
import csv

# Define path to csv file
csvpath = os.path.join('Resources','budget_data.csv')

# Define path to output text file
text_path_out = os.path.join('Analysis', 'summary_analysis.txt')

# Create variables and set to 0
Count_month = 0
Sum_Profit = 0
Profit = 0
Profit_delta = 0

# Lists
List_profit_delta = []
Month_delta = []
Total_profit = []

Max_increase = ["", 0]
Max_Decrease = ["", 99999999999]

# Open csv to read
with open(csvpath,'r') as csvfile:
    # Read csv file
    csvreader = csv.reader(csvfile, delimiter = ',')

    # Skip header row
    csv_header = next(csvreader)

    #Loop for counting months and summing total profit for the periods
    for row in csvreader:
        # Count months and sum profit
        Count_month = Count_month + 1

        # Collect list of the dates reported
        Month_delta.append(row[0])

        # Sum of all profit for the dates listed
        Total_profit.append(row[1])
        Sum_Profit = Sum_Profit + int(row[1])
        formatted_sum = "${:,.0f}".format(Sum_Profit)

        # Changes in profit calculations
        if Profit != 0:
            Recent_Profit = int(row[1])
            Profit_delta = Recent_Profit - Profit
            List_profit_delta.append(Profit_delta)
            Profit = Recent_Profit
        
        elif Profit == 0:
            Profit = int(row[1])

        # Determine max profit increase and month it occurred
        if (Profit_delta > Max_increase[1]):
            Max_increase[1] = Profit_delta
            Max_increase[0] = row[0]

        # Determine max profit decrease and month it occurred
        if (Profit_delta < Max_Decrease[1]):
            Max_Decrease[0] = row[0]
            Max_Decrease[1] = Profit_delta
        
# calculate the average profit outside of the loop
profit_mean = sum(List_profit_delta) / len(List_profit_delta)
formatted_mean = "${:,.2f}".format(profit_mean)


#print the outcomes
summary_output = ("Financial Analysis" + "\n"
    "------------------------------------" + "\n"
    f"Total Months: {Count_month}\n"
    f"Total: {formatted_sum}\n"
    f"Average Profit Change: {formatted_mean}\n"
    f"Greatest increase in Profits: {Max_increase[0]} ${Max_increase[1]}\n"
    f"Greatest decrease in Profits: {Max_Decrease[0]} ${Max_Decrease[1]}\n"
)

print(summary_output)

#Write to the text path
with open(text_path_out, "w") as text_file:
    text_file.write(summary_output)