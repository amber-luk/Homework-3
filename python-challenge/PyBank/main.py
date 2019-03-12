import os
import csv

# csv_path = os.path.join("Users", "amberlukaesko", "Desktop", "UCI_DBC_ClassRepo", "UCIRV201902DATA3", "02-Homework", "03-Python", "Instructions", "PyBank", "Resources", "budget_data.csv")

csv_path = "/Users/amberlukaesko/Desktop/UCI_DBC_ClassRepo/UCIRV201902DATA3/02-Homework/03-Python/Instructions/PyBank/Resources/budget_data.csv"


with open(csv_path, newline="") as file:

    budget_data_reader = csv.reader(file, delimiter=",")

    csv_header = next(budget_data_reader)

    row_count = 0
    net_total = 0
    for row in budget_data_reader:
        row_count += 1
        net_total += int(row[1])
        row_val = int(row[1])

with open(csv_path, newline="") as file:

    budget_data_reader = csv.reader(file, delimiter=",")

    csv_header = next(budget_data_reader)

    next(budget_data_reader)

    change = []

    for row in budget_data_reader:
        next_row_val = int(row[1])
        # if int(row[1]) > 0:
        #     change += row_val - next_row_val
        # else:
        #     change += -(row_val + next_row_val)

        # if row_val > 0 and next_row_val > 0:
        #     change += row_val - next_row_val
        # elif row_val > 0 and next_row_val < 0:
        #     change += row_val + next_row_val
        # elif row_val < 0 and next_row_val > 0:
        #     change += row_val + next_row_val
        # elif row_val < 0 and next_row_val < 0:
        #     change += row_val + next_row_val

        # if row_val > next_row_val:
        #     change += -abs(row_val - next_row_val)
        # else:
        #     change += abs(row_val - next_row_val)


        # if row_val > next_row_val:
        #     if row_val > 0 and next_row_val > 0:
        #         change += next_row_val - row_val
        #     elif row_val > 0 and next_row_val < 0:
        #         change += -(row_val - next_row_val)
        #     elif row_val < 0 and next_row_val < 0:
        #         change += (abs(row_val) - abs(next_row_val))
        # else:
        #     if row_val > 0 and next_row_val > 0:
        #         change += next_row_val - row_val
        #     elif row_val < 0 and next_row_val > 0:
        #         change += abs(row_val) + abs(next_row_val)
        #     elif row_val < 0 and next_row_val < 0:
        #         change += abs(next_row_val) - abs(row_val)


        [change.append(next_row_val - row_val) for row in range(row_count - 1)]
        print(change[0:5])

    # average_change = change.sum() / row_count

    print(row_count)
    print(net_total)
    # print(average_change)
