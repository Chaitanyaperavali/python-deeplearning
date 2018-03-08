import pandas
import matplotlib.pyplot as pl
from sklearn.cluster import KMeans

variables = pandas.read_csv('sample_stocks.csv')
Y = variables[['returns']]
X = variables[['dividendyield']]

kmeans = []
score = []

x=50
for i in range(1, x):
    kmeans.append(KMeans(i))

for i in range(len(kmeans)):
    score.append(kmeans[i].fit(Y).score(Y))

pl.plot(range(1,x), score)
pl.xlabel('Number of Clusters')
pl.ylabel('Score')
pl.title('Elbow Curve')
pl.show()