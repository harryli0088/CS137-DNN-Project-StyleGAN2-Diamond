import os

def make_directory(path:str):
    if not os.path.exists(path): # if the directory does not exist
        os.makedirs(path) # create the directory