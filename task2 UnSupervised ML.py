import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

iris = pd.read_csv('Iris.csv')
print(iris.shape)

samples=iris.iloc[:,[1,2,3,4]].values
print(samples)
optimum_set = []
for k in range(1,9):
    model = KMeans(n_clusters=k)
    model.fit(samples)
    optimum_set.append(model.inertia_)
# print(optimum_set)
ks=range(1,9)
plt.plot(ks, optimum_set, '-o')
plt.xlabel('number of clusters, k')
plt.ylabel('inertia')
plt.xticks(ks)
plt.show()
print(optimum_set)

kmeans = KMeans(n_clusters = 3, init = 'k-means++', max_iter = 300, n_init = 10, random_state =0)
y_kmeans = kmeans.fit_predict(samples)

plt.scatter(samples[y_kmeans == 0, 0], samples[y_kmeans == 0, 1],
            s = 100, c = 'red', label = 'Iris-setosa')
plt.scatter(samples[y_kmeans == 1, 0], samples[y_kmeans == 1, 1],
            s = 100, c = 'blue', label = 'Iris-versicolour')
plt.scatter(samples[y_kmeans == 2, 0], samples[y_kmeans == 2, 1],
            s = 100, c = 'green', label = 'Iris-virginica')

plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:,1],
            s = 100, c = 'black', label = 'Centroids')
plt.legend()
plt.show()