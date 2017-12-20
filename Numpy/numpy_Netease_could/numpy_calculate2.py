import numpy as np
A=np.arange(2,14).reshape((3,4))#arange,生成序列数

print(A)
print(np.argmin(A))#索引array最小值，打印对应的索引
print(np.argmax(A))#索引array最大值，打印对应的索引

print(np.mean(A,axis=0))#平均值,axis=0,每一列均值
print(A.mean(axis=0))
print(np.average(A))#average只用这种
print(np.median(A))#中位数

print(np.cumsum(A))#累加，size与A相同，
print(np.cumsum(A,axis=1))#每一行累加，

#互差,默认同一行中后一个减去前一个的差，若axis=0，则是同一列中下面的减去上面的差
print(np.diff(A))

#输出非零，索引，print后是矩阵坐标，前一个array输出的是行数，后一个array是输出的列数
print(np.nonzero(A))

print(np.sort(A))#逐行从小到大的排序

print(A.T)#矩阵翻转
print(np.transpose(A))#同上

print((A.T).dot(A))#矩阵转置乘以自身，非方阵时
print('转置相乘',np.dot(A.T,A))#同上

A=np.arange(14,2,-1).reshape((3,4))
print(A)

#clip(array,min,max),把array中数据全部置为min-max，
#小于min的用min代替，大于max的用max代替,中间的数值不变
print('判断5-9：',np.clip(A,5,9))

