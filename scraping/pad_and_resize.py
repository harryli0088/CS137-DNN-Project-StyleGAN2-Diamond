# StyleGAN requires all the input images to be square
# and have dimesions that are a power of 2

# This file will pad the images to be square then resize to (256,256)

import csv
from make_directory import make_directory
from PIL import Image


make_directory("./data/square/") # make the square directory if it does not exist 


# based on https://note.nkmk.me/en/python-pillow-add-margin-expand-canvas/
def pad_to_square(im, background_color="#aaaaaa"):
    width, height = im.size # get the dimensions
    if width == height: # if the dimensions are already square
        return im # we don't need to change anything
    elif width > height: # if the height is too small
        result = Image.new(im.mode, (width, width), background_color)
        result.paste(im, (0, (width - height) // 2))
        return result
    else: # else the width is too short
        result = Image.new(im.mode, (height, height), background_color)
        result.paste(im, ((height - width) // 2, 0))
        return result


def pad_and_resize_image(file_name:str):
    im = Image.open("./data/images/" + file_name) # open the image
        
    im = pad_to_square(im) # pad the image to be square

    im  = im.resize((256,256)) # resize the image to 256 x 256
    im.save("./data/square/" + file_name) # save the square image


with open("data/diamonds_catalog.csv") as fp:
    reader = csv.DictReader(fp)
    for row in reader: # check all the images
        pad_and_resize_image(row["file_name"])
