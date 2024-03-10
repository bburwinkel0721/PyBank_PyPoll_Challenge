import pandas

# converts the CVS file into a dataframe that we can use
budget = pandas.read_csv("./Resources/budget_data.csv")

# Separates out the columns for dates and for profit/loss into two separate data frames
dates = budget.Date
profit_losses = budget["Profit/Losses"]

# Stores the total amount of profit and loss into a variable
total = profit_losses.sum()

# Stores the total number of months into a variable
total_months = 0
for date in dates:
    total_months += 1

# Creates a list of all of the changes in profit
changes = [profit_losses[i+1] - profit_losses[i] for i in range(len(profit_losses)-1)]

# Creates a variable to add up all of the changes in profit
sum_changes = 0
for change in changes:
    sum_changes += change

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
print("Total Months: {}".format(total_months))
print("Total: ${}".format(total))
print("Average Change: ${}".format(average_changes))
print("Greatest Increase in Profits: {} (${})".format(max_change_date,max_change))
print("Greatest Decrease in Profits: {} (${})".format(min_change_date,min_change))

# Writes out the Financial Analysis results to a text file
with open('./Analysis/Financial_Analysis_Results.txt', 'w') as f:
    f.write("Results from my Financial_Analysis:\n")
    f.write("Total Months: {}\n".format(total_months))
    f.write("Total: ${}\n".format(total))
    f.write("Average Change: ${}\n".format(average_changes))
    f.write("Greatest Increase in Profits: {} (${})\n".format(max_change_date,max_change))
    f.write("Greatest Decrease in Profits: {} (${})\n".format(min_change_date,min_change))
