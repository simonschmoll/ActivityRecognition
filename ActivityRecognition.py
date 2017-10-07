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
#Feature Extraction
#For Feature Extraction we use a technique called window overlapping (reserch paper 3). It has an overlap of 50% between the different
#time series. As a time window 1 second is use --> corresponds to 52 samplings (52 Hz frequency)
#First we transform the Dataframe into an numpy array
arrayData = dataset.as_matrix()
#print(arrayData)
print(np.size(arrayData))
#Then we start with the sequencing
start = int(0)
end = int(52)
dataList = []
while start < np.size(arrayData)-1:
    newArray = arrayData[slice(start, end)]
    dataList.append(newArray)
    start = start + 26
    end = end + 26
#To verify our results we print the size of the dataList--> as it are 162500 rows we should have (162500/26)
print(np.size(dataList))

#Now we need to get the mean value of all sequences
totalAverageValues = []
for i in dataList:
    x_acceleration = np.mean(dataList[i], 1)
    y_acceleration = np.mean(dataList[i], 2)
    z_acceleration = np.mean(dataList[i], 3)
    tempAverageValue = [x_acceleration[0], y_acceleration[0], z_acceleration[0]]
    totalAverageValues.append(tempAverageValue)
print(totalAverageValues)