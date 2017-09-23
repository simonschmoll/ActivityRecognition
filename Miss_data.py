from pandas import read_csv
import numpy
num = 1
while(num < 16):
     dataset = read_csv('data/%d.csv' % (num), header=None)
     num += 1
     print(dataset.describe())
   # dataset = read_csv('data/%d.csv' % (num), header=None)

    #print(dataset.head(20))