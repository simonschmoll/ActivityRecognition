import pandas as pd
import numpy as np
from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
from Miss_data import zeroDet
from DataHandling import read, count_labels
from Feature_extraction_selection import grouping, extract_features,select_best_feature
from Classification import classify
from Classification import CrossValidation
# Importing data
dataframe = read(1)
#print(dataframe)
# Delete incorrect Data
cleaned_data = zeroDet(dataframe, 0)
# Just now I will convert by hand
# array_data = dataframe.as_matrix()
# array_data = array_data.astype(np.int)
# print(np.size(array_data,0))

print(cleaned_data)

#Check how balanced data is
counts = count_labels(cleaned_data)
print(counts)

#Feature Extraction
grouped_data = grouping(cleaned_data)
#print(np.size(grouped_data,0))
features = extract_features(grouped_data)

#Feature Selection
#print(features.__getitem__(0))
selected_feature = select_best_feature(features.__getitem__(0), features.__getitem__(1))
#print(selected_feature.__class__)
# To verify our results we print the size of the dataList--> as it are 162500 rows we should have (162500/26)
# print(np.size(dataList))
# print(dataList)


classify(selected_feature,features.__getitem__(1))

CrossValidation(selected_feature,features.__getitem__(1),10)

#3d plot Graph

def column(matrix, i):
    return [row[i] for row in matrix]

ax = plt.axes(projection='3d')
# Data for three-dimensional scattered points
zdata= column(cleaned_data,3)
ydata= column(cleaned_data,2)
xdata= column(cleaned_data,1)
ax.scatter3D(xdata, ydata, zdata, c=zdata, cmap='Greens');
