import pandas as pd
import numpy as np

#创建数据6*4，索引默认0-5，columns为ABCD
df=pd.DataFrame(np.random.randn(6,4),columns=list('ABCD'))
print(df)

#筛选D列数据大于0的数据，并重新选择数据
df_D=df[df.D>0]
print(df_D)

#用符号实现多条件筛选，&与关系，，|或关系
#筛选数据，D大于0，同时C小于0数据
df_DC=df[(df.D>0)&(df.C<0)]
print(df_DC)

#AB列是数据，CD列是用于判断筛选的，返回要求只返回AB列数据
df_AB_CD=df[['A','B']][(df.D>0)&(df.C<0)]
print(df_AB_CD)


#条件选择，isin ,通过某一列或某一行的数据判断后，筛选整个数据
#创建一组数据
import pandas as pd#导入模块
data=[[1,2,3],[1,3,4],[2,4,3]]
df = pd.DataFrame(data,index = ['one','two','three'],columns = ['A','B','C'])
print(df)
#选取C列中数据值为3的行
mask=df['C'].isin([3])#括号中必须为列表list
print(df[mask])


#条件筛选，筛选的对象是数组，筛选的条件也是数组，
#选择C列中数据值，在alist列表里面的数据行，
# 判断有的这一行返回为True,否则返回False
alist=[1,3]
df_isin_alist=df['C'].isin(alist)
print(df_isin_alist)
#再将判断后符合条件的数据筛选出来
df_df=df[df_isin_alist]
print(df_df)