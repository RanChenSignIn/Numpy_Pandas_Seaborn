import pandas as pd
import numpy as np

#一般的统计函数
np_zeros = np.zeros(500)#生成size为500的0，array
print(np_zeros.size)
print(np_zeros)

a=np.array([11,9,5,2,6,7,6,2,9])
a_unique=np.unique(a)#返冋其参数数组中所有不同的值，并且按照从小到大的顺序排列
print(a)
print(a_unique)

#return_index : Ture表示同时返回原始数组中的下标,及返回重排后的数组
#同时返回两个数组，第一个数据是重排后的数组，第二个数组是重排后数据在原始数组中的下标
a_index,index_index=np.unique(a,return_index=True)
print(a_index)
print(index_index)
#Return_inverse:True,表示返回，原始数据在重建数组后用的下标数组
a_inverse=np.unique(a,return_inverse=True)
print(a_inverse)

#Numpy 的统计函数
#生成一个4*6数组，
np_arange=np.arange(1,49,2).reshape((4,6))
print(np_arange.size)#打印数组的大小，size
print(np_arange)
np_min=np.min(np_arange,axis=0)#求取数组中，每一列的最小值 min
print(np_min)
np_max=np.max(np_arange,axis=1)#求取数组中，每一行的最大值max
print(np_max)#打印

#求取数组中的最大值的索引
np_argmax=np.argmax(np_arange)
print("np_argmax",np_argmax)
#求取数组中的最小值的索引
np_argmin=np.argmin(np_arange,axis=1)#求取每一行的最小值的索引
print("np_argmin",np_argmin)
#计算数组中最大值与最小值的差  ptp
np_ptp=np.ptp(np_arange,axis=0)#计算每一列最大值与最小值的差
print(np_ptp)#打印

#求取整个数组的的和 sum
np_sum=np.sum(np_arange)
print(np_sum)
#求数组中的每一列的和,或每一行的和
np_sum0=np.sum(np_arange,axis=0)
print(np_sum0)
#求数组的累加 cumsum
#求每一列的累加，或每一行的累加,同时保持了原数组的矩阵的大小
np_cumsum=np.cumsum(np_arange,axis=0)
print(np_cumsum)

#求取数组中的均值
#求取每一列的均值，或每一行的均值
np_mean=np.mean(np_arange,axis=0)
print(np_mean)
#求整个数据的均值
np_average=np.average(np_arange)
print(np_average)

#求数组中的中位数
#axis=0,求取每一列的中位数
# axis=1,求取每一行的中位数
np_median=np.median(np_arange)
print(np_median)

#求取一个数组的标准差
np_std0=np.std(np_arange,axis=0)#求数组的每一列的标准差
np_std1=np.std(np_arange,axis=1)#求数组的每一行的标准差
#求取一个数组的方差
print(np_std1)
np_var=np.var(np_arange,axis=1)#求数组的每一行的方差
print(np_var)

#求数组的协方差
np_array=np.array([[2,3,4],[4,5,6],[3,6,9],[2,5,8]])#4*3
print(np_array)
np_array_4=np_array-4
np_cov=np.cov(np_array,np_array_4)
print(np_cov)

#求数组中各元素的绝对值
np_abs=np.abs(np_array_4)
print(np_abs)
#求数组各元素的平方根
np_sqrt=np.sqrt(np_array)
print(np_sqrt)
#求数组各元素的平方
np_square=np.square(np_array_4)
print(np_square)
#求数组各元素的自然对数，10底对数，2底对数
np_log_e=np.log(np_array)#自然对数
np_log_10=np.log10(np_array)#10底对数
np_log_2=np.log2(np_array)#2底对数
np_log_any=np.log(np_array)/np.log(8)#any底对数

#计算数组各元素的ceiling值或floor值
#取数组各元素的ceiling值，即取不小于数组数据中的最小整数
np_ceil=np.ceil(np_array)
#取数组各元素的floor值，即取不大于数组数据中的最大整数
np_floor=np.floor(np_array)

#计算数组中各元素的四舍五入值
np_rint=np.rint(np_array)
#计算数组中各元素的指数值
np_exp=np.exp(np_array)

