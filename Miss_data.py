from pandas import read_csv
import numpy as np
num = 1
while(num < 16):
     dataset = read_csv('data/%d.csv' % (num), header=None)
     dataArray = dataset.as_matrix()
     if num == 1:
          allData = dataArray
     else:
         np.append(allData, dataArray)
     num += 1

print(allData)


   # dataset = read_csv('data/%d.csv' % (num), header=None)

    #print(dataset.head(20))