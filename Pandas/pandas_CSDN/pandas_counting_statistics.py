import pandas as pd#导入pandas模块
#读取本地csv数据，含有中文encoding为‘gbk’，默认为utf-8
pd_csv=pd.read_csv('../test_DataFrame.csv',encoding='gbk')
print(pd_csv)

#查看数据前三行，检查数据是否正确
pd_csv_head_3=pd_csv.head(3)#head，查看前三行0,1,2
print(pd_csv_head_3)
pd_csv_3=pd_csv[:3]#[]查看前三行,0,1,2
print("pd_csv_3",pd_csv_3)
pd_csv_iloc_3=pd_csv.iloc[:3,:]#iloc,查看数据前三行,0,1,2
print("pd_csv_iloc_3",pd_csv_iloc_3)
pd_csv_ix_3=pd_csv.ix[:3,:]#ix,查看数据前四行,0,1,2,3
print("pd_csv_ix_3",pd_csv_ix_3)

#选择其中的数据
#选选择语文的成绩
pd_csv_chinese=pd_csv['语文'][:3]
print(pd_csv_chinese)

#对数据进行计数统计
counts=pd_csv['语文'].value_counts()
print(counts)

#绘制图片
plt=counts.plot(kind='bar').get_figure()
plt.savefig('../plot.png')

#筛选计数统计
import pandas as pd
#读取数据
pd_csv=pd.read_csv('../test_DataFrame.csv',encoding='gbk')
print(pd_csv)
#选择总成绩大于400的学生
pd_400=pd_csv[pd_csv['总成绩']>400]
print(pd_400)

#打印总成绩前三的数据信息
pd_400_sort_values=pd_400.sort_values(by='总成绩')
pd_tail_3=pd_400_sort_values.tail(3)
print(pd_tail_3)

#根据得到的总成绩数据，进行关于数学成绩的计数统计
pd_tail_counts=pd_tail_3['数学'].value_counts()
print(pd_tail_counts)

#根据数学成绩，统计总体数据的数学成绩计数
pd_math_value=pd_csv['数学'].value_counts()
print(pd_math_value)

#数据分组
#groupby()
#引入模块，创建DataFrame
import pandas as pd
import numpy as np
df=pd.DataFrame({
    'A':['foo','bar','foo','bar','foo','bar','foo','foo',],
    'B':['one','one','two','three','two','two','one','three'],
    'C':np.random.randn(8),
    'D':np.random.randn(8),
})
#print(df)

#进行分组，
#依据A列进行分组，groupby
df_groupby_A=df.groupby('A')
print(df_groupby_A)
#d打印每一组的第一行数据
print(df_groupby_A.first())

#以两列以上进行分组，groupby参数为列表
df_groupby_AB=df.groupby(['A','B'])
#打印出来每一组的最后一行的数据
print(df_groupby_AB.last())

#将分组列，根据columns，字符与数组对应分组，
def get_type(letter):
    if letter.lower() in 'abem':
        return 'vowel'
    else:
        return 'consonant'
print(df)
df_get_type=df.groupby(get_type,axis=1)
#取得分组的第一组数据
df_get_type_first=df_get_type.first()
print("df_get_type_first\n",df_get_type_first)
#取得分组的最后一组数据
print("df_get_type_last\n",df_get_type.last())



