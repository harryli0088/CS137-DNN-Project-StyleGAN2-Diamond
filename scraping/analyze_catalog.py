import csv
import os
from PIL import Image
from typing import TypedDict

def track_feature(row, tracker:dict, key:str="") -> None:
    feature = row[key] # get the value of this feature
    if feature not in tracker: # if we are encountering this feature name for the first time
        tracker[feature] = { # initialize the counts to 0
          "is_square": 0,
          "total": 0,
        }
    tracker[feature]["total"] += 1 # increment the count for this feature

    # check if the image is square
    im = Image.open("./data/images/" + row["file_name"])
    dimensions = im.size
    if dimensions[0] == dimensions[1]:
        tracker[feature]["is_square"] += 1 # increment the count for square images


# class FeatureTracker(TypedDict):
#     is_sqaure: int
#     total: int

    
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