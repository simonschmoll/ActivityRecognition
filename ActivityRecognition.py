import pandas as pd
import numpy as np


num = 1
names_attributes = ['sequentialNumber','xAcceleration','yAcceleration','zAcceleration','lable']


#Specifying engine = python because c engine can not handle sep
dataset = pd.read_csv('data/%d.csv' % (num), sep=',', header=None, engine = 'python', names = names_attributes)

#Feature Extraction
#For Feature Extraction we use a technique called window overlapping (reserch paper 3). It has an overlap of 50% between the different
#time series. As a time window 1 second is use --> corresponds to 52 samplings (52 Hz frequency)
#First we transform the Dataframe into an numpy array
arrayData = dataset.as_matrix()

#Conversio to int array
arrayData = arrayData.astype(np.int)
print(arrayData)
print(np.size(arrayData, 0))

#Next we need to extract different arrays with the same activity


#Then we start with the sequencing
#Slicing needs to be done as follows:
#- it is not possible that 2 activities are grouped in one sequence (would falsify the outcome of the mean value)
#- therefore only labels with the same value are grouped into one sequence
start = int(0)
end = int(52)
dataList = []
length = np.size(arrayData, 0)
while start < length-52:
    if(arrayData[start][4] != arrayData[end-1][4]):
        while(arrayData[start][4] != arrayData[end-1][4]):
            end = end -1
        newArray = arrayData[slice(start, end)]
        start = end
        end = end + 52
    else:
        newArray = arrayData[slice(start, end)]
        start = start + 26
        end = end + 26
    dataList.append(newArray)
    if(end-52 > length - 1):
        end = length-1
file = open("tempFile", "w")
print(np.size(arrayData))
print(len(dataList))

#Comment in for printing the data to a text file
# for item in dataList:
#   file.write("%s\n" % item)
# file.close()

#To verify our results we print the size of the dataList--> as it are 162500 rows we should have (162500/26)
# print(np.size(dataList))
# print(dataList)

#Now we need to get the mean value of all sequences
totalAverageValues = []
total_label = []
for row in dataList:
    acceleration = np.nanmean(row, 0)
    tempAverageValue = [acceleration[1], acceleration[2], acceleration[3]]
    label_array = row[0][4]
    totalAverageValues.append(tempAverageValue)
    total_label.append(label_array)
print(totalAverageValues)
print(len(totalAverageValues))
#print(total_label)
feature = np.vstack(totalAverageValues)
target = np.vstack(total_label)
print(target)
print(feature)


# now we need to learn a random forest classifier (best fit according to  "Pierluigi Casale, Oriol Pujol, and Petia Radeva. Human activity recognition from accelerometer
# data using a wearable device. Pattern Recognition and Image Analysis, pages 289–296, 2011.
# [4] Wenchao Jiang and Zhaozheng Yin. Human activity recognition using wearable sensors by")
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_predict
classifier = RandomForestClassifier()
prediction = cross_val_predict(classifier, feature, target, cv=5)

