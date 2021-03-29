import os
import csv

pybank_csv = os.path.join("..", "Resources", "budget_data.csv")

# Open and read csv
with open(pybank_csv) as csv_file:
    csv_pybank_data = csv.reader(csv_file, delimiter=",")

    # Read the header row first (skip this part if there is no header)
    csv_header = next(csv_file)
    print(f"Header: {csv_header}")