import matplotlib.pyplot as plot;plot.rcdefaults()
import numpy as np
import matplotlib.pyplot as plot
import math
from Database_Queries import recover_graphs
WTTR_values,WTDD_values,WTDL_values,KOTR_values,KODD_values, KODL_values,WTTRM_values,WTTRF_values,WTDDM_values,WTDDF_values,WTDLM_values, WTDLF_values,KOTRM_values,KOTRF_values,KODDM_values,KODDF_values, KODLM_values, KODLF_values = recover_graphs('arbor_length')
#Calculate Means
WTTR_Mean = np.mean(WTTR_values)
WTDD_Mean = np.mean(WTDD_values)
WTDL_Mean = np.mean(WTDL_values)
KOTR_Mean = np.mean(KOTR_values)
KODD_Mean = np.mean(KODD_values)
KODL_Mean = np.mean(KODL_values)
WTTRM_Mean = np.mean(WTTRM_values)
WTTRF_Mean = np.mean(WTTRF_values)
WTDDM_Mean = np.mean(WTDDM_values)
WTDDF_Mean = np.mean(WTDDF_values)
WTDLM_Mean = np.mean(WTDLM_values)
WTDLF_Mean = np.mean(WTDLF_values)
KOTRM_Mean = np.mean(KOTRM_values)
KOTRF_Mean = np.mean(KOTRF_values)
KODDM_Mean = np.mean(KODDM_values)
KODDF_Mean = np.mean(KODDF_values)
KODLM_Mean = np.mean(KODLM_values)
KODLF_Mean = np.mean(KODLF_values)

print WTTR_Mean, WTDD_Mean, WTDL_Mean
print KOTR_Mean, KODD_Mean, KODL_Mean

#Calculate SEM
WTTR_SEM = np.std(WTTR_values,ddof=1) / math.sqrt(len(WTTR_values))
WTDD_SEM = np.std(WTDD_values,ddof=1) / math.sqrt(len(WTDD_values))
WTDL_SEM = np.std(WTDL_values,ddof=1) / math.sqrt(len(WTDL_values))
KOTR_SEM = np.std(KOTR_values,ddof=1) / math.sqrt(len(KOTR_values))
KODD_SEM = np.std(KODD_values,ddof=1) / math.sqrt(len(KODD_values))
KODL_SEM = np.std(KODL_values,ddof=1) / math.sqrt(len(KODL_values))
WTTRM_SEM = np.std(WTTRM_values,ddof=1) / math.sqrt(len(WTTRM_values))
WTTRF_SEM = np.std(WTTRF_values,ddof=1) / math.sqrt(len(WTTRF_values))
WTDDM_SEM = np.std(WTDDM_values,ddof=1) / math.sqrt(len(WTDDM_values))
WTDDF_SEM = np.std(WTDDF_values,ddof=1) / math.sqrt(len(WTDDF_values))
WTDLM_SEM = np.std(WTDLM_values,ddof=1) / math.sqrt(len(WTDLM_values))
WTDLF_SEM = np.std(WTDLF_values,ddof=1) / math.sqrt(len(WTDLF_values))
KOTRM_SEM = np.std(KOTRM_values,ddof=1) / math.sqrt(len(KOTRM_values))
KOTRF_SEM = np.std(KOTRF_values,ddof=1) / math.sqrt(len(KOTRF_values))
KODDM_SEM = np.std(KODDM_values,ddof=1) / math.sqrt(len(KODDM_values))
KODDF_SEM = np.std(KODDF_values,ddof=1) / math.sqrt(len(KODDF_values))
KODLM_SEM = np.std(KODLM_values,ddof=1) / math.sqrt(len(KODLM_values))
KODLF_SEM = np.std(KODLF_values,ddof=1) / math.sqrt(len(KODLF_values))

fig,axs = plot.subplots(nrows=2, ncols=2, sharex=False)

#Plot WTTR, DR, DL graph
ax =axs[0,0]
objects = ('WT TR','WT DD','WT DL')
xvalue = np.arange(len(objects))
yvalue = [WTTR_Mean, WTDD_Mean, WTDL_Mean]
yerr = [WTTR_SEM, WTDD_SEM, WTDL_SEM]
bar_width = 0.35

ax.bar(xvalue, yvalue, bar_width, align='center', alpha=1,color=('#0d0d0d','#878787','#616161'),linewidth=0)
ax.set_ylabel('Metric')
ax.set_title('WT TR,DR,DL')
ax.errorbar(xvalue, yvalue, yerr, fmt='none', ecolor='#666666', elinewidth='2', capsize=10, capthick='2')


#plot WT*dep*sex graph
ax=axs[0,1]
objects = ('WT TR', 'WT DR', 'WT DL')
group_n = 3
xvalue = np.arange(group_n)
m_yvalue = [WTTRM_Mean,WTDDM_Mean,WTDLM_Mean]
f_yvalue = [WTTRF_Mean,WTDDF_Mean, WTDLF_Mean]
m_yerr =  [WTTRM_SEM,WTDDM_SEM,WTDLM_SEM]
f_yerr = [WTTRF_SEM,WTDDF_SEM,WTDLF_SEM]

bar_width = 0.35
opacity = 0.8

rects1 = ax.bar(xvalue, m_yvalue, bar_width,align='center',color=('#0d0d0d','#878787','#616161'), linewidth=0)

rects2 = ax.bar(xvalue + 0.4, f_yvalue, bar_width, align='center', color=('#0d0d0d','#878787','#616161'), linewidth=0)

#ax.set_xlabel('condition')
ax.set_title('Condition and Sex')
ax.set_xticks(xvalue + bar_width,('WT TR', 'WT DR', 'WT DL'))
ax.errorbar(xvalue, m_yvalue,m_yerr,fmt='none',ecolor= '#666666',elinewidth='2',capsize=5,capthick='2')
ax.errorbar(xvalue+0.4, f_yvalue,f_yerr,fmt='none',ecolor= '#666666',elinewidth='2',capsize=5,capthick='2')

#Plot KOTR, DR, DL graph
ax =axs[1,0]
objects = ('KO TR','KO DD','KO DL')
xvalue = np.arange(len(objects))
yvalue = [KOTR_Mean, KODD_Mean, KODL_Mean]
yerr = [KOTR_SEM, KODD_SEM, KODL_SEM]
bar_width = 0.35

ax.bar(xvalue, yvalue,bar_width, align='center', alpha=1,color=('#035069','#3D9CBC','#2a6d83'),linewidth=0)
ax.set_ylabel('Metric')
ax.set_title('KO TR,DR,DL')
ax.errorbar(xvalue, yvalue, yerr, fmt='none', ecolor='#666666', elinewidth='2', capsize=10, capthick='2')


#plot KO*dep*sex graph
ax=axs[1,1]
objects = ('KO TR', 'KO DR', 'KO DL')
group_n = 3
xvalue = np.arange(group_n)
m_yvalue = [KOTRM_Mean,KODDM_Mean,KODLM_Mean]
f_yvalue = [KOTRF_Mean,KODDF_Mean, KODLF_Mean]
m_yerr =  [KOTRM_SEM,KODDM_SEM,KODLM_SEM]
f_yerr = [KOTRF_SEM,KODDF_SEM,KODLF_SEM]

bar_width = 0.35
# opacity = 0.8

rects3 = ax.bar(xvalue, m_yvalue, bar_width,align='center',color=('#035069','#3D9CBC','#2a6d83'), linewidth=0)

rects4 = ax.bar(xvalue + 0.4, f_yvalue, bar_width, align='center', color=('#035069','#3D9CBC','#2a6d83'), linewidth=0)

#ax.set_xlabel('condition')
ax.set_title('Condition and Sex')
ax.set_xticks(xvalue + bar_width,('KO TR', 'KO DR', 'KO DL'))
ax.errorbar(xvalue, m_yvalue,m_yerr,fmt='none',ecolor= '#666666',elinewidth='2',capsize=5,capthick='2')
ax.errorbar(xvalue+0.4, f_yvalue,f_yerr,fmt='none',ecolor= '#666666',elinewidth='2',capsize=5,capthick='2')



# #Plot WT vs KO boxplot
# ax =axs[1,0]
# WTTR_data = WTTR_values
# KOTR_data = KOTR_values
# data=(WTTR_data,KOTR_data)
#
# boxprops = dict(linestyle='-', linewidth=0, color ='none',facecolor=('#035069'))
# flierprops = dict(marker='o', markerfacecolor='#E0B104', markersize=4,markeredgecolor='none')
# medianprops = dict(linestyle='-', linewidth=2.5, color='white')
# whiskerprops=dict(linestyle='-',color='#666666',linewidth=2)
# capprops= dict(linewidth=2,color='#666666')
#
# box=ax.boxplot(data, patch_artist=True, sym='o',boxprops=boxprops, flierprops=flierprops,medianprops=medianprops, whiskerprops=whiskerprops,capprops=capprops)
# colors = ['#0d0d0d','#035069']
# for patch, color in zip(box['boxes'], colors):
#     patch.set_facecolor(color)
# ax.set_title('WT vs. KO')
#
#
#
# # Plot WT vs KO * TR vs DR boxplot
# ax =axs[1,1]
#
# WTTR_data = WTTR_values
# KOTR_data = KOTR_values
# WTDD_data = WTDD_values
# KODD_data = KODD_values
# data=(WTTR_data,WTDD_data,KOTR_data,KODD_data)
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
# ax.set_title('WT/KO * TR/DR')
#
#
#
# # Plot WT/KO * TR/DR * M/F
# ax =axs[1,2]
# WTTRM_data = WTTRM_values
# WTTRF_data = WTTRF_values
# KOTRM_data = KOTRM_values
# KOTRF_data = KOTRF_values
# WTDDM_data = WTDDM_values
# WTDDF_data = WTDDF_values
# KODDM_data = KODDM_values
# KODDF_data = KODDF_values
# data=(WTTRM_data,WTTRF_data,WTDDM_data,WTDDF_data,KOTRM_data,KOTRF_data,KODDM_data,KODDF_data)
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
# ax.set_title('WT/KO * TR/DR * M/F')


plot.show()


