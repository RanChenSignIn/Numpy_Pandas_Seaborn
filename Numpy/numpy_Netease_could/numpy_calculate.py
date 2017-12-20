import numpy as np
a=np.array([10,20,30,40])#四个元素
b=np.arange(4)#0-3，四个元素
print(a,b)#a，b一列输出
c=a-b#减法，加法类同
print(c)
c=c**2#2次方，几次方，双星号
print(c)

#三角函数运算
c=10*np.sin(a)#c中的每一个值对应的正弦值，对a求正弦值
print(c)

#判断大于或小于一些值，并输出对应的True,False
print(b)
print(b<3)#返回true false 小于
print(b==3)#等于

#二维矩阵 运算
a=np.array([[1,2],
            [2,3]])
b=np.arange(4).reshape((2,2))
print(a)
print(b)

c=a*b#对应数据相乘，同维度矩阵，逐个相乘
c_dot=np.dot(a,b)#矩阵乘法，行列相乘，dot
c_dot_2=a.dot(b)#同上
print(c)
print(c_dot)
print(c_dot_2)

a=np.random.random((2,4))#随机生成0-1数据，两行四列
print(a)
print(np.sum(a))#求整个array的和
print(np.min(a))#整个array最小值
a_max=a.max()#求最大值
a_max_col=a.max(axis=0)#每一列的最大值
a_np_max=np.max(a)
print('a_max',a_max)
print('a_np_max:',a_np_max)#整个array的最大值

print('每列的和：',np.sum(a,axis=0))#axis=0,求列；axis=1，求行
print('每行最小值：',np.min(a,axis=1))#求array每行的最小值,axis=0,求列；axis=1，求行



