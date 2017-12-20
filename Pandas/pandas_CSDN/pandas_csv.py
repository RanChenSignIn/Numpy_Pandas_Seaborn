import pandas as pd
import numpy as np
path='..\\test_data.csv'#纯数据，没有header
#读取csv文件，参数header默认第一行，此处设定header为None
df=pd.read_csv(path, header=None)


print(df.head())#打印头五行0,1,2,3,4，
# print(df)
print(df.describe())

from pandas import Series, DataFrame
#X, y = df.values[:, 2:], df.values[:, 1]
X, y = df.loc[:, 2:].values, df.loc[:, 1].values
# print(X)
# print(y)

#各个列的数据类型
print(df.dtypes)
print(df.columns)
path='..\\test_DataFrame.csv'#纯数据，没有header
df=pd.read_csv(path)
print(df.columns)
df_data=df.data#数据类型转变为Series

df_num_data=df[['num', 'data']]#数据类型还是dataframe

## 此时 df 本身并未发生任何改变；
df_2=df['data']*100
df_assign=df.assign(df2=df_2)#将data数据乘以100，再添加到新的列数，key为df2
print('df_assign:',df_assign)
print(df)

#接收 lambda 型函数对象，
df_3=df['data']*1000
df_lambda=df.assign(data_3=lambda i: df_3)
print(df_lambda)
print(df)


url = 'http://s3.amazonaws.com/assets.datacamp.com/course/dasi/present.txt'
present = pd.read_table(url, sep=' ')
zz=present.shape
print(zz)
present.to_csv('..\\txt_csv.csv')#csv文件保存

#获取当前工作目录，os.getcwd()
import os
print(os.getcwd())#获取当前工作目录地址

