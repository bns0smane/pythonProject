import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import numpy as np

#read data from csv file
data=pd.read_csv('https://raw.githubusercontent.com/AdiPersonalWorks/Random/master/student_scores%20-%20student_scores.csv')

#plot scatter plot
plt.scatter(data['Hours'],data['Scores'])

#reshape data array
X = data.iloc[:, :-1].values
Y = data.iloc[:, 1].values
print(Y)

#train/test split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y,
                            test_size=0.2, random_state=0)

#calculate prediction (regression
regressor = LinearRegression()
regressor.fit(X_train,Y_train)
Y_pred = regressor.predict(X_test)

line = regressor.coef_*X+regressor.intercept_
plt.plot(X,line,color='red')
plt.show()

# create a dict to compar the prediction!!!!'
df = pd.DataFrame({'actual':Y_test, 'predicted':Y_pred})
print(df)

#prediction hours = 9.25 !!!!!
max=[]
max.append(9.25)
max_pred=np.array(max).reshape(-1,1)
print("prediction hours = 9.25 !!!!!")
max_hour=regressor.predict(max_pred)
print('prediction is {}'.format(max_hour))

