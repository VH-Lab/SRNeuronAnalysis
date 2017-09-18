import matplotlib.pyplot as plot;plot.rcdefaults()
import numpy as np
import matplotlib.pyplot as plot
import math
from Database_Queries import summary_graphs
WTTR_values,WTDD_values,KOTR_values,KODD_values,WTTRM_values,WTTRF_values,WTDDM_values,WTDDF_values,KOTRM_values,KOTRF_values,KODDM_values,KODDF_values = summary_graphs('P30','tree_number')

#Calculate Means
WTTR_Mean = np.mean(WTTR_values)
WTDD_Mean = np.mean(WTDD_values)
KOTR_Mean = np.mean(KOTR_values)
KODD_Mean = np.mean(KODD_values)
WTTRM_Mean = np.mean(WTTRM_values)
WTTRF_Mean = np.mean(WTTRF_values)
WTDDM_Mean = np.mean(WTDDM_values)
WTDDF_Mean = np.mean(WTDDF_values)
KOTRM_Mean = np.mean(KOTRM_values)
KOTRF_Mean = np.mean(KOTRF_values)
KODDM_Mean = np.mean(KODDM_values)
KODDF_Mean = np.mean(KODDF_values)

#Calculate SEM
WTTR_SEM = np.std(WTTR_values,ddof=1) / math.sqrt(len(WTTR_values))
WTDD_SEM = np.std(WTDD_values,ddof=1) / math.sqrt(len(WTDD_values))
KOTR_SEM = np.std(KOTR_values,ddof=1) / math.sqrt(len(KOTR_values))
KODD_SEM = np.std(KODD_values,ddof=1) / math.sqrt(len(KODD_values))
WTTRM_SEM = np.std(WTTRM_values,ddof=1) / math.sqrt(len(WTTRM_values))
WTTRF_SEM = np.std(WTTRF_values,ddof=1) / math.sqrt(len(WTTRF_values))
WTDDM_SEM = np.std(WTDDM_values,ddof=1) / math.sqrt(len(WTDDM_values))
WTDDF_SEM = np.std(WTDDF_values,ddof=1) / math.sqrt(len(WTDDF_values))
KOTRM_SEM = np.std(KOTRM_values,ddof=1) / math.sqrt(len(KOTRM_values))
KOTRF_SEM = np.std(KOTRF_values,ddof=1) / math.sqrt(len(KOTRF_values))
KODDM_SEM = np.std(KODDM_values,ddof=1) / math.sqrt(len(KODDM_values))
KODDF_SEM = np.std(KODDF_values,ddof=1) / math.sqrt(len(KODDF_values))

fig,axs = plot.subplots(nrows=2, ncols=3, sharex=False)

#Plot WT/KO graph
ax =axs[0,0]
objects = ('WT','KO')
xvalue = np.arange(len(objects))
yvalue = [WTTR_Mean, KOTR_Mean]
yerr = [WTTR_SEM, KOTR_SEM]

ax.bar(xvalue, yvalue, align='center', alpha=1,color=('#0d0d0d','#035069'),linewidth=0)
ax.set_ylabel('Metric')
ax.set_title('WT vs. KO')
ax.errorbar(xvalue, yvalue, yerr, fmt='none', ecolor='#666666', elinewidth='2', capsize=10, capthick='2')


#Plot Depriviation condition graph
ax=axs[0,1]
objects = ('WT', 'WT DR', 'KO', 'KO DR')
xvalue = np.arange(len(objects))
yvalue = [WTTR_Mean, WTDD_Mean, KOTR_Mean, KODD_Mean]
yerr = [WTTR_SEM, WTDD_SEM, KOTR_SEM, KODD_SEM]

ax.bar(xvalue, yvalue, align='center', alpha=1, color=('#0d0d0d','#878787','#035069','#3D9CBC'), linewidth=0)
ax.set_title('Genotype * Condition')
ax.errorbar(xvalue,yvalue,yerr,fmt='none',ecolor= '#666666',elinewidth='2',capsize=10,capthick='2')


#plot geno*dep*sex graph
ax=axs[0,2]
objects = ('WT TR', 'WT DR', 'KO TR', 'KO DR')
group_n = 4
xvalue = np.arange(group_n)
m_yvalue = [WTTRM_Mean,WTDDM_Mean,KOTRM_Mean,KODDM_Mean]
f_yvalue = [WTTRF_Mean,WTDDF_Mean,KOTRF_Mean,KODDF_Mean]
m_yerr =  [WTTRM_SEM,WTDDM_SEM,KOTRM_SEM,KODDM_SEM]
f_yerr = [WTTRF_SEM,WTDDF_SEM,KOTRF_SEM,KODDF_SEM]

bar_width = 0.35
opacity = 0.8

rects1 = ax.bar(xvalue, m_yvalue, bar_width,align='center',color=('#0d0d0d','#878787','#035069','#3D9CBC'), linewidth=0)

rects2 = ax.bar(xvalue + 0.4, f_yvalue, bar_width, align='center', color=('#0d0d0d','#878787','#035069','#3D9CBC'), linewidth=0)

#ax.set_xlabel('condition')
ax.set_title('Condition and Sex')
ax.set_xticks(xvalue + bar_width,('WT TR', 'WT DR', 'KO TR', 'KO DR'))
ax.errorbar(xvalue, m_yvalue,m_yerr,fmt='none',ecolor= '#666666',elinewidth='2',capsize=5,capthick='2')
ax.errorbar(xvalue+0.4, f_yvalue,f_yerr,fmt='none',ecolor= '#666666',elinewidth='2',capsize=5,capthick='2')


#Plot WT vs KO boxplot
ax =axs[1,0]
WTTR_data = WTTR_values
KOTR_data = KOTR_values
data=(WTTR_data,KOTR_data)

boxprops = dict(linestyle='-', linewidth=0, color ='none',facecolor=('#035069'))
flierprops = dict(marker='o', markerfacecolor='#E0B104', markersize=4,markeredgecolor='none')
medianprops = dict(linestyle='-', linewidth=2.5, color='white')
whiskerprops=dict(linestyle='-',color='#666666',linewidth=2)
capprops= dict(linewidth=2,color='#666666')

box=ax.boxplot(data, patch_artist=True, sym='o',boxprops=boxprops, flierprops=flierprops,medianprops=medianprops, whiskerprops=whiskerprops,capprops=capprops)
colors = ['#0d0d0d','#035069']
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)
ax.set_title('WT vs. KO')



# Plot WT vs KO * TR vs DR boxplot
ax =axs[1,1]

WTTR_data = WTTR_values
KOTR_data = KOTR_values
WTDD_data = WTDD_values
KODD_data = KODD_values
data=(WTTR_data,WTDD_data,KOTR_data,KODD_data)

boxprops = dict(linestyle='-', linewidth=0, color ='none',facecolor=('#035069'))
flierprops = dict(marker='o', markerfacecolor='#E0B104', markersize=4,markeredgecolor='none')
medianprops = dict(linestyle='-', linewidth=2.5, color='white')
whiskerprops=dict(linestyle='-',color='#666666',linewidth=2)
capprops= dict(linewidth=2,color='#666666')

box=ax.boxplot(data, patch_artist=True, sym='o',boxprops=boxprops, flierprops=flierprops,medianprops=medianprops, whiskerprops=whiskerprops,capprops=capprops)
colors = ['#0d0d0d','#878787','#035069','#3D9CBC']
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)
ax.set_title('WT/KO * TR/DR')



# Plot WT/KO * TR/DR * M/F
ax =axs[1,2]
WTTRM_data = WTTRM_values
WTTRF_data = WTTRF_values
KOTRM_data = KOTRM_values
KOTRF_data = KOTRF_values
WTDDM_data = WTDDM_values
WTDDF_data = WTDDF_values
KODDM_data = KODDM_values
KODDF_data = KODDF_values
data=(WTTRM_data,WTTRF_data,WTDDM_data,WTDDF_data,KOTRM_data,KOTRF_data,KODDM_data,KODDF_data)

position=[1,2,4,5,7,8,10,11]


boxprops = dict(linestyle='-', linewidth=0, color ='none',facecolor=('#035069'))
flierprops = dict(marker='o', markerfacecolor='#E0B104', markersize=4,markeredgecolor='none')
medianprops = dict(linestyle='-', linewidth=2.5, color='white')
whiskerprops=dict(linestyle='-',color='#666666',linewidth=2)
capprops= dict(linewidth=2,color='#666666')

box=ax.boxplot(data,positions = position, patch_artist=True, sym='o',boxprops=boxprops, flierprops=flierprops,medianprops=medianprops, whiskerprops=whiskerprops,capprops=capprops)
colors = ['#0d0d0d','#0d0d0d','#878787', '#878787', '#035069', '#035069','#3D9CBC','#3D9CBC']
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)
ax.set_title('WT/KO * TR/DR * M/F')


plot.show()





