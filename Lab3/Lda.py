import numpy as np
from sklearn import cross_validation
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

# LDA model
lda = LinearDiscriminantAnalysis()

# Load wine data from input file
d = np.loadtxt('wineinput.data',delimiter=',',skiprows=1)

# split input data into input and response
x = d[:,1:]
y = d[:,0]

# Perform cross validation on given data
k_fold = cross_validation.KFold(len(x), 3, shuffle=True)
print('LDA Results: ')
for (train, test) in k_fold:
    lda.fit(x[train], y[train])
    # computes accuracy of the system
    outVal = lda.score(x[test], y[test])

# print overall output
print('Score: ' + str(outVal))