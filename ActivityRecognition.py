from pandas import read_csv
import pandas as pd
import numpy
num = 1
names_attributes = ['sequentialNumber','xAcceleration','yAcceleration','zAcceleration','lable']

while(num < 16):
     table = pd.read_csv('data/%d.csv' % (num), sep=',', index_col=False)
     if num == 1:
         all_tables = table
     else:
         all_tables = pd.concat([all_tables, table])
     num += 1

print(all_tables)
