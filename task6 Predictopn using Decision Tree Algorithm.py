from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pandas as pd
import matplotlib.pyplot as plt


data=pd.read_csv('Iris.csv')
print(data.head())

X=data.iloc[:,[1,2,3,4]]
Y=data['Species']

X_train , X_test , Y_train , Y_test = train_test_split(X,Y,test_size=0.2,stratify=Y,random_state=1)
dt = DecisionTreeClassifier(criterion='gini',random_state=1)
dt.fit(X_train,Y_train)
Y_pred = dt.predict(X_test)
accuracy_score(Y_test,Y_pred)
plot_tree(dt, rounded=True, filled=True)
plt.show()
