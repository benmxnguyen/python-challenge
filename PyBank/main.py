# Import modules needed
import csv
import os

#set file path
csvpath = os.path.join("Resources", "budget_data.csv").replace("\\", "/")


#open csv using with and saving it into a variable
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile)

    #strip and store header
    csv_header = next(csvreader)

    #creating empty lists
    dates = []
    profits = []

    #populating the empty lists and finding total
    total = 0
    for row in csvreader:
        dates.append(row[0])
        profits.append(int(row[1]))
        total = total + int(row[1])

    #find total number of months
    total_months = len(dates)

    #-----------------------------------------------------------
    #find total w/o for loop
    #total = sum(profits)
    #-----------------------------------------------------------

    #calculating change between each period
    changes_between = []
    for i in range(len(profits) - 1):
            changes_between.append(profits[i+1] - profits[i])


    #find average of changes
    avg_change = round(sum(changes_between)/len(changes_between),2)

    #find greatest increase and decrease using for loop
    max_greatest_inc = 0
    for index,changes in enumerate(changes_between):
        if changes > max_greatest_inc:
            max_greatest_inc = changes
            for_greatest_inc_date = dates[index + 1]

    
    max_greatest_dec = 0
    for index,changes in enumerate(changes_between):
        if changes < max_greatest_dec:
            max_greatest_dec = changes
            for_greatest_dec_date = dates[index + 1]
    
    #-----------------------------------------------------------
    #find greatest increase and decrease
    # greatest_inc = max(changes_between)
    # greatest_dec = min(changes_between)
    # greatest_inc_date = dates[changes_between.index(greatest_inc) + 1]
    # greatest_dec_date = dates[changes_between.index(greatest_dec) + 1]
    greatest_inc_pair = (for_greatest_inc_date, max_greatest_inc)
    greatest_dec_pair = (for_greatest_dec_date, max_greatest_dec)
    #-----------------------------------------------------------

    #print results to terminal
    print(f"Financial Analysis\n"
         "-------------------------\n"
          f"Total Months: {total_months}\n"
          f"Total: ${total}\n"
          f"Average Change: ${avg_change}\n"
          f"Greatest Increase in Profits: {greatest_inc_pair[0]} (${greatest_inc_pair[1]})\n"
          f"Greatest Decrease in Profits: {greatest_dec_pair[0]} (${greatest_dec_pair[1]})\n"
           "-------------------------\n"
                    "")

    #writing to a text file
    #setting path for file
    results_path = os.path.join("analysis", "results.txt").replace("\\", "/")
    with open(results_path, 'w') as file:
        file.write(f"Financial Analysis\n"
                    "-------------------------\n"
                    f"Total Months: {total_months}\n"
                    f"Total: ${total}\n"
                    f"Average Change: ${avg_change}\n"
                    f"Greatest Increase in Profits: {greatest_inc_pair[0]} (${greatest_inc_pair[1]})\n"
                    f"Greatest Decrease in Profits: {greatest_dec_pair[0]} (${greatest_dec_pair[1]})\n"
                    "-------------------------\n"
                            "")
