# run this file if you want to scrape the diamonds

import csv
import json
import requests
import urllib.request

SHAPES = ["Round","Oval","Cushion","Pear","Princess","Emerald","Marquise","Asscher","Radiant","Heart"]


def getUrl(shape="Round",page=1):
  """returns the URL to request JSON data for the diamonds
     
     You could concat multiple shapes together, ie like "shapes=Round%2COval"
     but requesting them separately ensures that you will get a guaranteed
     number of each shape (in case multiple shapes are not distributed even).

  Args:
      shape (str, optional): shape. Defaults to "Round".
      page (int, optional): pagination number. Defaults to 1.

  Returns:
      str: URL
  """
  return "https://www.brilliantearth.com/loose-diamonds/list/?shapes="+shape+"&cuts=Fair%2CGood%2CVery%20Good%2CIdeal%2CSuper%20Ideal&colors=J%2CI%2CH%2CG%2CF%2CE%2CD&clarities=SI2%2CSI1%2CVS2%2CVS1%2CVVS2%2CVVS1%2CIF%2CFL&polishes=Good%2CVery%20Good%2CExcellent&symmetries=Good%2CVery%20Good%2CExcellent&fluorescences=Very%20Strong%2CStrong%2CMedium%2CFaint%2CNone&min_carat=0.25&max_carat=12.05&min_table=46.00&max_table=87.00&min_depth=3.50&max_depth=94.30&min_price=420&max_price=465880&stock_number=&row=0&page="+str(page)+"&requestedDataSize=200&order_by=cut&order_method=desc&currency=%24&has_v360_video=&dedicated=&min_ratio=1.00&max_ratio=2.75&shipping_day=&suppler_shipping_day=&exclude_quick_ship_suppliers=&MIN_PRICE=420&MAX_PRICE=465880&MIN_CARAT=0.25&MAX_CARAT=12.05&MIN_TABLE=45&MAX_TABLE=87&MIN_DEPTH=3.5&MAX_DEPTH=94.3"


catalog_data = []
for shape in SHAPES: # loop through all the shapes
  # TODO paginate?
  
  response = requests.get(getUrl(shape)) # make a GET request
  response_dict = response.json() # parse the JSON response into a dictionary

  for diamond in response_dict["diamonds"]: # loop through all the diamonds
    for real_image in diamond["images"]["real_images"]: # loop through all the real images for this diamond (usually only 1)
      id = diamond["id"]
      src = real_image["src"]

      print("Saving Diamond:", id)

      urllib.request.urlretrieve( # save the image to file
        "http:"+src, "data/images/"+src.split("/")[-1]
      )
      catalog_data.append({
        "id": diamond["id"],
        "real_image_src": src,
        # if you want to record other data, add it here, then update csv_columns
      })

print("Downloaded", len(catalog_data), "total images")


# https://www.tutorialspoint.com/How-to-save-a-Python-Dictionary-to-CSV-file
csv_columns = ['id','real_image_src']
csv_file = "diamonds_catalog.csv"
try:
  with open(csv_file, 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
    writer.writeheader()
    for data in catalog_data:
      writer.writerow(data)
  print("Saved catalog data")
except IOError:
  print("I/O error")