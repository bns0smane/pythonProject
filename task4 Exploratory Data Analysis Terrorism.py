import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import plotly.express as px
import plotly.graph_objects as go
from google.colab import drive
drive.mount('/content/drive')
df =pd.read_csv("/content/drive/My Drive/globalterrorismdb_0718dist.csv", encoding='cp1252',low_memory=False)
df.head()

df['casualties'] = df.nkill + df.nwound

NAN_cols= df.isna().any()
NAN_list=df.columns[NAN_cols].to_list()
NAN_list
print(df.describe())

features = ['eventid','iyear','imonth','iday','approxdate','latitude','longitude','success',
            'doubtterr','country_txt','region_txt','provstate','city','attacktype1_txt','gname','individual',
            'targtype1_txt','weaptype1_txt','nperps','motive','nkill','nwound']
len(features)
df1 =df[features]
print(df1.head())


sns.set_theme()
plt.figure(figsize=(15,8))
sns.heatmap(data=df1.isna())


sns.set_theme()
plt.figure(figsize=(15,8))
sns.histplot(data=df1,x=df['iyear'])
plt.show()


plt.figure(figsize=(15,8))
sns.histplot(data=df1, y=df1['region_txt'])
plt.xticks(rotation=-90)


sns.set_theme()
plt.figure(figsize=(15,8))
sns.histplot(data=df1,x=df['success'])


sns.set_theme()
plt.figure(figsize=(15,8))
sns.histplot(data=df1,y=df['attacktype1_txt'])
plt.xticks(rotation=-90)


sns.set_theme()
plt.figure(figsize=(15,8))
sns.histplot(data=df1,y=df['weaptype1_txt'])
plt.xticks(rotation=-90)


sns.set_theme()
plt.figure(figsize=(15,8))
sns.histplot(data=df1,y=df['targtype1_txt'])
plt.xticks(rotation=-90)


sns.set_theme()
plt.figure(figsize=(15,8))
sns.barplot(x=df1['gname'].value_counts()[1:15].values,y=df1['gname'].value_counts()[1:15].index)
plt.xticks(rotation=-90)


df1.isna().sum()
df2 = df1[df1['region_txt']=='Middle East & North Africa']
print(df2.head())
print(df2['country_txt'].unique())


sns.set_theme()
plt.figure(figsize=(15,8))
sns.barplot(x=df2['country_txt'].value_counts()[:15].values,y=df2['country_txt'].value_counts()[:15].index)
plt.xticks(rotation=-90)


list1 = df2.sort_values(by=df2['country_txt'].value_counts())
print(df2.head())
countries = df2['country_txt'].unique()
print(countries)
print(df2.head())
df2=df2.replace(np.nan,0)
ig =px.scatter_geo(df2,animation_frame=df2.iyear,color=df2.nkill,width=900,height=650,hover_name=df2.country_txt,hover_data=[df2.nkill]
                    ,projection='natural earth',
                    lat=df2.latitude
                    ,lon=df2.longitude)
fig.show()
plt.figure(figsize=(8,8))

plt.pie(df2['success'].value_counts(),labels= ['success','faild'], autopct='%1.1f%%')
plt.show()
success=df2[df2['success']==1].value_counts().sum()
faild=df2[df2['success']==0].value_counts().sum()
print(success ,faild)
df2['iyear'].value_counts()[:10]
plt.figure(figsize=(10,10))

plt.pie(df2['targtype1_txt'].value_counts()[:10],labels= df2['targtype1_txt'].unique()[:10], autopct='%1.1f%%')
plt.show()