import csv

def track_feature(row, tracker:dict, key:str="") -> None:
    feature = row[key] # get the value of this feature
    if feature not in tracker: # if we are encountering this feature name for the first time
        tracker[feature] = 0 # initialize the count to 0
    tracker[feature] += 1 # increment the count for this feature
    
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
        count += 1 # increemnt count

print("Total # of diamonds:", count)


def print_tracker(tracker:dict) -> None:
    print("------------------------------------")
    for key in tracker:
        print(key, "has a total of", tracker[key], "diamonds")

print_tracker(clarity_tracker)
print_tracker(color_tracker)
print_tracker(shape_tracker)