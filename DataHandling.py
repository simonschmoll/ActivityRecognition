from pandas import read_csv
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

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

#3d plot Graph
#Here we reate a simple funcion to create the plot of the data
#of our original dataset. The different 7 colour corrispond our 7 labels
#@input:database in a matrix Array
#@output:plot of the point in a 3d structure

def d3Plot(dataset):
    def column(matrix, i):
        return [row[i] for row in matrix]
    ax = plt.axes(projection='3d')
    # Data for three-dimensional scattered points
    zdata= column(dataset,3)
    ydata= column(dataset,2)
    xdata= column(dataset,1)
    lable= column(dataset,4)
    colors = ['orange','green','blue','purple','yellow','black','orange','white']
    ax.scatter3D(xdata, ydata, zdata, c=lable, cmap=matplotlib.colors.ListedColormap(colors))
    return plt.show()



