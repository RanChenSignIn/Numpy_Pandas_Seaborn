
import pandas as pd
import numpy as np
#merge
#merging two df by key/key.(may be used in database)
#simple example
left=pd.DataFrame({
    'key':['K0','K1','K2','K3'],
    'A':['A0','A1','A2','A3'],
    'B':['B0','B1','B2','B3']})
right=pd.DataFrame({
    'key':['K0','K1','K2','K3'],
    'C':['C0','C1','C2','C3'],
    'D':['D0','D1','D2','D3']})
print(left)
print(right)

res=pd.merge(left,right,on='key')
print(res)

#consider two keys
left = pd.DataFrame({
    'key1': ['K0', 'K0', 'K1', 'K2'],
    'key2': ['K0', 'K1', 'K0', 'K1'],
    'A': ['A0', 'A1', 'A2', 'A3'],
    'B': ['B0', 'B1', 'B2', 'B3']})
right = pd.DataFrame({
    'key1': ['K0', 'K1', 'K1', 'K2'],
     'key2': ['K0', 'K0', 'K0', 'K0'],
      'C': ['C0', 'C1', 'C2', 'C3'],
      'D': ['D0', 'D1', 'D2', 'D3']})
print("left:",left)
print("right",right)
#关键字key1,key2，同时作为合并依据,两个关键字同时相同的则合并为用一行，不同的则补齐nan
res_key1_key2=pd.merge(left,right,on=['key1','key2'],how='outer')
print('res_key1_key2',res_key1_key2)

# indicator
df1 = pd.DataFrame({'col1':[0,1], 'col_left':['a','b']})
df2 = pd.DataFrame({'col1':[1,2,2],'col_right':[2,2,2]})
print(df1)
print(df2)
res = pd.merge(df1, df2, on='col1', how='outer', indicator=True)
print(res)
# give the indicator a custom name
res_indicator_column = pd. merge(df1, df2, on='col1', how='outer', indicator='indicator_column')
#定义判断合并后的数据，两组数据那边有left_only,right_only，还是两边都有both
print(res_indicator_column)

# merged by index
left = pd.DataFrame({'A': ['A0', 'A1', 'A2'],
                    'B': ['B0', 'B1', 'B2']},
                    index=['K0', 'K1', 'K2'])
right = pd.DataFrame({'C': ['C0', 'C2', 'C3'],
                      'D': ['D0', 'D2', 'D3']},
                      index=['K0', 'K2', 'K3'])
print("left:",left)
print("right",right)
# left_index and right_index
res_outer= pd.merge(left, right, left_index=True, right_index=True, how='outer')
#合并全部，没有的关键字key，则补上nan
print('res_outer:',res_outer)
res_inner= pd.merge(left, right, left_index=True, right_index=True, how='inner')
#只合并关键字key相同的部分，inner，关键字不同的则舍弃
print('res_inner:',res_inner)
# handle overlapping
boys = pd.DataFrame({'k': ['K0', 'K1', 'K2'], 'age': [1, 2, 3]})
girls = pd.DataFrame({'k': ['K0', 'K0', 'K3'], 'age': [4, 5, 6]})
print(boys)
print(girls)
res = pd.merge(boys, girls, on='k', suffixes=['_boy', '_girl'], how='inner')
print(res)
