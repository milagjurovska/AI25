import os

os.environ['OPENBLAS_NUM_THREADS'] = '1'
from submission_script import *
from dataset_script import dataset
from sklearn.naive_bayes import GaussianNB

# Ova e primerok od podatochnoto mnozestvo, za treniranje/evaluacija koristete ja
# importiranata promenliva dataset
dataset_sample = [['1', '35', '12', '5', '1', '100', '0'],
                  ['1', '29', '7', '5', '1', '96', '1'],
                  ['1', '50', '8', '1', '3', '132', '0'],
                  ['1', '32', '11.75', '7', '3', '750', '0'],
                  ['1', '67', '9.25', '1', '1', '42', '0']]

if __name__ == '__main__':
    train_dataset = dataset[:int(0.85 * len(dataset))]
    test_dataset = dataset[int(0.85 * len(dataset)):]
    train_X = [[float(val) for val in row[:-1]] for row in train_dataset]
    train_Y = [int(row[-1]) for row in train_dataset]
    test_X = [[float(val) for val in row[:-1]] for row in test_dataset]
    test_Y = [int(row[-1]) for row in test_dataset]

    classifier = GaussianNB()

    classifier.fit(train_X, train_Y)
    accuracy = classifier.score(test_X, test_Y)

    print(accuracy)

    line = input().split(" ")
    line = [float(i) for i in line]
    class_pred = classifier.predict([line])[0]
    print(class_pred)
    probs = classifier.predict_proba([line])
    print(probs)
