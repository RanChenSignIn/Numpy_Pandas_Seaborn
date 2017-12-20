import numpy as np
import pandas as pd

#创建时间索引
dates=pd.date_range('20170808',periods=6)#日期起点为20170808，天数6天，即到20170813
print(dates)

#创建6*4的数据,横向索引为日期6日，纵向列为ABCD
df=pd.DataFrame(np.random.randn(6,4),index=dates,columns=list('ABCD'))
print(df)

#创建指定列名A的数据框，索引是自动创建的整数
df2=pd.DataFrame({'A':np.random.randn(6)})
print(df2)

#字典创建,同一固定日期，多个相同或不同的数据
df2=pd.DataFrame({'A':pd.Timestamp('20170808'),
                  'B':pd.Series(1)})
print(df2)

#使用dtype查看各行数据格式
print(df)
print(df.dtypes)
#查看各列数据columns,关键字
print(df.columns)

#查看数据所有
print(df)

#使用head查看数据前几行（默认是前五行），可指定前几行head（3）
df_head_default=df.head()#默认前五行
df_head_three=df.head(3)#指定前三行
print(df_head_default)
print(df_head_three)

#使用tail查看数据后几行数据（默认是前五行），可指定后几行tail（3）
df_tail_default=df.tail()#默认后五行
print(df_tail_default)
df_tail_three=df.tail(3)#指定后三行
print(df_tail_three)

#查看数据的索引，即行索引,同时查看索引格式
df_index=df.index
print(df_index)

#查看数据的列名，即列关键字
df_columns=df.columns
print(df_columns)

#只查看数据值，不查看数据索引及columns
df_values=df.values
print(df_values)

#查看对数据统计性描述，describe
df_describes=df.describe()#此处添加括号
print(df_describes)

#使用type查看输出的描述性统计是什么样的数据类型
type_df_describe=type(df.describe())
print(type_df_describe)

#使用转置T，进行行列转换
df_T=df.T
print(df_T)

#对数据进行重排，sort_values,可指定根据哪一列数据进行排序,by，从上往下，从小到大
print(df)
df_sort_values=df.sort_values(by='C')
print(df_sort_values)