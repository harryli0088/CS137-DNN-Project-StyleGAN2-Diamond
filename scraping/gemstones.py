# run this file if you want to scrape the gemstones

from bs4 import BeautifulSoup
import requests
import urllib.parse
import urllib.request

def getUrl(gemstone_color="white"):
  return "https://www.brilliantearth.com/colored-gemstones/list/?sortby=bestsell&colored_gemstone=all&gemstone_shape=all&gemstone_color="+gemstone_color+"&dimensions_range=all&origin=all&price_range=all&inventory_location=all&page=1&sid=&process=cyoring&can_preview=False&min_price=225&max_price=97480&price_range_min=225&price_range_max=97480&supplier=all&display=60&currency=%24"

# URLS to request
urls = [
  getUrl("white"),
  getUrl("peach"),
]

catalog = "GEM_URL\tIMAGE_URL\n" # used to record the data we're saving
count = 0 # used to track how many images were downloaded
for url in urls:
  page = requests.get(url) # make a GET request
  # print(page.text)

  soup = BeautifulSoup(page.content, "html.parser") # parse the HTML response

  for link in soup.select("a.clk_through.top_lg.pdp_url"): # find all the image anchors
    href = link.get('href') # get the diamond URL
    data_image = link.get('data-image') # get the image URL
    print("Saving Diamond:", href, data_image)

    urllib.request.urlretrieve( # save the image to file
      "http:"+data_image, "data/images/"+data_image.split("/")[-1]
    )
    catalog += href + "\t" + data_image + "\n" # make a record of this diamond
    count += 1 # increment the counter

print("Downloaded", count, "total images")

# write the catalog to a tsv file
f = open("data/catalog.tsv", "w")
f.write(catalog)
f.close()
