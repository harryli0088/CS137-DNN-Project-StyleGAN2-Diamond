# run this file after gemstones_angles.py

import csv
import os

# Read CSV file
new_catalog = []
with open("data/gemstones_angles_catalog.csv") as fp:
    reader = csv.DictReader(fp)
    for row in reader:
        idx = row["idx"]
        if idx == "0": # if this is the zeroeth index image
            # delete it
            file_name = row["file_name"]
            try:
                os.remove("data/gemstones_angles-raw/" + file_name)
            except FileNotFoundError:
                print("File was already deleted", file_name)
        else:
            new_catalog.append(row) # else we want to keep this image


# https://www.tutorialspoint.com/How-to-save-a-Python-Dictionary-to-CSV-file
csv_columns = [
  "file_name",
  "gemstone_id",
  "gemstone_url",
  "idx",
  "image_url",
]
csv_file = "data/gemstones_angles_catalog.csv"

try:
  with open(csv_file, 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
    writer.writeheader()
    for data in new_catalog:
      writer.writerow(data)
  print("Saved catalog data")
except IOError:
  print("I/O error")