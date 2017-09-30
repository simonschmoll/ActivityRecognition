import sklearn as metrics
import numpy as np
from numpy import genfromtxt
data1 = genfromtxt('data/1.csv', delimiter=',')
mylist = []
num = 1
while(num < 16):
    data = genfromtxt('data/%d.csv' % (num), delimiter=',')
    mylist.append(data)
    num += 1
print(mylist[0])

from pandas import read_csv
import numpy
num = 1
while(num < 16):
     dataset = read_csv('data/%d.csv' % (num), header=None)
     num += 1

     print(dataset.describe())