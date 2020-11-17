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
#from ggplot import *
from plotnine import*
#import plotly.plotly as py
import plotly.graph_objects as go
import statistics

#Code for histogram


figure(num=None, figsize=(11, 8), dpi=80)
data = pd.read_csv('education.csv')

data['reading'].plot.hist()
plt.color = 'bold'
plt.show()

#-----------------------------------------------------
#Code for boxplot

#sns.catplot(x = data['writing,reading'], kind='box', data = data)

#data = data.drop(columns =['state','percent_graduates_sat','pupil_staff_ratio','dropout_rate'])
#plt.boxplot(data['reading'])
#plt.boxplot(data['writing'])
x = [data['reading'], data['writing'], data['math']]
plt.boxplot(x)

plt.show()

#-----------------------------------------------------
#Code for scatterplot

ax = plt.gca()

ax.scatter(data['state'],data['reading'], color="b",label= 'Reading')

ax.scatter(data['state'],data['writing'], color="g", label = 'Writing')

plt.axhline(np.mean(data['reading']), color = 'b')
plt.axhline(np.mean(data['writing']), color="g")
ax.legend()
plt.title('Scores of Subject by State with Averages')
plt.xlabel('State')
plt.ylabel('Score')
plt.xticks(rotation=90)

plt.show()


#-----------------------------------------------------

#Code for bullet chart

fig = go.Figure()


fig.add_trace(go.Indicator(
    mode= 'number+gauge+delta',
    gauge = {'shape': "bullet",
             'bar':{'color':'blue'}},
    value = statistics.mean(data['reading']),
    delta = {'reference': 600},
    domain = {'x': [0.25, 1], 'y': [0.1, 0.35]},
    title = {'text': "Reading"}))

fig.add_trace(go.Indicator(
    mode= 'number+gauge+delta',
    gauge = {'shape': "bullet",
             'bar':{'color':'green'},
             'axis':{'ticks':'',
                     'visible':False}},
    value = statistics.mean(data['writing']),
    delta = {'reference': 600},
    domain = {'x': [0.25, 1], 'y': [0.4, 0.65]},
    title = {'text': "Writing"}))

fig.add_trace(go.Indicator(
    mode= 'number+gauge+delta',
    gauge = {'shape': "bullet",
             'bar':{'color':'red'},
             'axis': {'ticks': '',
                      'visible': False}},
    value = statistics.mean(data['math']),
    delta = {'reference': 600},
    domain = {'x': [0.25, 1], 'y': [0.7, 0.95]},
    title = {'text': "Math"}))

fig.update_layout(height = 400,margin = {'t':0,'r':100, 'l':100})


fig.show()



