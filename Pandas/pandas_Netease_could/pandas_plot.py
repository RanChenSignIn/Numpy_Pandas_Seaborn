import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#plot data

#Series 线型数据
data=pd.Series(np.random.randn(1000),index=np.arange(1000))
data=data.cumsum()#累加
data.plot()#绘图
plt.show()
#DdtaFrame
data=pd.DataFrame(np.random.randn(1000,4),
                  index=np.arange(1000),
                  columns=list("ABCD"))
data=data.cumsum()
print(data.head)
#bar ,hist,box,area,scatter,hexbin,pie
data.plot()#绘图
ax=data.plot.scatter(x='A',y='B',color='r',label='Class 1')
data.plot.scatter(x='A',y='C',color='b',label='Class 2',ax=ax)

plt.show()