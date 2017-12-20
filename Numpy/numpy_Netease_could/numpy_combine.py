import numpy as np
#矩阵合并
A=np.array([1,1,1])#全为1
B=np.array([2,2,2])#全为2
B_mean=np.mean(B)#B均值
print(B_mean)
print(np.vstack((A,B)))#把A和B列方向合并，上下合并，成2*3
print(np.hstack((A,B)))#行方向合并，左右合并，成1*6
C=np.vstack((A,B))

print(C.shape)#打印矩阵大小

A_T=A.T#A的转置
C_T=C.T#C的转置
print(C_T)
print(C_T.shape)#打印矩阵的大小
# print(A)
# print(A_T)

print(A[:,np.newaxis])#将横向的变成纵向的

C=np.concatenate((A,B,B,A),axis=0)#多个array横向或纵向的合并,同时定义那个维度合并
print(C)

