"""
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
# Load the example tips dataset
iris = sns.load_dataset("iris")
# Plot tip as a function of toal bill across days
g = sns.lmplot(x="sepal_length", y="sepal_width", hue="species",truncate=True, size=5, data=iris)
# Use more informative axis labels than are provided by default
g.set_axis_labels("Sepal length (mm)", "Sepal width (mm)")
plt.show()
"""


import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
sns.set_style('darkgrid')
# Load the example tips dataset
#iris = sns.load_dataset("D:\Program Files\Python36\Lib\site-packages\pandas\\tests\data\iris")
iris = pd.read_csv('D:\Program Files\Python36\Lib\site-packages\pandas\\tests\data\iris.csv')
# Plot tip as a function of toal bill across days
g=sns.lmplot(x='SepalLength', y='SepalWidth', hue='Name',truncate=True, size=5, data=iris)
# Use more informative axis labels than are provided by default
g.set_axis_labels("Sepal length (mm)", "Sepal width (mm)")
plt.show()