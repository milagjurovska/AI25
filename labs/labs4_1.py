import os

os.environ['OPENBLAS_NUM_THREADS'] = '1'
# from submission_script import *
# from dataset_script import dataset
from zad1_dataset import *
from sklearn.preprocessing import OrdinalEncoder
from sklearn.tree import DecisionTreeClassifier
# Ova e primerok od podatochnoto mnozestvo, za treniranje/evaluacija koristete ja
# importiranata promenliva dataset
dataset_sample = [['C', 'S', 'O', '1', '2', '1', '1', '2', '1', '2', '0'],
                  ['D', 'S', 'O', '1', '3', '1', '1', '2', '1', '2', '0'],
                  ['C', 'S', 'O', '1', '3', '1', '1', '2', '1', '1', '0'],
                  ['D', 'S', 'O', '1', '3', '1', '1', '2', '1', '2', '0'],
                  ['D', 'A', 'O', '1', '3', '1', '1', '2', '1', '2', '0']]

if __name__ == '__main__':
    encoder= OrdinalEncoder()
    encoder.fit([row[:-1] for row in dataset])
    procent=int(input())
    criterion=input().strip()

    train_data=dataset[int((1-procent/100)*len(dataset)):]
    test_data=dataset[:int((1-procent/100)*len(dataset))]
    X_train=[row[:-1] for row in train_data]
    y_train=[row[-1] for row in train_data]
    X_test = [row[:-1] for row in test_data]
    y_test = [row[-1] for row in test_data]

    X_train=encoder.transform(X_train)
    X_test=encoder.transform(X_test)

    classifier = DecisionTreeClassifier(criterion=criterion, random_state=0)
    classifier.fit(X_train,y_train)

    depth=classifier.get_depth()
    print('Depth:',depth)

    leaves=classifier.get_n_leaves()
    print('Number of leaves:',leaves)

    accuracy=classifier.score(X_test,y_test)
    print('Accuracy:', accuracy)

    features = list(classifier.feature_importances_)
    most_important=features.index(max(features))
    least_important=features.index(min(features))

    print('Most important feature:', most_important)
    print('Least important feature:', least_important)

# Na kraj potrebno e da napravite submit na podatochnoto mnozestvo,
# klasifikatorot i encoderot so povik na slednite funkcii

# submit na trenirachkoto mnozestvo
submit_train_data(X_train, y_train)

# submit na testirachkoto mnozestvo
submit_test_data(X_test, y_test)

# submit na klasifikatorot
submit_classifier(classifier)

# submit na encoderot
submit_encoder(encoder)
