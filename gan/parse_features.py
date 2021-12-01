from typing import Union

# based off https://www.brilliantearth.com/round-diamonds-search/
FEATURE_MAP = {
  "COLOR": ["J","I","H","G","F","E","D"],
  "CUT": ["FAIR", "GOOD", "VERY GOOD", "IDEAL", "SUPER IDEAL"],
  "CLARITY": ["SI2","SI1","VS2","VS1","VVS2","VVS1","IF","FL"],
  "SHAPE": [
    "PRINCESS", "RADIANT", "EMERALD", "ASSCHER",  "CUSHION",
    "ROUND", "OVAL", "PEAR", "MARQUISE", "HEART"
  ],
}


def parse_features(feature:str = "color", value: str = "J") -> float:
    """returns a numeric representation of the feature

    Args:
        feature (str, optional): name of the feature. Defaults to "color".
        value (str, optional): value of the feature. Defaults to "J".

    Raises:
        ValueError: if the feature or value is not valid

    Returns:
        float: index of the feature value as a float
    """

    feature = feature.upper() # convert to upper case
    if feature in FEATURE_MAP: # if the feature is valid
        valid_values = FEATURE_MAP[feature] # get the list of values for this feature
        value = value.upper() # convert to upper case
        if value in valid_values: # if the value is valid
            return float(valid_values.index(value)) # return the index of the value for the feature
        else:
            raise ValueError('Argument "value" must be one of ',valid_values,' Received ' + value)
    else:
        raise ValueError('Argument "feature" must be one of ["color", "cut", "clarity", "shape"]. Received ' + feature)


