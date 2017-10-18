# now we need to learn a random forest classifier (best fit according to  "Pierluigi Casale, Oriol Pujol, and Petia Radeva. Human activity recognition from accelerometer
# data using a wearable device. Pattern Recognition and Image Analysis, pages 289–296, 2011.
# [4] Wenchao Jiang and Zhaozheng Yin. Human activity recognition using wearable sensors by")
from sklearn.model_selection import cross_val_predict
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import TimeSeriesSplit
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
from sklearn.model_selection import train_test_split


#function to classify without crossvalidaion

def classify(x_features, y_features):
    X_train, X_test, y_train, y_test = train_test_split(x_features, y_features.ravel(), test_size=0.2, random_state=0)
    X_train.shape, y_train.shape
    X_test.shape, y_test.shape
    forest= RandomForestClassifier(n_estimators=100, random_state=0)
    model = forest.fit(X_train,y_train )
    predicted_labels = model.predict(X_test)
    print(metrics.accuracy_score(y_test, predicted_labels))
    return

def CrossValidation(x_features, y_features, kfold):
    forest = RandomForestClassifier(n_estimators=100, random_state=0)
    #print(metrics.accuracy_score(y_test, predicted_labels))
    #print(metrics.average_precision_score())
    scores = cross_val_score(forest, x_features, y_features.ravel(), cv=kfold)
    print("Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))
    return

#time slip
# tscv = TimeSeriesSplit(n_splits=3)
# print(tscv)
# for train, test in tscv.split(features.__getitem__(0)):
#     print("%s %s" % (train, test))