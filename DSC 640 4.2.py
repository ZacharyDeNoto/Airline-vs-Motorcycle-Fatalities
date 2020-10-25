import matplotlib
import plotly
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import  pandas as pd
import xlrd
from matplotlib.ticker import FuncFormatter
import squarify
from matplotlib.pyplot import figure


#Code for scatter plot


figure(num=None, figsize=(11, 8), dpi=80)
data = pd.read_csv('birth-rate.csv')

ndata = data[data['1960']<17]

plt.scatter(x= ndata['Country'], y=ndata['1960'])

plt.xlabel('Country')
plt.ylabel('Birth Rate')
plt.title('Birth Rate for Countries in 1960')



plt.show()

#-----------------------------------------------------
#Code for bubble chart

ndata = data[data['1980']<30]
ndata = ndata[ndata['1960']<25]

plt.scatter(x= ndata['1980'], y=ndata['1960'], s=ndata['1980']*100, alpha=0.5)

plt.xlabel('1960s Birth Rate')
plt.ylabel('1980s Birth Rate')
plt.title('Birth Rate for Countries in 1960 vs 1980')

plt.show()
#-----------------------------------------------------

#Code for density plot

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

data = pd.read_csv('tv_sizes.txt',sep="\t")


data = data[data['year'] >2004]
data = data[data['size'] <40]


data1 = data[data['year'] ==2006]
data2 = data[data['year'] ==2007]
data3 = data[data['year'] ==2008]
data4 = data[data['year'] ==2009]
data5 = data[data['year'] ==2005]

sns.kdeplot(data5['size'], color="purple", shade=True, label = '2005')
sns.kdeplot(data1['size'], color="green", shade=True, label = '2006')
sns.kdeplot(data2['size'], color="blue", shade=True, label = '2007')
sns.kdeplot(data3['size'], color="red", shade=True, label = '2008')
sns.kdeplot(data4['size'], color="orange", shade=True, label = '2009')

plt.xlabel('TV Size')
plt.ylabel('Density')
plt.title('Density Plot of TV Sizes')


plt.show()