import numpy as np
import  pandas as pd

dates=pd.date_range('20170802',periods=6)
df=pd.DataFrame(np.arange(24).reshape((6,4)),index=dates,columns=['A','B','C','D'])

df.iloc[2,2]=11111#更改数据值
print(df)


df.loc['20170802','B']=2222
print(df)


df.A[df.A>4]=0#判断，更改
print(df)

df['F']=np.nan#添加一列

df['E']=pd.Series([1,2,3,4,5,6],index=pd.date_range('20170802',periods=6))
print(df)
