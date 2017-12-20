import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

"""
url = 'http://s3.amazonaws.com/assets.datacamp.com/course/dasi/present.txt'
present = pd.read_table(url, sep=' ')
zz=present.shape
print(zz)
#present.to_csv('..\\txt_csv.csv')#csv文件保存
"""

#pandas
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.style.use('ggplot')

path='..\\txt_csv.csv'
present=pd.read_csv(path)#读取csv文件
print(present)
print(present.columns)
present_year=present.set_index('year')#设置索引，以年份
#直接绘图
#Series的plot的绘图方法
"""
present_year['boys'].plot()#只绘制男生
plt.legend(loc='best')
plt.show()
"""


"""
present_year.plot()#男女都绘制
present_year.girls.plot(color='g')#指定颜色
present_year.boys.plot(color='b')
plt.legend(loc='best')#自动选择最合适的location of legend
plt.show()
"""

"""
present_year[:10].plot(kind='bar')#选取前10年的数据绘制，bar图形 竖直的
present_year[:10].plot(kind='barh',color=("#FF4562",'g'))#颜色，kind  水平的
plt.show()
"""



#DataFrame生成数据，匹配关键字
"""
df2 = pd.DataFrame(np.random.rand(10, 4), columns=['a', 'b', 'c', 'd'])
df2.plot.bar()#绘制DataFrame多组对比性数据，bar
plt.show()
"""


#读取本地数据，并利用DataFrame对数据格式，关键字，分组处理，可视化数据
"""
path='..\\txt_csv.csv'
present=pd.read_csv(path)
df2=pd.DataFrame(present,columns=['boys', 'girls'])
df2.plot.bar()
#如果你需要累积的柱状图，则只需要指定stacked=True。
df2.plot.barh(stacked=True)
plt.show()
"""


#Box plots
"""
#调用格式，Series.plot.box(),and DataFrame.plot.box(),and DataFrame.boxplot()
#生成数据  10*5的DataFrame数据，关键字ABCDE,
df=pd.DataFrame(np.random.rand(10,5),columns=['A','B','C','D','E'])
#df.plot.box()#内部未填充的箱线图，
color = dict(boxes='DarkGreen', whiskers='DarkOrange',
             medians='DarkBlue', caps='Gray')#设定box每个部分的具体颜色
#df.plot.box(color=color,sym='r+')
df.plot.box(vert=False, positions=[1, 4, 5, 6, 8])#设置box水平或垂直，以及position
plt.show()
"""

#Area Plot
"""
#生成10*4数据，DataFrame数据，columns为abcd
df=pd.DataFrame(np.random.rand(10,4),columns=['a','b','c','d'])
# df.plot.area()#绘制面积图
df.plot.area(stacked=False)#绘制非堆积图，the value of area锐化0.5
plt.show()
"""

#Scatter Plot
"""
#scatter绘制需要同时columns of x and y axis,or by x and y keywords each
df=pd.DataFrame(np.random.rand(50,4),columns=['a','b','c','d'])
# df.plot.scatter(x='a',y='b')#绘制

#绘制两组数据，分别制定颜色，label,
ax=df.plot.scatter(x='a',y='b',color='DarkBlue',label='Group 1')
# df.plot.scatter(x='c',y='d',color='DarkGreen',label='Group 2',ax=ax)

#c设定scatter中点颜色，同时添加色柱
df.plot.scatter(x='a',y='b',c='c',s=50)

#通过数据本身来设定scatter的色点大小，直接调用数据即可
#df.plot.scatter(x='a', y='b', s=df['c']*200);
plt.show()
"""

#plotting with Error Bars
"""
#Generate the data
#多重索引的关键字
ix3=pd.MultiIndex.from_arrays([['a','a','a','a','b','b','b','b'],
                               ['foo','foo','bar','bar','foo','foo','bar','bar']],
                              names=['letter','word'])
df3=pd.DataFrame({'data1':[3,2,4,3,2,4,3,2],
                  'data2':[6,5,7,5,4,5,6,5]},
                 index=ix3)
print(df3)
#通过索引index分组，分别求出mean and standard deviations of each group
gp3=df3.groupby(level=('letter','word'))#分组依据
means=gp3.mean()#求均值，
errors=gp3.std()#求标准偏差、标准差

# fig,ax=plt.subplots()#等价于下面两句
fig=plt.figure()
ax=fig.add_subplot()
means.plot.bar(yerr=errors,ax=ax)#自动添加legend,
plt.show()

#colormap,and color bar
dd=pd.DataFrame(np.random.randn(10,10)).applymap(abs)
dd=dd.cumsum()#对dd累加，
plt.figure()
dd.plot.bar(colormap='Greens')#颜色bar，同一种颜色不同度
plt.show()
"""

price=pd.Series(np.random.randn(150).cumsum(),
                index=pd.date_range('20170806',periods=150,freq='B'))
ma=price.rolling(20).mean()
mstd=price.rolling(20).std()
plt.figure()
plt.plot(price.index,price,'k')
plt.plot(ma.index,ma,'b')
plt.fill_between(mstd.index,ma-2*mstd,ma+2*mstd,color='b',alpha=0.2)
plt.show()