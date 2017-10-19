import pandas as pd
import numpy as np
from mpl_toolkits import mplot3d
import numpy as np
from Miss_data import zeroDet
from DataHandling import read, count_labels ,d3Plot
from Feature_extraction_selection import grouping, extract_features
from Classification import classify,CrossValidation
# Importing data
dataframe = read(1)
#print(dataframe)
# Delete incorrect Data
cleaned_data = zeroDet(dataframe, 0)

#Check how balanced data is
counts = count_labels(cleaned_data)
print("Instances of every label, starting by one to seven",counts)

#Feature Extraction
grouped_data = grouping(cleaned_data)
features = extract_features(grouped_data)


#we are calling the function for classify our data, first with a simple
#splitting of the dataset to divide test and training set, after
#using k-crossvalidation with two different train model: 1)RandomForest classifier , 2)Super Vector Machine
classify(features.__getitem__(0),features.__getitem__(1))
CrossValidation(features.__getitem__(0),features.__getitem__(1),10)

