import numpy as np

#Feature Extraction

#For Feature Extraction we use a technique called window overlapping (reserch paper 3). It has an overlap of 50% between the different
#time series. As a time window 1 second is use --> corresponds to 52 samplings (52 Hz frequency)
#Then we start with the sequencing
#Slicing needs to be done as follows:
#- it is not possible that 2 activities are grouped in one sequence (would falsify the outcome of the mean value)
#- therefore only labels with the same value are grouped into one sequence
#@params: array_data is list of array that contains the grouped data
def grouping(array_data):
    start = int(0)
    end = int(52)
    data_list = []
    length = np.size(array_data, 0)
    while start < length-52:
        if(array_data[start][4] != array_data[end-1][4]):
            while(array_data[start][4] != array_data[end-1][4]):
                end = end -1
            newArray = array_data[slice(start, end)]
            start = end
            end = end + 52
        else:
            newArray = array_data[slice(start, end)]
            start = start + 26
            end = end + 26
        data_list.append(newArray)
        if(end-52 > length - 1):
            end = length-1

    # Comment in to print out to a file and show the len and size of the data_list array
    # print(np.size(array_data))
    # print(len(data_list))
    return data_list

#Comment in for printing the data to a text file
# def sysout_to_text(dataList):
#     file = open("tempFile", "w")
#     for item in dataList:
#         file.write("%s\n" % item)
#     file.close()


#Now we need to get the mean value of all sequences
#@Params: grouped data_List containing the window arrays
#@Output: mean value of x, y, z, standard deviation of the coordinates, target array
def extract_features(data_list):
    total_average_values = []
    total_label = []
    for row in data_list:
        acceleration = np.nanmean(row, 0)
        standard_deviation = np.std(row, 0)
        temp_features = [acceleration[1], acceleration[2], acceleration[3], standard_deviation[1], standard_deviation[2], standard_deviation[3]]
        label_array = [row[0][4]]
        total_average_values.append(temp_features)
        total_label.append(label_array)
    print(total_average_values)
    print(total_label)
    feature = np.vstack(total_average_values)
    target = np.vstack(total_label)

    # comment in to print out lists
    # print(feature)
    # print(target)
    return feature, target


#Feature selection
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
#chi2 as we are dealing with a classifcation problem

def select_best_feature(feature, target):
    featureSelector = SelectKBest(chi2, k=1).fit_transform(feature, target)
    print(featureSelector)
    return featureSelector