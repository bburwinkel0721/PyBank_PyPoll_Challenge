# Import in the CSV package so that we can work with the CSV
import csv

# Reads the CSV file and then turns the dates and profit/losses data into two lists
with open('./Resources/budget_data.csv', 'r') as file:
    reader = csv.reader(file)
    # Reads the headers of the columns into a variable
    header = next(reader)
    
    dates = []
    profit_losses_text = []
    for row in reader:
        dates.append(row[0])
        profit_losses_text.append(row[1])



# Creates a new list for profit/losses but with the values converted into integers
profit_losses = [int(value) for value in profit_losses_text]

# Stores the total amount of profit and loss into a variable
total = sum(profit_losses)

# Stores the total number of months into a variable
total_months = len(dates)

# Creates a list of all of the changes in profit
changes = [profit_losses[i+1] - profit_losses[i] for i in range(len(profit_losses)-1)]

# Creates a variable to add up all of the changes in profit
sum_changes = sum(changes)

# Stores the average change into a variable
average_changes = round(sum_changes/len(changes), 2)

# Stores the Greatest Increase in Profits and Greatest Decrease in Profits into variables
max_change = max(changes)
min_change = min(changes)

# Stores the dates for Greatest Increase in Profits and Greatest Decrease in Profits into variables
max_change_date = dates[changes.index(max_change)+ 1]
min_change_date = dates[changes.index(min_change) + 1]

# Prints out the Financial Analysis results to the terminal
print("Financial Analysis \n-----------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total}")
print(f"Average Change: ${average_changes}")
print(f"Greatest Increase in Profits: {max_change_date} (${max_change})")
print(f"Greatest Decrease in Profits: {min_change_date} (${min_change})")

# Writes out the Financial Analysis results to a text file
with open('./Analysis/Financial_Analysis_Results.txt', 'w') as f:
    f.write("Results from my Financial_Analysis:\n")
    f.write(f"Total Months: {total_months}\n")
    f.write(f"Total: ${total}\n")
    f.write(f"Average Change: ${average_changes}\n")
    f.write(f"Greatest Increase in Profits: {max_change_date} (${max_change})\n")
    f.write(f"Greatest Decrease in Profits: {min_change_date} (${min_change})")
    