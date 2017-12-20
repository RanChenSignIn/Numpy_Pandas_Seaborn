import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dates=pd.date_range('20170802',periods=6)#生成以20170802日期为起点的，6个日期
data_np=np.random.randn(6,4)
data_ones=np.ones(10,dtype=int).reshape(5,2)
print("data_ones:",data_ones)
data_array=np.random.randint(1,15,14)#生成（1,15），之间14个数，随机生成，可重复
print("data_array:",data_array)
data_arange=np.arange(10,100,2)#生成（10，100），步长2，的数据
print("data_arange:",data_arange)
data_linespace=np.linspace(10,100,2)#生成（10,100），2个数据
print("data_linspace:",data_linespace)




df=pd.DataFrame(data_np,index=dates,columns=['A','B','C','D'])
df_A=df['A']
print("\ndf_A:\n",df_A)
#plt.plot(data_np[:,0])
#plt.show()

df_row03=df[0:3]
print(df_row03)

df_46=df['20170804':'20170806']
df_46_mean=np.mean(df_46,axis=1)#行均值
print(df_46_mean)
print("df_46\n",df_46)

df_iloc=df.iloc[:3]
print(df_iloc)

df_iloc_32=df.iloc[:3,:2]
print(df_iloc_32)

df_12402=df.iloc[[1,2,4],[0,2]]
print(df_12402)

df_ac=df.ix[:3,['A','C']]
print(df_ac)

print(df[df.A>0])#判断，同时满足的打印
