import os

os.environ['OPENBLAS_NUM_THREADS'] = '1'

#from dataset_script import dataset
from zad2_dataset_rf import *
from sklearn.tree import DecisionTreeClassifier

if __name__ == '__main__':
    p=int(input())
    train_data=dataset[:int(len(dataset)*p/100)]
    test_datset=dataset[int(len(dataset)*p/100):]
    train_x=[row[:-1] for row in train_data]
    train_y=[row[-1] for row in train_data]
    test_y=[row[-1] for row in test_datset]
    test_x=[row[:-1] for row in test_datset]

    c=input()
    l=int(input())

    clf = DecisionTreeClassifier(criterion=c, max_leaf_nodes=l, random_state=0)
    clf.fit(train_x, train_y)

    print("Tochnost so originalniot klasifikator:", clf.score(test_x, test_y))

    modeli=[]
    for cls in clf.classes_:
        model = DecisionTreeClassifier(criterion=c, max_leaf_nodes=l, random_state=0)
        model.fit(train_x, [1 if lab == cls else 0 for lab in train_y])
        modeli.append((cls,model))

    acc_count=0

    for r, l in zip(test_x, test_y):
        prediction=True
        for c, model in modeli:
            pred=model.predict([r])[0]
            if l == c:
                if pred != 1:
                    prediction=False
                    break
            else:
                if pred != 0:
                    prediction=False
                    break

        if prediction:
            acc_count+=1

    print("Tochnost so kolekcija od klasifikatori:", acc_count/len(test_datset))
