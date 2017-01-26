import sys

sys.path.append("../../")

from class_vis import prettyPicture, output_image
from prep_terrain_data import makeTerrainData

import numpy as np
import pylab as pl

features_train, labels_train, features_test, labels_test = makeTerrainData()



#################################################################################


########################## DECISION TREE #################################

from sklearn.tree import DecisionTreeClassifier

clf2 = DecisionTreeClassifier(min_samples_split=2)
clf2.fit(features_train, labels_train)
acc_min_samples_split_2 = clf2.score(features_test, labels_test)

clf50 = DecisionTreeClassifier(min_samples_split=50)
clf50.fit(features_train, labels_train)
acc_min_samples_split_50 = clf50.score(features_test, labels_test)


### be sure to compute the accuracy on the test set

print {"acc_min_samples_split_2":round(acc_min_samples_split_2,3),
          "acc_min_samples_split_50":round(acc_min_samples_split_50,3)}

prettyPicture(clf2, features_test, labels_test, "test2.png")

prettyPicture(clf50, features_test, labels_test, "test50.png")