import numpy as np
from sklearn.svm import SVC
from sklearn import model_selection

def svm(kernalValue):
    # SVM model with kernal type passed as input
    svm = SVC(kernel=kernalValue)

    # Load wine data from input file
    d = np.loadtxt('wineinput.data', delimiter=',', skiprows=1)

    # split input data into input and response
    x = d[:, 1:]
    y = d[:, 0]

    # Perform cross validation on given data
    k_fold = model_selection.KFold(5, shuffle=True)
    print('SVM Results using '+kernalValue+' as kernal type : ')
    for (train, test) in k_fold.split(x):
        svm.fit(x[train], y[train])
        # computes accuracy of the system
        outVal = svm.score(x[test], y[test])

    # print overall output
    print('Score: ' + str(outVal))

def runSVM():

    # SVM with linear kernal
    svm('linear')

    # SVM with RBF kernal
    svm('rbf')

runSVM()