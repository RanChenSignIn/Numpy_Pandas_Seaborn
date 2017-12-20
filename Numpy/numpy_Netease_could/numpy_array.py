# import pandas
import numpy as np

array=np.array([[1,2,3,],
                [2,3,4,],
                [3,4,5,]])#list列表形式,二维，两个中括号，内括号列表，外括号矩阵
print(array)
print('number of dim:',array.ndim)#读取维数
print('shape:',array.shape)#行数与列数
print('size:',array.size)#元素多少


"""
a=np.array([2,23,74],dtype=np.int32)
b=np.array([2,23,4],dtype=np.float)
print(a.dtype)
print(b.dtype)

zero_a=np.zeros((3,4),dtype=np.int)#三行四列矩阵,双括号
print(zero_a)

ones_a=np.ones((3,4),dtype=np.int8)#三行四列矩阵,双括号
print(ones_a)

a=np.arange(10,20,2)#生成10-20，步长2的矩阵
print(a)

a=np.arange(12).reshape((3,4))#reshape,双括号
print(a)

a=np.linspace(1,200,50,dtype=np.int16).reshape((5,10))#1-200之间，生成50个点
print(a)
"""