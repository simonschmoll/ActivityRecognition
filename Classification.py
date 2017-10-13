# now we need to learn a random forest classifier (best fit according to  "Pierluigi Casale, Oriol Pujol, and Petia Radeva. Human activity recognition from accelerometer
# data using a wearable device. Pattern Recognition and Image Analysis, pages 289–296, 2011.
# [4] Wenchao Jiang and Zhaozheng Yin. Human activity recognition using wearable sensors by")
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_predict
#classifier = RandomForestClassifier().fit(featureAverageValue, target)
#prediction = cross_val_predict(classifier, featureAverageValue, target, cv=5)