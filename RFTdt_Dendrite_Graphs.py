import matplotlib.pyplot as plot;plot.rcdefaults()
import numpy as np
import matplotlib.pyplot as plot
import math
from RFTdt_Database_Queries import summary_graphs
WTTR_values, FLXTR_values = summary_graphs('07dpi','volume')
# print WTTR_values
# print FLXTR_values
#Calculate Means
WTTR_Mean = np.mean(WTTR_values)
# WTDD_Mean = np.mean(WTDD_values)
FLXTR_Mean = np.mean(FLXTR_values)
# FLXDD_Mean = np.mean(FLXDD_values)
# WTTRM_Mean = np.mean(WTTRM_values)
# WTTRF_Mean = np.mean(WTTRF_values)
# WTDDM_Mean = np.mean(WTDDM_values)
# WTDDF_Mean = np.mean(WTDDF_values)
# FLXTRM_Mean = np.mean(FLXTRM_values)
# FLXTRF_Mean = np.mean(FLXTRF_values)
# FLXDDM_Mean = np.mean(FLXDDM_values)
# FLXDDF_Mean = np.mean(FLXDDF_values)

#Calculate SEM
WTTR_SEM = np.std(WTTR_values,ddof=1) / math.sqrt(len(WTTR_values))
# WTDD_SEM = np.std(WTDD_values,ddof=1) / math.sqrt(len(WTDD_values))
FLXTR_SEM = np.std(FLXTR_values,ddof=1) / math.sqrt(len(FLXTR_values))
# FLXDD_SEM = np.std(FLXDD_values,ddof=1) / math.sqrt(len(FLXDD_values))
# WTTRM_SEM = np.std(WTTRM_values,ddof=1) / math.sqrt(len(WTTRM_values))
# WTTRF_SEM = np.std(WTTRF_values,ddof=1) / math.sqrt(len(WTTRF_values))
# WTDDM_SEM = np.std(WTDDM_values,ddof=1) / math.sqrt(len(WTDDM_values))
# WTDDF_SEM = np.std(WTDDF_values,ddof=1) / math.sqrt(len(WTDDF_values))
# FLXTRM_SEM = np.std(FLXTRM_values,ddof=1) / math.sqrt(len(FLXTRM_values))
# FLXTRF_SEM = np.std(FLXTRF_values,ddof=1) / math.sqrt(len(FLXTRF_values))
# FLXDDM_SEM = np.std(FLXDDM_values,ddof=1) / math.sqrt(len(FLXDDM_values))
# FLXDDF_SEM = np.std(FLXDDF_values,ddof=1) / math.sqrt(len(FLXDDF_values))

fig,axs = plot.subplots(nrows=1, ncols=2, sharex=False)

#Plot WT/FLX graph
ax =axs[0]
objects = ('WT','FLX')
xvalue = np.arange(len(objects))
yvalue = [WTTR_Mean, FLXTR_Mean]
yerr = [WTTR_SEM, FLXTR_SEM]
bar_width=0.35
from random import *


# print WTTR_values
WT_xcoords = []
WT_xcoords = [uniform(-0.05,0.05) for value in WTTR_values]
# print WT_xcoords

FLX_xcoords = []
FLX_xcoords = [uniform(0.95,1.05) for value in FLXTR_values]

ax.scatter(WT_xcoords,WTTR_values, color = '#035069',zorder='3',alpha='0.8',edgecolors='none',s=50)
ax.scatter(FLX_xcoords,FLXTR_values, color = '#035069',zorder='3',alpha='0.8',edgecolors='none',s=50)
ax.bar(xvalue, yvalue,bar_width, align='center', alpha=1,color=('#0d0d0d','#DFB125'),linewidth=0)
ax.set_ylabel('Metric')
ax.set_title('WT vs. FLX')
ax.errorbar(xvalue, yvalue, yerr, fmt='none', ecolor='#666666', elinewidth='2', capsize=10, capthick='2', zorder='1')



# #Plot Depriviation condition graph
# ax=axs[0,1]
# objects = ('WT', 'WT DR', 'FLX', 'FLX DR')
# xvalue = np.arange(len(objects))
# yvalue = [WTTR_Mean, WTDD_Mean, FLXTR_Mean, FLXDD_Mean]
# yerr = [WTTR_SEM, WTDD_SEM, FLXTR_SEM, FLXDD_SEM]
#
# ax.bar(xvalue, yvalue, align='center', alpha=1, color=('#0d0d0d','#878787','#035069','#3D9CBC'), linewidth=0)
# ax.set_title('Genotype * Condition')
# ax.errorbar(xvalue,yvalue,yerr,fmt='none',ecolor= '#666666',elinewidth='2',capsize=10,capthick='2')
#
#
# #plot geno*dep*sex graph
# ax=axs[0,2]
# objects = ('WT TR', 'WT DR', 'FLX TR', 'FLX DR')
# group_n = 4
# xvalue = np.arange(group_n)
# m_yvalue = [WTTRM_Mean,WTDDM_Mean,FLXTRM_Mean,FLXDDM_Mean]
# f_yvalue = [WTTRF_Mean,WTDDF_Mean,FLXTRF_Mean,FLXDDF_Mean]
# m_yerr =  [WTTRM_SEM,WTDDM_SEM,FLXTRM_SEM,FLXDDM_SEM]
# f_yerr = [WTTRF_SEM,WTDDF_SEM,FLXTRF_SEM,FLXDDF_SEM]
#
# bar_width = 0.35
# opacity = 0.8
#
# rects1 = ax.bar(xvalue, m_yvalue, bar_width,align='center',color=('#0d0d0d','#878787','#035069','#3D9CBC'), linewidth=0)
#
# rects2 = ax.bar(xvalue + 0.4, f_yvalue, bar_width, align='center', color=('#0d0d0d','#878787','#035069','#3D9CBC'), linewidth=0)
#
# #ax.set_xlabel('condition')
# ax.set_title('Condition and Sex')
# ax.set_xticks(xvalue + bar_width,('WT TR', 'WT DR', 'FLX TR', 'FLX DR'))
# ax.errorbar(xvalue, m_yvalue,m_yerr,fmt='none',ecolor= '#666666',elinewidth='2',capsize=5,capthick='2')
# ax.errorbar(xvalue+0.4, f_yvalue,f_yerr,fmt='none',ecolor= '#666666',elinewidth='2',capsize=5,capthick='2')


#Plot WT vs FLX boxplot
ax =axs[1]
WTTR_data = WTTR_values
FLXTR_data = FLXTR_values
data=(WTTR_data,FLXTR_data)

WT_xcoords = []
WT_xcoords = [uniform(0.95,1.05) for value in WTTR_values]
# print WT_xcoords

FLX_xcoords = []
FLX_xcoords = [uniform(1.95,2.05) for value in FLXTR_values]

ax.scatter(WT_xcoords,WTTR_values, color = '#035069',zorder='1')
ax.scatter(FLX_xcoords,FLXTR_values, color = '#035069',zorder='1')

boxprops = dict(linestyle='-', linewidth=0, color ='none',facecolor=('#DFB125'))
flierprops = dict(marker='o', markerfacecolor='#5E4FC9', markersize=4,markeredgecolor='none')
medianprops = dict(linestyle='-', linewidth=2.5, color='white')
whiskerprops=dict(linestyle='-',color='#666666',linewidth=2)
capprops= dict(linewidth=2,color='#666666')

box=ax.boxplot(data, patch_artist=True, sym='o',boxprops=boxprops, flierprops=flierprops,medianprops=medianprops, whiskerprops=whiskerprops,capprops=capprops)
colors = ['#0d0d0d','#DFB125']
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)
ax.set_title('WT vs. FLX')



# # Plot WT vs FLX * TR vs DR boxplot
# ax =axs[1,1]
#
# WTTR_data = WTTR_values
# FLXTR_data = FLXTR_values
# WTDD_data = WTDD_values
# FLXDD_data = FLXDD_values
# data=(WTTR_data,WTDD_data,FLXTR_data,FLXDD_data)
#
# boxprops = dict(linestyle='-', linewidth=0, color ='none',facecolor=('#035069'))
# flierprops = dict(marker='o', markerfacecolor='#E0B104', markersize=4,markeredgecolor='none')
# medianprops = dict(linestyle='-', linewidth=2.5, color='white')
# whiskerprops=dict(linestyle='-',color='#666666',linewidth=2)
# capprops= dict(linewidth=2,color='#666666')
#
# box=ax.boxplot(data, patch_artist=True, sym='o',boxprops=boxprops, flierprops=flierprops,medianprops=medianprops, whiskerprops=whiskerprops,capprops=capprops)
# colors = ['#0d0d0d','#878787','#035069','#3D9CBC']
# for patch, color in zip(box['boxes'], colors):
#     patch.set_facecolor(color)
# ax.set_title('WT/FLX * TR/DR')
#
#
#
# # Plot WT/FLX * TR/DR * M/F
# ax =axs[1,2]
# WTTRM_data = WTTRM_values
# WTTRF_data = WTTRF_values
# FLXTRM_data = FLXTRM_values
# FLXTRF_data = FLXTRF_values
# WTDDM_data = WTDDM_values
# WTDDF_data = WTDDF_values
# FLXDDM_data = FLXDDM_values
# FLXDDF_data = FLXDDF_values
# data=(WTTRM_data,WTTRF_data,WTDDM_data,WTDDF_data,FLXTRM_data,FLXTRF_data,FLXDDM_data,FLXDDF_data)
#
# position=[1,2,4,5,7,8,10,11]
#
#
# boxprops = dict(linestyle='-', linewidth=0, color ='none',facecolor=('#035069'))
# flierprops = dict(marker='o', markerfacecolor='#E0B104', markersize=4,markeredgecolor='none')
# medianprops = dict(linestyle='-', linewidth=2.5, color='white')
# whiskerprops=dict(linestyle='-',color='#666666',linewidth=2)
# capprops= dict(linewidth=2,color='#666666')
#
# box=ax.boxplot(data,positions = position, patch_artist=True, sym='o',boxprops=boxprops, flierprops=flierprops,medianprops=medianprops, whiskerprops=whiskerprops,capprops=capprops)
# colors = ['#0d0d0d','#0d0d0d','#878787', '#878787', '#035069', '#035069','#3D9CBC','#3D9CBC']
# for patch, color in zip(box['boxes'], colors):
#     patch.set_facecolor(color)
# ax.set_title('WT/FLX * TR/DR * M/F')


plot.show()





