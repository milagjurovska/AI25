import os

from sklearn.tree import DecisionTreeClassifier

os.environ['OPENBLAS_NUM_THREADS'] = '1'

#from dataset_script import dataset
from zad2_dataset_rf import *

if __name__ == '__main__':
    p=int(input())
    c=input().strip()
    l=int(input())

    train_data=dataset[:int(len(dataset)*p/100)]
    test_data=dataset[int(len(dataset)*p/100):]

    X_train, y_train = [row[:-1] for row in train_data], [row[-1] for row in train_data]
    X_test, y_test = [row[:-1] for row in test_data], [row[-1] for row in test_data]

    clf1=DecisionTreeClassifier(criterion=c, max_leaf_nodes=l, random_state=0)
    clf1.fit(X_train, y_train)
    print("Tochnost so originalniot klasifikator:", clf1.score(X_test, y_test))

    classificators = []
    for klasa in ["Perch", "Roach", "Bream"]:
        clf = DecisionTreeClassifier(criterion=c, max_leaf_nodes=l, random_state=0)
        clf.fit(X_train, [1 if label == klasa else 0 for label in y_train])
        classificators.append(clf)

        
