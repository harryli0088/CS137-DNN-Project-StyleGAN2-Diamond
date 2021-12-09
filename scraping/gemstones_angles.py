# this file assumes you have already run gemstones.py
# this file gets the angles of the diamonds found in ./data/gemstones-datalog.csv

import base64
import csv
from make_directory import make_directory
import requests
from PIL import Image

make_directory("./data/gemstones_angles-raw/") # make the raw directory if it does not exist

catalog_data = []

# Read CSV file
with open("data/gemstones_catalog.csv") as fp:
    reader = csv.DictReader(fp)
    for row in reader:
        id = row["gemstone_url"].split("/")[1].split("-")[-1] # get the id of the gemstone

        print("Requesting for", id)
        url = "https://image.brilliantearth.com/media/v360/imaged/"+id+"/sm.json" # create the URL to request
        
        response = requests.get(url) # request the URL
        
        try:
            response = response.json() # convert to JSON
        except ValueError:
            print(ValueError)
            continue

        print("response", id, len(response))

        if type(response) is not list: # if the response is not a list
            print("WARNING, expected response to be a list. Received", type(response))
            continue

        for idx, img_str in enumerate(response): # loop through all the image responses
            print("img_str", img_str)
            file_name = id + "-" + str(idx) + ".jpeg" # create a name for this file

            with open("data/gemstones_angles-raw/"+file_name, "wb") as fh:
                fh.write(base64.b64decode(img_str)) # save the image

                catalog_data.append({ # record this in the catalog
                    "file_name": file_name,
                    "gemstone_id": id,
                    "gemstone_url": row["gemstone_url"],
                    "idx": idx,
                    "image_url": row["image_url"],
                })
        break


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
    for data in catalog_data:
      writer.writerow(data)
  print("Saved catalog data")
except IOError:
  print("I/O error")