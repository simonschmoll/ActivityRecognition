from pandas import read_csv
import numpy as np
#header= ['sequentialNumber','xAcceleration','yAcceleration','zAcceleration','lable']
num = 2
allData=read_csv('data/1.csv', header=None)
while(num < 16):
    dataset = read_csv('data/%d.csv' % (num), header=None)
    allData = allData.append(dataset,ignore_index=False,verify_integrity=False)
    num += 1

print(allData)


   # dataset = read_csv('data/%d.csv' % (num), header=None)

    #print(dataset.head(20))