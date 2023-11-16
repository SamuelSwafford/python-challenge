import csv
import os

cwd = os.getcwd()

# Define the path to the budget data
budget_data_path = cwd + '/PyBank/Resources/budget_data.csv'

# Initialize variables
total_months = 0
net_total = 0
monthly_changes = []
previous_month_amount = 0
greatest_increase = ["", 0]
greatest_decrease = ["", float("inf")]

# Read the CSV file
with open(budget_data_path, mode='r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header
    header = next(csvreader)

    # Read each row of data after the header
    for row in csvreader:
        # Count the total of months
        total_months += 1

        # Sum the total net amount of "Profit/Losses"
        net_total += int(row[1])

        # Calculate the monthly change, then add it to the list of changes
        if total_months > 1:
            change = int(row[1]) - previous_month_amount
            monthly_changes.append(change)

            # Check if the current change is the greatest increase or decrease
            if change > greatest_increase[1]:
                greatest_increase[0] = row[0]
                greatest_increase[1] = change
            
            if change < greatest_decrease[1]:
                greatest_decrease[0] = row[0]
                greatest_decrease[1] = change

        # Set the previous month amount for the next loop iteration
        previous_month_amount = int(row[1])

# Calculate the average change
average_change = sum(monthly_changes) / len(monthly_changes) if monthly_changes else 0

# Prepare the analysis output
analysis_output = (
    "Financial Analysis\n"
    "----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${net_total}\n"
    f"Average Change: ${average_change:,.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n"
)

# Print the analysis to the terminal
print(analysis_output)

# Export a text file with the results
output_path = cwd + '/PyBank/analysis/financial_analysis.txt'
with open(output_path, 'w') as file:
    file.write(analysis_output)
