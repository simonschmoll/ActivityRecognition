import pandas as pd
import numpy as np

from Miss_data import zeroDet
from DataHandling import read_convert
from Feature_extraction_selection import grouping, extract_features,select_best_feature

# Importing data
dataframe = read_convert(1)

# Delete incorrect Data
# cleaned_data = zeroDet(dataframe, 0)
# Just now I will convert by hand
array_data = dataframe.as_matrix()
array_data = array_data.astype(np.int)

#Feature Extraction
grouped_data = grouping(array_data)
features = extract_features(grouped_data)
#To verify our results we print the size of the dataList--> as it are 162500 rows we should have (162500/26)
# print(np.size(dataList))
# print(dataList)

