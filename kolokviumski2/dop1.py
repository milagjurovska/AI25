import os

os.environ['OPENBLAS_NUM_THREADS'] = '1'

from dataset_script import dataset  # this will import the dataset on coderunner at courses
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import MinMaxScaler


def main():
    global dataset

    C = int(input())
    P = int(input())

    new_dataset=[]
    for row in dataset:
        new_feature = row[0] + row[10]
        new_row=[new_feature] + row[1:10] + [row[-1]]
        new_dataset.append(new_row)
        
    good_dataset=[row for row in new_dataset if row[-1]=="good"]
    bad_dataset=[row for row in new_dataset if row[-1]=="bad"]

    if C == 0:
        train_dataset = good_dataset[:int(len(good_dataset) * P / 100)] + bad_dataset[:int(len(bad_dataset) * P / 100)]
        test_dataset = good_dataset[int(len(good_dataset) * P / 100):] + bad_dataset[int(len(bad_dataset) * P / 100):]
    else:
        train_dataset = good_dataset[int(len(good_dataset) * (100-P )/ 100):] + bad_dataset[int(len(bad_dataset) * (100-P )/ 100):]
        test_dataset = good_dataset[:int(len(good_dataset) *(100-P )/ 100)] + bad_dataset[:int(len(bad_dataset) * (100-P )/ 100)]


    test_x=[row[:-1] for row in test_dataset]
    test_y=[row[-1] for row in test_dataset]
    train_x=[row[:-1] for row in train_dataset]
    train_y=[row[-1] for row in train_dataset]

    classifier1 = GaussianNB()
    classifier2 = GaussianNB()

    print("Broj na podatoci vo train se:", len(train_dataset))
    print("Broj na podatoci vo test se:", len(test_dataset))
    classifier1.fit(train_x, train_y)
    print("Tochnost so zbir na koloni:", classifier1.score(test_x, test_y))


    scaler = MinMaxScaler(feature_range=(-1,1))
    scaler.fit(train_x)

    test_x_scaled = scaler.transform(test_x)
    train_x_scaled = scaler.transform(train_x)
    classifier2.fit(train_x_scaled, train_y)
    print("Tochnost so zbir na koloni i skaliranje:", classifier2.score(test_x_scaled, test_y))


main()
