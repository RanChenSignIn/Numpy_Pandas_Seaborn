import numpy as np
import pandas as pd

s=pd.Series([1,3,6,np.nan,44,1])
#一维
#print(s)

dates=pd.date_range('20170802',periods=6)#生成日期索引序列号
print(dates)

row_col=np.random.randn(6,4)
df=pd.DataFrame(row_col,index=dates,columns=['a','b','c','d'])
print(df)

df2=pd.DataFrame({
    'A':1.,
    'B':pd.Timestamp('20130102'),
    'C':pd.Series(1,index=list(range(4)),dtype='float32'),
    'D':np.array([3]*4,dtype='int32'),
    'E':pd.Categorical(["test","train","test","train"]),
    'F':'foo'
    })
print(df2)

print(df2.dtypes)#查看每一列的类型
df2.sort_index(axis=1,ascending=False)#axis=0.根据列排序，axis=1,根据行排序


df_E=df2.sort_values(by='E')#根据E值排序
print(df_E)

print(df2.describe())
