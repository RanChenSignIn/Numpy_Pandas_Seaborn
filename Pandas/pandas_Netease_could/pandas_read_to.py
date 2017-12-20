#读取数据  导出
#read_csv
#to_csv
import pandas as pd
data=pd.read_csv('student.csv')
print(data)
data.to_pickle('studend.pickle')
