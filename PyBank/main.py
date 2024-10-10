# -*- coding: UTF-8 -*-
"""PyBank Homework Starter File."""

# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resource", "budget_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "budget_analysis.txt")  # Output file path

# Define variables to track the financial data
total_months = 0
total_net = 0

# Add more variables to track other necessary financial data
# Create a net_change_list to calculate the average net change
net_change_list = []

# Initialize both greatest increase and decrease to have variable to compare a new value to
greatest_increase = -1
greatest_decrease = 1



# Open and read the csv
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data, delimiter=",")

    # Skip the header row
    header = next(reader)

    # Extract first row to avoid appending to net_change_list
    first_row = next(reader)

    #creates a variable to calculate net_change
    previous_value = int(first_row[1]) 

    # Track the total months and net change
    total_months = total_months + 1
    total_net = total_net + int(first_row[1])

    # Process each row of data
    for row in reader:

        # Track the total months
        total_months = total_months + 1

        #Track the total net
        total_net += int(row[1])

        # Tracts the change and stores it in a variable called net_change
        net_change = int(row[1]) - previous_value

        #adds the change to net_change_list
        net_change_list.append(net_change)
        

        # Calculate the greatest increase in profits (month and amount)
        if net_change > greatest_increase:
            greatest_increase = net_change
            greatest_increase_month = row[0]

        # Calculate the greatest decrease in losses (month and amount)
        if net_change < greatest_decrease:
            greatest_decrease = net_change
            greatest_decrease_month = row[0]

        # Update the previous value so the next iteration can perform calculations
        previous_value = int(row[1])


# Calculate the average net change across the months
average_net = round(sum(net_change_list)/len(net_change_list), 2)

# Generate the output summary
output = (
    f'Financial Analysis\n'
    '-----------------------------------------------\n'
    f'Total Months: {total_months}\n'
    f'Total: {total_net}\n'
    f'Average Change: ${average_net}\n'
    f'Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})\n'
    f'Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})\n'
)

# Print the output
print(output)

# Write the results to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)
