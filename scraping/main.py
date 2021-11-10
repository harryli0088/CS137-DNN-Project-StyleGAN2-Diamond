from bs4 import BeautifulSoup
import requests
import urllib.parse
import urllib.request

# URL to request
URL = "https://www.brilliantearth.com/colored-gemstones/list/?sortby=bestsell&colored_gemstone=all&gemstone_shape=all&gemstone_color=white&dimensions_range=all&origin=all&price_range=all&inventory_location=all&page=1&sid=&process=cyoring&can_preview=False&min_price=225&max_price=97480&price_range_min=225&price_range_max=97480&supplier=all&display=60&currency=%24&abv=&tile_page_url=%2Fwhite-gemstones%2F&product_4_columns=ft13821"
page = requests.get(URL) # make a GET request
# print(page.text)

soup = BeautifulSoup(page.content, "html.parser")

catalog = "GEM_URL\tIMAGE_URL\n" # record the data we're saving
for link in soup.select("a.clk_through.top_lg.pdp_url"): # find all the image anchors
  href = link.get('href') # get the diamond URL
  data_image = link.get('data-image') # get the image URL
  print("Saving Diamond:", href, data_image)

  urllib.request.urlretrieve( # save the image to file
    "http:"+data_image, "data/images/"+data_image.split("/")[-1]
  )
  catalog += href + "\t" + data_image + "\n" # make a record of this diamond

# write the catalog to a tsv file
f = open("data/catalog.tsv", "w")
f.write(catalog)
f.close()
