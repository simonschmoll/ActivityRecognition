import pandas as pd
import numpy as np


num = 1
names_attributes = ['sequentialNumber','xAcceleration','yAcceleration','zAcceleration','label']

#First we transform the Dataframe into an numpy array
#Specifying engine = python because c engine can not handle 'sep'
# @params: dataNum
# @output: dataset (Dataframe)
def read_convert(data_num):
    dataset = pd.read_csv('data/%d.csv' % (data_num), sep=',', header=None, engine='python', names=names_attributes)
    # array_data = dataset.as_matrix()
    # array_data = array_data.astype(np.int)

    # Comment in for printing out the array data and the size of the array
    # print(array_data)
    # print(np.size(array_data, 0))

    return dataset






