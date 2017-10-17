import numpy as np
header= ['sequentialNumber','xAcceleration','yAcceleration','zAcceleration','lable']

 # definition of the function for deleting rows with '0' as a label
 # @input: Pandas Dataframe, value of lable to delete
 # @output: array of int without lable 0
def zeroDet( dataset, value ):
    num = []
    num=(dataset.loc[dataset['label'] == value].index.values)
    dataClean=(dataset.drop(num))
    dataClean = dataClean.as_matrix()
    dataClean = dataClean.astype(np.int)
    return dataClean

