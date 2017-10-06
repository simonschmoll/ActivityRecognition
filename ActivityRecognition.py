import pandas as pd
import numpy as np
num = 1
names_attributes = ['sequentialNumber','xAcceleration','yAcceleration','zAcceleration','lable']

#while (num < 16):
#Specifying engine = python because c engine can not handle sep
dataset = pd.read_csv('data/%d.csv' % (num), sep=', ', header=None, engine = 'python')
    # if num == 1:
    #     allData = dataset
    # else:
    #     allData = allData.append(dataset)
    #     print('This is all Data at point', num, allData)
    #num += 1
#print(dataset)
print(dataset.size)


#Feature Extraction
#For Feature Extraction we use a technique called window overlapping. It has an overlap of 50% between the different
#time series. As a time window 1 second is use --> corresponds to 52 samplings (52 Hz frequency)
#First we transform the Dataframe into an numpy array
arrayData = dataset.as_matrix()
#print(arrayData)
print(np.size(arrayData))
#Then we start with the sequencing
start = 0
end = 52
while start < np.size(arrayData)-1:
    newArray = arrayData.sl
#splitLists = np.array_split(arrayData, sections)

#getting the mean value of the different time sequences

print(np.size(splitLists))