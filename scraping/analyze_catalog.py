import csv
import os
from PIL import Image
from shutil import copyfile
from typing import Set, TypedDict

dimensions_set:Set[str] = set()

def track_feature(row, tracker:dict, key:str="") -> None:
    feature = row[key] # get the value of this feature
    if feature not in tracker: # if we are encountering this feature name for the first time
        tracker[feature] = { # initialize the counts to 0
          "is_square": 0,
          "total": 0,
        }
    tracker[feature]["total"] += 1 # increment the count for this feature

    # # check if the image is square
    # im = Image.open("./data/diamonds-raw/" + row["file_name"])
    # dimensions = im.size

    # dimensions_set.add(str(im.size[0]) + " - " + str(im.size[1])) # record the dimension of the image

    # # check if the image is not 300 pixels in 1 direction
    # if dimensions[0]!=300 == dimensions[1]!=300:
    #     print("WARNING:",row["file_name"],"does not have a dimension with 300",im.size)

    # if dimensions[0] == dimensions[1]:
    #     # copyfile("./data/raw/" + row["file_name"], "./data/square/" + row["file_name"])
    #     tracker[feature]["is_square"] += 1 # increment the count for square images

    
clarity_tracker = {}
color_tracker = {}
shape_tracker = {}


# Read CSV file
count = 0
with open("data/diamonds_catalog.csv") as fp:
    reader = csv.DictReader(fp)
    for row in reader:
        track_feature(row, clarity_tracker, "clarity")
        track_feature(row, color_tracker, "color")
        track_feature(row, shape_tracker, "shape")
        count += 1 # increment count

print("Total # of diamonds:", count)


def print_tracker(tracker:dict) -> None:
    print("------------------------------------")
    for key in tracker:
        print(key, "has a total of", tracker[key]["total"], "diamonds.", tracker[key]["is_square"], "of them are square (",tracker[key]["is_square"]/tracker[key]["total"],")")

print_tracker(clarity_tracker)
print_tracker(color_tracker)
print_tracker(shape_tracker)
print("dimensions_set",dimensions_set)