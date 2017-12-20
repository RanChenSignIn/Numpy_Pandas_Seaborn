import numpy as np

A=np.arange(12).reshape((3,4))#创建3*4
print(A)
#对等的分割，分成相同的块
print(np.split(A,2,axis=1))#对A分割，两块，纵向分割
print(np.split(A,3,axis=0))#横向分割，分割三块，
#不等的分割
print(np.array_split(A,3,axis=1))#不等的分割，四列分割成三块
print(np.vsplit(A,3))#分割成纵向的3块
print(np.hsplit(A,2))#分割成横向的2块
