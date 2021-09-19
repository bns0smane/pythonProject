import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import numpy as np

iris = pd.read_csv('Iris.csv')
print(iris.shape)

samples=iris.iloc[:,[1,2,3,4]].values
print(samples)
optimum_set = []
for k in range(1,9):
    model = KMeans(n_clusters=k )
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

model_opt=KMeans(n_clusters=3)
model_opt.fit(samples)
labels=model_opt.predict()

