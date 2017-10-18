from pandas import read_csv
import numpy as np

num = 1
names_attributes = ['sequentialNumber','xAcceleration','yAcceleration','zAcceleration','label']

#First we transform the Dataframe into an numpy array
#Specifying engine = python because c engine can not handle 'sep'
# @params: dataNum
# @output: dataset (Dataframe)
def read(data_num):
    dataset = read_csv('data/%d.csv' % (data_num), sep=',', header=None, engine='python', names=names_attributes)

    # Comment in for printing out the array data and the size of the array
    # print(array_data)
    # print(np.size(array_data, 0))

    return dataset

# This function checks how balanced the data is
# @Input: data_array with labels
# @Output: list with different counts for the labels
def count_labels(data_array):
    result_count = []
    count = np.int
    count = 0
    label_data = data_array[:,[4]]
    unique, counts = np.unique(label_data, return_counts=True)
    ret = dict(zip(unique, counts))
    return ret




