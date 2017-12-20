import pandas as pd
import numpy as np

#DataFrame 选择数据
dates=pd.date_range('20170808',periods=6)
df=pd.DataFrame(np.random.randn(6,4),index=dates,columns=list('ABCD'))
print(df)

#选择数据A列，并对其操作
df_A=df['A']#取A列数据
print(df_A)#打印查看

#对数据进行切片操作，行数据切片操作
df_1_3=df[1:3]#取第一行到第三行，即取第一行和第二行
print(df_1_3)

#df，切片对列操作，将报错
#print(df['A':'C'])#错误操作
print(df.ix[:,:3])
print(df.iloc[:,:3])

#使用行标签输出指定行，或指定行范围
#标签指定，即指定到第几行，封闭式索引，不像序号位置的半封闭索引
df_rownum=df['20170809':'20170812']
print(df_rownum)

#df.loc选择数据，以dates作为索引
print(df.loc[dates[0]])#选择日期第0行的数据，

#df.loc选择多列数据的方法
print(df.loc[:,['A','C','D']])#同时选择A,C,D

#选择数据中一部分数据，交叉区域
#选择8,9,10号的，A，B类，数据
df_complex=df.loc['20170808':'20170810',['A','B']]
print(df_complex)

#只选择数据中的一个数据，进行单独查看，可以指定行和列
df_row_col=df.loc[dates[0],'A']#通过指定dates日期索引，和指定列选择数据
print(df_row_col)

#DataFrame,切片操作 iloc,如同操作array数组一样
#创建6*4的数据，横向索引为日期6日，纵向列为ABCD
dates=pd.date_range('20170808',periods=6)
df=pd.DataFrame(np.random.randn(6,4),index=dates,columns=list('ABCD'))
print(df)

#提取数据，iloc,
#提取第四行数据
df_iloc_3=df.iloc[3]#单个数字，提取行
print(df_iloc_3)

#查看上面返回数据类型
type_df=type(df_iloc_3)
print(type_df)

#双位置提取数据，类同array切片操作，iloc
#iloc,提取[3:5,0:2]，即第3,4行，第0，1列的交叉数据
df_iloc_two=df.iloc[3:5,0:2]
print(df_iloc_two)

#iloc提取不连续行和列的数据
#提取第1,2,4行，第0,2列的交叉数据
df_iloc_interrupt=df.iloc[[1,2,4],[0,2]]
print(df_iloc_interrupt)

#iloc提取，某一行，或者某几行的数据，保证所有列都在
#提取第1,2列的所有数据
df_iloc_1_3=df.iloc[1:3,:]
print(df_iloc_1_3)
#同理，取某列，保证所有行
df_iloc_13=df.iloc[:,[0,2]]
print(df_iloc_13)

#提取某一个数值，
#提取第2行，第2列的数据
df_iloc_22=df.iloc[2,2]
print(df_iloc_22)

#提取数据，ix，类同iloc
#提取第0列的所有数据，的前五行
df_head=df.ix[:,0].head()
print(df_head)

#提取单个数据，高效率
df_iat=df.iat[1,1]
print(df_iat)