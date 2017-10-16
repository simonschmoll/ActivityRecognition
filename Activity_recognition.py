import pandas as pd
import numpy as np

from Miss_data import zeroDet
from DataHandling import read
from Feature_extraction_selection import grouping, extract_features,select_best_feature
# Importing data
dataframe = read(1)
print(dataframe)
# Delete incorrect Data
# cleaned_data = zeroDet(dataframe, 0)
# Just now I will convert by hand
array_data = dataframe.as_matrix()
array_data = array_data.astype(np.int)
print(np.size(array_data,0))

#Feature Extraction
grouped_data = grouping(array_data)
print(np.size(grouped_data,0))
features = extract_features(grouped_data)

#Feature Selection
print(features.__getitem__(0))
selected_feature = select_best_feature(features.__getitem__(0), features.__getitem__(1))
print(selected_feature.__class__)
# To verify our results we print the size of the dataList--> as it are 162500 rows we should have (162500/26)
# print(np.size(dataList))
# print(dataList)

