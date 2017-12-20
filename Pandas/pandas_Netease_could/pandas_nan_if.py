import numpy as np
import pandas as pd

dates=pd.date_range('20170802',periods=6)
df=pd.DataFrame(np.arange(24).reshape((6,4)),index=dates,columns=['A','B','C','D'])
df.iloc[0,1]=np.nan
df.iloc[1,2]=np.nan
print(df)
print(df.dropna(axis=0,how='any'))#按行丢弃包含nan的的行数据  how={'any','all'}
#all,行列全部nan,则丢弃，否则不丢弃

#把nan的矩阵填入为0，
print(df.fillna(value=0))

#检查数据是否有nan数据,是nan的数据显示为ture,否则显示false
print(df.isnull())

#整个数据只要有一个null,即返回True,则显示True
print(np.any(df.isnull())==True)
