import sklearn as metrics
import numpy as np
from numpy import genfromtxt
data1 = genfromtxt('data/1.csv', delimiter=',')
mylist = [14]
num = 1
while(num < 16):
    data = genfromtxt('data/%d.csv' % (num), delimiter=',')
    mylist.append(data)
    num += 1
print(mylist[1])
