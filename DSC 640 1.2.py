import matplotlib
import plotly
import seaborn
import matplotlib.pyplot as plt
import numpy as np
import  pandas as pd
import xlrd

#Code for Bar Chart

hotdog_winner = pd.read_excel('hotdog-contest-winners.xlsm')
obama = pd.read_excel('obama-approval-ratings.xls')

plt.barh(obama['Issue'], obama['Approve'])

plt.xlabel('Approval Rating')
plt.ylabel('Policy')
plt.title('Approval Ratings for Obama per Subject')

plt.show()

#-----------------------------------------------------

#Code for Stacked Bar Chart

obama1 = obama[obama['Approve']>43]
p1 = plt.bar(obama1['Issue'], obama1['Approve'])
p2 = plt.bar(obama1['Issue'], obama1['Disapprove'], bottom=obama1['Approve'])
p3 = plt.bar(obama1['Issue'], obama1['None'], bottom= np.array(obama1['Approve'])+np.array(obama1['Disapprove']))

plt.xlabel('Policy')
plt.ylabel('Percentage')
plt.title('Approval Ratings for Obama per Subject')
plt.legend(['Approval','Disapproval','None'], loc = 'lower right')

plt.show()

#----------------------------------------------------

#Code for Pie Chart

obama1 = obama[obama['Issue']=='Race Relations']

nums = []

for i in range(1,4) :
    nums.append(obama1.iloc[0,i])

labels = obama1.columns
labels = labels[1:]


plt.pie(nums, labels = labels,autopct='%1.1f%%')

plt.title('Obamas Approval Ratings for Race Relations')


plt.show()


#----------------------------------------------------

#Code for Donut Chart

obama2 = obama[obama['Issue']=='Immigration']

nums2 = []

for i in range(1,4) :
    nums2.append(obama2.iloc[0,i])

labels2 = obama2.columns
labels2 = labels2[1:]


plt.pie(nums2, labels = labels2,autopct='%1.1f%%')

my_circle=plt.Circle( (0,0), 0.7, color='white')
p=plt.gcf()
p.gca().add_artist(my_circle)
plt.title('Obamas Approval Ratings for Immigration')

plt.show()









