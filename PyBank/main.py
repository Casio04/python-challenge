
import csv
import os
import datetime

budget_bank = os.path.join("Resources","budget_data.csv")
total_months = 0
total_amount = 0
average_change = 0
next_value = 0
actual_value = 0
change_sum = 0
next_increase = 0
next_decrease = 0
max_increase = 0
max_decrease = 0

# Open csv file with reading permissions
with open(budget_bank, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    # Skip header
    header = next(csvreader)

    for row in csvreader:
            # Get the current values and store them in different vaariables to accomplish the max, min and average change questions.
            actual_increase = next_increase
            actual_decrease = next_decrease
            next_value = int(row[1])
            if csvreader.line_num > 2:
                next_increase = next_value - actual_value
                next_decrease = next_value - actual_value
                change_sum = change_sum + (next_value - actual_value)
                if next_increase > max_increase:
                    max_increase = next_increase
                    month_increase = row[0]

                if next_decrease < max_decrease:
                    max_decrease = next_decrease
                    month_decrease = row[0]

            total_months = total_months + 1
            total_amount = (total_amount + int(row[1]))
            average_change = total_amount / total_months
            actual_value = next_value


    month_increase =  datetime.datetime.strptime(str(month_increase),"%b-%y").strftime("%b-%Y")      
    month_decrease =  datetime.datetime.strptime(str(month_decrease),"%b-%y").strftime("%b-%Y")      
    average_change = round(change_sum / (total_months - 1),2)
    result =f"""
    Financial Analyisis
    --------------------------
    Total Months: {total_months}
    Total: ${total_amount}
    Average Change: ${average_change}
    Greatest Increase in Profits: {month_increase} (${max_increase})
    Greatest Decrease in Profits: {month_decrease} (${max_decrease})
    """ 
    print(result)

output_file = os.path.join("Analysis","PyBank_results.txt")

open(output_file, "w").write(result)
