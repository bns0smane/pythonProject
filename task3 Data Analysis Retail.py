import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data= pd.read_csv('SampleSuperstore.csv')
#checking for null variables
print(data.isnull().sum())  # no null variables
print(data.shape)

#dropping columns whish dont affect
data=data.drop(['Ship Mode','Postal Code','Country'],axis=1)
print(data.duplicated().sum())
data=data.drop_duplicates()
print(data.keys())
x=data['Profit']
y=data['State']
#SP=State & Profit

SP=data.groupby('State')['Profit'].sum()
SP = SP.to_frame().reset_index()
SP=SP.sort_values(by='Profit', ascending=True)
sns.barplot(x=SP['State'],y=SP['Profit'])
plt.ylabel("Profit")
plt.xlabel("State")
plt.xticks(rotation = 90)

#RPS=Region & Profit & Sales
RPS=data.groupby('Region')['Profit','Sales'].sum()
RPS.plot(kind='bar',rot=45)

#CPS=Category & Profit & Sales
CPS=data.groupby('Category')['Profit','Sales'].sum()
CPS.plot(kind='bar',rot=45)

#SCPS=Sub-Category & Profit & Sales
SCPS=data.groupby('Sub-Category')['Profit','Sales'].sum()
SCPS=SCPS.sort_values(by='Profit', ascending=True)
SCPS.plot(kind='bar',rot=45)

#SPS=State & Profit & Sales
SPS=data.groupby('State')['Profit','Sales'].sum()
SPS=SPS.sort_values(by='Profit', ascending=True)
SCPS.plot(kind='bar',rot=45)

#SPS=Segment & Profit & Sales
SGPS=data.groupby('Segment')['Profit','Sales'].sum()
SGPS=SGPS.sort_values(by='Profit', ascending=True)
SGPS.plot(kind='bar',rot=45)


#SS=State Sales
SS=data.groupby('State')['Sales'].sum()
SS = SS.to_frame().reset_index()
SS=SS.sort_values(by='Sales', ascending=True)
sns.barplot(x=SS['State'],y=SS['Sales'])
plt.ylabel("Sales")
plt.xlabel("State")
plt.xticks(rotation = 90)

plt.show()
