from pandas import read_csv
import pandas as pd
import numpy
num = 1
names_attributes = ['sequentialNumber','xAcceleration','yAcceleration','zAcceleration','lable']

#while (num < 16):
dataset = read_csv('data/%d.csv' % (num), header=None)
    # if num == 1:
    #     allData = dataset
    # else:
    #     allData = allData.append(dataset)
    #     print('This is all Data at point', num, allData)
    #num += 1
print(dataset)

#Feature Extraction
#Mean Value
#feat_meanValue = np.mean(allData)
#gitprint(feat_meanValue)