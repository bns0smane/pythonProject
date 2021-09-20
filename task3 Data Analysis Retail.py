import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
plt.style.use("seaborn")

data= pd.read_csv('SampleSuperstore.csv')
#checking for null variables
print(data.isnull().sum())  # no null variables
print(data.shape)

#dropping columns whish dont affect
data=data.drop(['Ship Mode','Postal Code','Country'],axis=1)
print(data.duplicated().sum())
data=data.drop_duplicates()

x=data['Profit']
y=data['State']
state=data.groupby('State')['Profit'].sum()
state = state.to_frame().reset_index()
sns.barplot(x=state['State'],y=state['Profit'])
plt.ylabel("Profit")
plt.xlabel("State")
plt.xticks(rotation = 75)
plt.show()

