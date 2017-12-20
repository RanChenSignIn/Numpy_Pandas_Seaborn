import seaborn as sns
import matplotlib.pyplot as plt
sns.set_style(style="darkgrid")
# Load the example tips dataset
iris = sns.load_dataset("D:\Program Files\Python36\Lib\site-packages\pandas\\tests\data\iris")
# Plot tip as a function of toal bill across days
g = sns.lmplot(x="sepal_length", y="sepal_width", hue="species",truncate=True, size=5, data=iris)
# Use more informative axis labels than are provided by default
g.set_axis_labels("Sepal length (mm)", "Sepal width (mm)")
plt.show()