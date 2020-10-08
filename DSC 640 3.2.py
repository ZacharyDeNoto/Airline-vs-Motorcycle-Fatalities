import matplotlib
import plotly
import seaborn
import matplotlib.pyplot as plt
import numpy as np
import  pandas as pd
import xlrd
from matplotlib.ticker import FuncFormatter
import squarify
from matplotlib.pyplot import figure


#Code for Area Chart

unemployment = pd.read_csv('unemployement-rate-1948-2010.csv')

unemployment_group = unemployment.groupby(['Year']).mean().reset_index()



plt.fill_between(unemployment_group['Year'], unemployment_group['Value'], color = 'blue')

plt.xlabel('Year')
plt.ylabel('Unemployment Percentage)')
plt.title('Area Chart of Unemployment by Year')



plt.show()

#-----------------------------------------------------

#Code for Stacked Area Chart

figure(num=None, figsize=(9, 7), dpi=80)
unemployment = unemployment[unemployment['Year']<2010]
print(unemployment)

plt.stackplot(list(set(unemployment.Year.values)), unemployment.Value[unemployment.Period == 'M01'],
              unemployment.Value[unemployment.Period == 'M02'],
              unemployment.Value[unemployment.Period == 'M03'],
              unemployment.Value[unemployment.Period == 'M04'],
              unemployment.Value[unemployment.Period == 'M05'],
              unemployment.Value[unemployment.Period == 'M06'],
              unemployment.Value[unemployment.Period == 'M07'],
              unemployment.Value[unemployment.Period == 'M08'],
              unemployment.Value[unemployment.Period == 'M09'],
              unemployment.Value[unemployment.Period == 'M10'],
              unemployment.Value[unemployment.Period == 'M11'],
              unemployment.Value[unemployment.Period == 'M12'], labels=['M01','M02','M03','M04',
                                                                        'M05','M06','M07','M08',
                                                                        'M09','M10','M11','M12'])

#plt.xticks([1948,2009], )
plt.legend(loc = 'upper left')
plt.title('Stacked Area Chart of Unemployment by Month')
plt.show()

#-----------------------------------------------------

#Code for Tree Map

figure(num=None, figsize=(10, 8), dpi=80)
month = unemployment[unemployment['Period']=='M12']
vals = list(set(unemployment[unemployment['Period']=='M12'].Value.values))

month['labs'] = month['Year'].astype(str) + ' - ' + month['Value'].astype(str) + '%'
month = month.sort_values(by=['Value'])
print(month)

squarify.plot(sizes=month['Value'], label=month['labs'])
plt.axis('off')
plt.title('Heatmap of Unemployment in December')
plt.show()







