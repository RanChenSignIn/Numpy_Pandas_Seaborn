import pandas as pd
import numpy as np

#concatenating  合并
df1=pd.DataFrame(np.ones((3,4))*0,columns=['a','b','c','d'])
df2=pd.DataFrame(np.ones((3,4))*1,columns=['a','b','c','d'])
df3=pd.DataFrame(np.ones((3,4))*2,columns=['a','b','c','d'])#同一个columns

#上下合并
res=pd.concat([df1,df2,df3],axis=0,ignore_index=True)#重新排序，index
print(res)

#join,['inner','outer']
df1=pd.DataFrame(np.ones((3,4))*0,columns=['a','b','c','d'],index=[1,2,3])
df2=pd.DataFrame(np.ones((3,4))*1,columns=['b','c','d','e'],index=[2,3,4])
res=pd.concat([df1,df2],join='inner',ignore_index=True)#把columns相同的部分合并，舍弃非重合的
print(res)

#concat,索引合并
res=pd.concat([df1,df2],axis=1,join_axes=[df1.index])
#按照df1的index索引合并，没有填充，另外舍弃4
print(res)

#append
df1=pd.DataFrame(np.ones((3,4))*0,columns=['a','b','c','d'])
df2=pd.DataFrame(np.ones((3,4))*1,columns=['a','b','c','d'])
df3=pd.DataFrame(np.ones((3,4))*1,columns=['b','c','d','e'],index=[2,3,4])#同一个columns
res=df1.append(df2,ignore_index=True)#把df2加在df1后面
res=df1.append([df2,df3],ignore_index=True)#两个依次加在后面，列向

s1=pd.Series([1,2,3,4],index=['a','b','c','d'])
res=df1.append(s1,ignore_index=True)
print(res)



