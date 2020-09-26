import matplotlib
import plotly
import seaborn
import matplotlib.pyplot as plt
import numpy as np
import  pandas as pd
import xlrd
from matplotlib.ticker import FuncFormatter



#Code for Bar Chart

population = pd.read_excel('world-population.xlsm')

plt.plot(population['Year'], population['Population']/10**9)


plt.xlabel('Year')
plt.ylabel('World Population(In Billions)')
plt.title('World Population by Year')

plt.show()

#-----------------------------------------------------

#Code for Step Chart
plt.step(population['Year'], population['Population']/10**9, color = 'black')


plt.xlabel('Year')
plt.ylabel('World Population(In Billions)')
plt.title('World Population by Year')

plt.show()





