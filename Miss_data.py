import numpy as np
from pandas import read_csv
header= ['sequentialNumber','xAcceleration','yAcceleration','zAcceleration','label']

 # definition of the function for deleting rows with '0' as a label
 # @input: Pandas Dataframe, value of lable to delete
 # @output: array of int without lable 0
def zeroDet( dataset, value ):
    num = []
    num=(dataset.loc[dataset['label'] == value].index.values)
    dataClean=(dataset.drop(num))
    dataClean = dataClean.as_matrix()
    dataClean = dataClean.astype(np.int)
    return dataClean

#here we are trying to detect if there are some
#missing data in all dataset.
#To prove there aren't missing data,
#output should generate empty arrays
num = 1
while(num < 16):
    dataset = read_csv('data/%d.csv' % (num) , names=header)
    boolData = dataset.isnull()
    for name in header:
        print(boolData.loc[boolData[name] == True])
    num += 1