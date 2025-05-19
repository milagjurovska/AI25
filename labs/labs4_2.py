import os

os.environ['OPENBLAS_NUM_THREADS'] = '1'
# from submission_script import *
# from dataset_script import dataset
from zad2_dataset_rf import *
from sklearn.ensemble import RandomForestClassifier

# Ova e primerok od podatochnoto mnozestvo, za treniranje/evaluacija koristete ja
# importiranata promenliva dataset
dataset_sample = [[180.0, 23.6, 25.2, 27.9, 25.4, 14.0, 'Roach'],
                  [12.2, 11.5, 12.2, 13.4, 15.6, 10.4, 'Smelt'],
                  [135.0, 20.0, 22.0, 23.5, 25.0, 15.0, 'Perch'],
                  [1600.0, 56.0, 60.0, 64.0, 15.0, 9.6, 'Pike'],
                  [120.0, 20.0, 22.0, 23.5, 26.0, 14.5, 'Perch']]

if __name__ == '__main__':
    # Vashiot kod tuka
    col_index=int(input())
    n_trees=int(input())
    criterion=input().strip()
    line=input().split(" ")
    line=[float(r) for r in line]
    line = line[:col_index] + line[col_index + 1:]

    new_dataset=[row[:col_index] + row[col_index+1:] for row in dataset]

    train_data=new_dataset[:int(0.85*len(new_dataset))]
    test_data=new_dataset[int(0.85*len(new_dataset)):]
    train_X=[row[:-1] for row in train_data]
    train_Y=[row[-1] for row in train_data]
    test_X=[row[:-1] for row in test_data]
    test_Y=[row[-1] for row in test_data]

    classifier = RandomForestClassifier(n_estimators=n_trees, criterion=criterion, random_state=0)
    classifier.fit(train_X, train_Y)

    accuracy = classifier.score(test_X, test_Y)
    print("Accuracy:", accuracy)
    y_pred = classifier.predict([line])[-1]
    print(y_pred)
    print(classifier.predict_proba([line])[0])

# Na kraj potrebno e da napravite submit na podatochnoto mnozestvo
# i klasifikatorot so povik na slednite funkcii

# submit na trenirachkoto mnozestvo
submit_train_data(train_X, train_Y)

# submit na testirachkoto mnozestvo
submit_test_data(test_X, test_Y)

# submit na klasifikatorot
submit_classifier(classifier)
