import numpy as np
header= ['sequentialNumber','xAcceleration','yAcceleration','zAcceleration','lable']

 #define the function for  delete rows with 0 Labels
 # @input: Pandas Dataframe, value of lable to delet
 # @output: Array of int without lable 0
def zeroDet( dataset, value ):
    num = []
    num=(dataset.loc[dataset['lable'] == value].index.values)
    dataClean=(dataset.drop(num))
    dataClean = dataClean.as_matrix()
    dataClean = dataClean.astype(np.int)
    return dataClean

