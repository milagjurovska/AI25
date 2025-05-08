import os
os.environ['OPENBLAS_NUM_THREADS'] = '1'
from submission_script import *
from dataset_script import dataset
from sklearn.preprocessing import OrdinalEncoder
from sklearn.naive_bayes import CategoricalNB

# Ova e primerok od podatochnoto mnozestvo, za treniranje/evaluacija koristete ja
# importiranata promenliva dataset
dataset_sample = [['C', 'S', 'O', '1', '2', '1', '1', '2', '1', '2', '0'],
                  ['D', 'S', 'O', '1', '3', '1', '1', '2', '1', '2', '0'],
                  ['C', 'S', 'O', '1', '3', '1', '1', '2', '1', '1', '0'],
                  ['D', 'S', 'O', '1', '3', '1', '1', '2', '1', '2', '0'],
                  ['D', 'A', 'O', '1', '3', '1', '1', '2', '1', '2', '0']]

if __name__ == '__main__':
    encoder=OrdinalEncoder()
    
    train_set=dataset[:int(0.75*len(dataset))]
    test_set=dataset[int(0.75*len(dataset)):]
    train_X = [row[:-1] for row in train_set]
    train_Y = [row[-1] for row in train_set]
    test_X=[row[:-1] for row in test_set]
    test_Y=[row[-1] for row in test_set]
       

    classifier = CategoricalNB()
    encoder.fit([row[:-1] for row in dataset])

    train_x_enc = encoder.transform(train_X)
    test_x_enc = encoder.transform(test_X)

    classifier.fit(train_x_enc, train_Y)

    line=input().split(" ")
    line=encoder.transform([line])

    accuracy=classifier.score(test_x_enc, test_Y)

    print(accuracy)

    pred_class=classifier.predict(line)[0]
    probs=classifier.predict_proba(line)
    print(pred_class)
    print(probs)
    
