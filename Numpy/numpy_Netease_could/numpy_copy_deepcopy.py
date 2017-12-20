import numpy as np

#浅度复制
a=np.arange(4)
print(a)
b=a
c=a
d=b
a[0]=6
print(a)
print(b)
print(c)
print(b is a)#判断a是否是与b完全相同，成立返回true,否则返回FALSE
#deep copy
b=a.copy()
#或者 b=a[:]
print(b)
a[3]=33
print(a)