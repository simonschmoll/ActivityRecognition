# now we need to learn a random forest classifier (best fit according to  "Pierluigi Casale, Oriol Pujol, and Petia Radeva. Human activity recognition from accelerometer
# data using a wearable device. Pattern Recognition and Image Analysis, pages 289–296, 2011.
# [4] Wenchao Jiang and Zhaozheng Yin. Human activity recognition using wearable sensors by")
from sklearn.metrics import confusion_matrix
import numpy as np
from sklearn.metrics import f1_score
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn import svm

#function to classify without crossvalidaion:
#we created here funtion to predict with Random forest and SVM the values with a simple division of the dataset.
#we split infact the dataset in 2 part:Training and test set and we provide the follow estimators:
#1)F1score
#2)Accuracy
#3)Confusion Matrix

def classify(x_features, y_features):
    X_train, X_test, y_train, y_test = train_test_split(x_features, y_features.ravel(), test_size=0.2, random_state=0)
    X_train.shape, y_train.shape
    X_test.shape, y_test.shape
    forest= RandomForestClassifier(n_estimators=100, random_state=0)
    clf = svm.SVC(kernel='linear', C=1)
    model = forest.fit(X_train,y_train )
    modelSv=clf.fit(X_train,y_train )
    predicted_labels = model.predict(X_test)
    predicted_labelsSv = modelSv.predict(X_test)

    # Compute the F1 score, also known as balanced F-score or F-measure
    # The F1 score can be interpreted as a weighted average of the precision and recall,
    #  where an F1 score reaches its best value at 1 and worst score at 0.
    #  The relative contribution of precision and recall to the F1 score are equal.
    #  The formula for the F1 score is:
    # F1 = 2 * (precision * recall) / (precision + recall)
    # In the multi-class and multi-label case, this is the weighted average of the F1 score of each class.

    print(" F1 score Random forest: %f" % f1_score(y_test, predicted_labels, average='macro'))
    print(" F1 score precision with SV: %f" % f1_score(y_test, predicted_labels, average='macro'))

    print("Accuracy Random forest: %f" % metrics.accuracy_score(y_test, predicted_labels))
    print("Accuracy with SV: %f" % metrics.accuracy_score(y_test, predicted_labelsSv))
    #By definition a confusion matrix C is such that C_{i, j}
    # is equal to the number of observations known to be in group i but predicted to be in group j.
    print("Confusion Matrix Random forest: ")
    print(confusion_matrix(y_test, predicted_labels, labels=[1, 2, 3, 4, 5, 6, 7]))
    print("Confusion Matrix with SV: ")
    print(confusion_matrix(y_test, predicted_labelsSv, labels=[1, 2, 3, 4, 5, 6, 7]))
    return



def CrossValidation(x_features, y_features, kfold):
    forest = RandomForestClassifier(n_estimators=100, random_state=0)
    clf = svm.SVC(kernel='linear', C=1)
    scoresSv = cross_val_score(clf, x_features, y_features.ravel(), cv=kfold)
    scores = cross_val_score(forest, x_features, y_features.ravel(), cv=kfold)
    print("Accuracy Random Forest: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))
    print("Accuracy with SV: %0.2f (+/- %0.2f)" % (scoresSv.mean(), scoresSv.std() * 2))
    return

