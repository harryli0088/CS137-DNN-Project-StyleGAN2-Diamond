# run this file if you want to scrape the gemstones

from bs4 import BeautifulSoup
import csv
from make_directory import make_directory
import requests
import urllib.parse
import urllib.request

make_directory("./data/gemstones-raw/") # make the raw directory if it does not exist

URL = "https://www.brilliantearth.com/colored-gemstones/list/"\
    "?sortby=bestsell&colored_gemstone=all&gemstone_shape=all&"\
    "gemstone_color=all&dimensions_range=all&origin=all&price_range=all&"\
    "inventory_location=all&page=1&sid=&process=cyoring&can_preview=False&"\
    "min_price=225&max_price=97480&price_range_min=225&"\
    "price_range_max=97480&supplier=all&display=2000&currency=%24"

catalog_data = []
count = 0 # used to track how many images were downloaded

page = requests.get(URL) # make a GET request
# print(page.text)

soup = BeautifulSoup(page.content, "html.parser") # parse the HTML response

for link in soup.select("a.clk_through.top_lg.pdp_url"): # find all the image anchors
    gemstone_url = link.get('href') # get the gemstone URL
    image_url = link.get('data-image') # get the image URL
    print("Saving Diamond:", gemstone_url, image_url)

    file_name = image_url.split("/")[-1]
    urllib.request.urlretrieve( # save the image to file
      "http:"+image_url, "data/gemstones-raw/"+file_name
    )
    catalog_data.append({
      "file_name": file_name,
      "gemstone_url": gemstone_url,
      "image_url": image_url,
    })
    count += 1 # increment the counter
    

print("Downloaded", count, "total images")

# https://www.tutorialspoint.com/How-to-save-a-Python-Dictionary-to-CSV-file
csv_columns = [
  "file_name",
  "gemstone_url",
  "image_url",
]
csv_file = "data/gemstones_catalog.csv"

try:
  with open(csv_file, 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
    writer.writeheader()
    for data in catalog_data:
      writer.writerow(data)
  print("Saved catalog data")
except IOError:
  print("I/O error")