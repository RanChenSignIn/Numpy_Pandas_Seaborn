import numpy as np

A=np.arange(3,15)#生成3-14的数据
print(A)
print("A[0]",A[0])
print('取第四个元素：',A[3])#取第四个

A=np.arange(3,15,1).reshape(3,4)#重排为3*4矩阵
print(A)
A2=A[2,2]#取A，array中的第2行第2列的元素
print(A[2,2])#同上
print(A2)

print(A[2][2])#取A，array中的第2行第2列的元素
print(A[:2][:2])
A23=A[:,2]#第二列所有的数据
print(A23)

for row in A:#打印每一行
    print(row)

for column in A.T:#没有column，通过翻转打印column
    print(column)

print(list(A.flat))#把3*4的array转变成一行的列表
# for item in A.flat:
#     print(item)
