import numpy as np
import os
import pandas as pd
from parse_features import parse_features
from PIL import Image
from skimage import io
import torch
from torch.utils.data import Dataset

class DiamondCatalogDataset(Dataset):
    """Diamond dataset. Based off https://pytorch.org/tutorials/beginner/data_loading_tutorial.html"""

    def __init__(self, csv_file, root_dir, transform=None):
        """
        Args:
            csv_file (string): Path to the csv file with annotations.
            root_dir (string): Directory with all the images.
            transform (callable, optional): Optional transform to be applied
                on a sample.
        """
        print(csv_file)
        self.frame = pd.read_csv(csv_file)
        self.root_dir = root_dir
        self.transform = transform

    def __len__(self):
        return len(self.frame)

    def __getitem__(self, idx):
        if torch.is_tensor(idx):
            idx = idx.tolist()

        this_iloc = self.frame.iloc[idx]
        img_name = os.path.join(self.root_dir,this_iloc.loc["file_name"])

        sample = {
          "carat": float(this_iloc.loc["carat"]),
          "clarity": parse_features("clarity",this_iloc.loc["clarity"]),
          "color": parse_features("color",this_iloc.loc["color"]),
          "cut": parse_features("cut",this_iloc.loc["cut"]),
          'image': Image.open(img_name),
          "price": float(this_iloc.loc["price"]),
          "shape": parse_features("shape",this_iloc.loc["shape"]),
        }

        if self.transform:
            sample["image"] = self.transform(sample["image"])
        # print("SAMPLE", sample)
        return sample