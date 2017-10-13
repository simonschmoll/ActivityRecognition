from pandas import read_csv
import numpy as np
header= ['sequentialNumber','xAcceleration','yAcceleration','zAcceleration','lable']
# num = 1
#allData=read_csv('data/1.csv', header=None)
# while(num < 16):
#  #   dataset = read_csv('data/%d.csv' % (num), header=None)
#  #   allData = allData.append(dataset,ignore_index=False,verify_integrity=False)
#     dataset = read_csv('data/%d.csv' % (num) , names=header)
#     boolData = dataset.isnull()
#     for idx in header:
#        print(boolData.loc[boolData[idx] == True])
#     num += 1
 #print(allData)

 #define the function for  delete rows with 0 Labels
 # @input: Pandas Dataframe, value of lable to delet
 # @output: Array of int without lable 0
def zeroDet( dataset, value ):
    num = []
    num=(dataset.loc[dataset['lable'] == value].index.values)
    dataClean=(dataset.drop(num))
    dataClean = dataClean.as_matrix()
    dataClean = dataClean.astype(np.int)
    return dataClean

# dataset=read_csv('data/1.csv', names=header)
# dataArray=zeroDet(dataset,0)
# print(dataArray)
