from pandas import read_csv
import pandas as pd
import numpy as np

def read_data_set():
    num = 1
    while(num < 16):
         dataset = read_csv('data/%d.csv' % (num), header=None)
         if num == 1:
              allData = dataset
         else:
             allData = allData.append(dataset)
             print('This is all Data at point',num, allData)
         num += 1

#Feature Extraction
#Mean Value
#feat_meanValue = np.mean(allData)
#gitprint(feat_meanValue)