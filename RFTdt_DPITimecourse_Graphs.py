import math
import matplotlib.pyplot as plot;plot.rcdefaults()
import numpy as np
import matplotlib.pyplot as plot
import statsmodels.api as sm
from random import *
from RFTdt_Database_Queries import dev_graphs
WTTR_dpi03_values, WTTR_dpi05_values, WTTR_dpi07_values, WTTR_dpi09_values, WTTR_dpi12_values, FLXTR_dpi03_values, FLXTR_dpi05_values, FLXTR_dpi07_values, FLXTR_dpi09_values, FLXTR_dpi12_values = dev_graphs('density')

#Calculate Means
WTTR_dpi03_Mean = np.mean(WTTR_dpi03_values)
WTTR_dpi05_Mean = (np.mean(WTTR_dpi05_values))
WTTR_dpi07_Mean = (np.mean(WTTR_dpi07_values))
WTTR_dpi09_Mean = (np.mean(WTTR_dpi09_values))
WTTR_dpi12_Mean = np.mean(WTTR_dpi12_values)
FLXTR_dpi03_Mean = np.mean(FLXTR_dpi03_values)
FLXTR_dpi05_Mean = (np.mean(FLXTR_dpi05_values))
FLXTR_dpi07_Mean = (np.mean(FLXTR_dpi07_values))
FLXTR_dpi09_Mean = (np.mean(FLXTR_dpi09_values))
FLXTR_dpi12_Mean = np.mean(FLXTR_dpi12_values)


#Calculate SEM
WTTR_dpi03_SEM  = np.std(WTTR_dpi03_values,ddof=1) / math.sqrt(len(WTTR_dpi03_values))
WTTR_dpi05_SEM = (np.std(WTTR_dpi05_values,ddof=1) / math.sqrt(len(WTTR_dpi05_values)))
WTTR_dpi07_SEM = (np.std(WTTR_dpi07_values,ddof=1) / math.sqrt(len(WTTR_dpi07_values)))
WTTR_dpi09_SEM = (np.std(WTTR_dpi09_values,ddof=1) / math.sqrt(len(WTTR_dpi09_values)))
WTTR_dpi12_SEM = np.std(WTTR_dpi12_values,ddof=1) / math.sqrt(len(WTTR_dpi12_values))
FLXTR_dpi03_SEM  = np.std(FLXTR_dpi03_values,ddof=1) / math.sqrt(len(FLXTR_dpi03_values))
FLXTR_dpi05_SEM = (np.std(FLXTR_dpi05_values,ddof=1) / math.sqrt(len(FLXTR_dpi05_values)))
FLXTR_dpi07_SEM = (np.std(FLXTR_dpi07_values,ddof=1) / math.sqrt(len(FLXTR_dpi07_values)))
FLXTR_dpi09_SEM = (np.std(FLXTR_dpi09_values,ddof=1) / math.sqrt(len(FLXTR_dpi09_values)))
FLXTR_dpi12_SEM = np.std(FLXTR_dpi12_values,ddof=1) / math.sqrt(len(FLXTR_dpi12_values))


#Make Blank Figure
fig,axs = plot.subplots(nrows=2, ncols=3, sharex=False, sharey='row')

#Plot WT Dev Graph
ax=axs[0,0]
objects = ('WT dpi05', 'WT dpi07', 'WT dpi12')
xvalue = np.arange(len(objects))
yvalue = [WTTR_dpi05_Mean, WTTR_dpi07_Mean, WTTR_dpi12_Mean]
yerr = [WTTR_dpi05_SEM, WTTR_dpi07_SEM, WTTR_dpi12_SEM]

# New_WTTR_dpi03_values = [value for value in WTTR_dpi03_values]
New_WTTR_dpi05_values = [value for value in WTTR_dpi05_values]
New_WTTR_dpi07_values = [value for value in WTTR_dpi07_values]

# WT03_xcoords = []
# WT03_xcoords = [uniform(-0.05,0.05) for value in WTTR_dpi03_values]
# # print WT_xcoords

WT05_xcoords = []
WT05_xcoords = [uniform(-0.05,0.05) for value in WTTR_dpi05_values]
# print WT_xcoords

WT07_xcoords = []
WT07_xcoords = [uniform(0.95,1.05) for value in WTTR_dpi07_values]
# print WT_xcoords

WT12_xcoords = []
WT12_xcoords = [uniform(1.95,2.05) for value in WTTR_dpi12_values]
# print WT_xcoords

# ax.scatter(WT03_xcoords,New_WTTR_dpi03_values, color = '#035069',zorder='3',alpha='0.8',edgecolors='none',s=50)
ax.scatter(WT05_xcoords,New_WTTR_dpi05_values, color = '#035069',zorder='3',alpha='0.8',edgecolors='none',s=50)
ax.scatter(WT07_xcoords,New_WTTR_dpi07_values, color = '#035069',zorder='3',alpha='0.8',edgecolors='none',s=50)
ax.scatter(WT12_xcoords,WTTR_dpi12_values, color = '#035069',zorder='3',alpha='0.8',edgecolors='none',s=50)

ax.bar(xvalue, yvalue, align='center', alpha=1, color=('#838383','#838383','#5b5b5b','#0d0d0d'), linewidth=0)
ax.set_title('WT Development')
ax.errorbar(xvalue,yvalue,yerr,fmt='none',ecolor= '#666666',elinewidth='2',capsize=10,capthick='2')


#Plot KO Dev Graph
ax=axs[0,1]
opacity=1.0

objects = ( 'KO dpi05', 'KO dpi07', 'KO dpi12')
xvalue = np.arange(len(objects))
yvalue = [ FLXTR_dpi05_Mean, FLXTR_dpi07_Mean,FLXTR_dpi12_Mean]
yerr = [ FLXTR_dpi05_SEM, FLXTR_dpi07_SEM, FLXTR_dpi12_SEM]

FLX05_xcoords = []
FLX05_xcoords = [uniform(-0.05,0.05) for value in FLXTR_dpi05_values]
# print FLX_xcoords

FLX07_xcoords = []
FLX07_xcoords = [uniform(0.95,1.05) for value in FLXTR_dpi07_values]
# print FLX_xcoords

FLX12_xcoords = []
FLX12_xcoords = [uniform(1.95,2.05) for value in FLXTR_dpi12_values]
# print FLX_xcoords

New_FLXTR_dpi03_values = [value for value in FLXTR_dpi03_values]
New_FLXTR_dpi05_values = [value for value in FLXTR_dpi05_values]
New_FLXTR_dpi07_values = [value for value in FLXTR_dpi07_values]


ax.scatter(FLX05_xcoords,New_FLXTR_dpi05_values, color = '#035069',zorder='3',alpha='0.8',edgecolors='none',s=50)
ax.scatter(FLX07_xcoords,New_FLXTR_dpi07_values, color = '#035069',zorder='3',alpha='0.8',edgecolors='none',s=50)
ax.scatter(FLX12_xcoords,FLXTR_dpi12_values, color = '#035069',zorder='3',alpha='0.8',edgecolors='none',s=50)

ax.bar(xvalue, yvalue, align='center', alpha=1, color=('#f3e2ae','#eaca6a','#DFB125'), linewidth=0)
ax.set_title('KO Development')
ax.errorbar(xvalue,yvalue,yerr,fmt='none',ecolor= '#666666',elinewidth='2',capsize=10,capthick='2')


#Plot WT + KO Dev Graph
ax=axs[0,2]
group_n = 3
bar_width = 0.35
ax.set_title('WT and KO Development')

xvalue = np.arange(group_n)
wt_yvalue = [WTTR_dpi05_Mean,WTTR_dpi07_Mean,WTTR_dpi12_Mean]
FLX_yvalue = [FLXTR_dpi05_Mean,FLXTR_dpi07_Mean,FLXTR_dpi12_Mean]
wt_yerr =  [WTTR_dpi05_SEM, WTTR_dpi07_SEM,  WTTR_dpi12_SEM]
FLX_yerr = [FLXTR_dpi05_SEM, FLXTR_dpi07_SEM,  FLXTR_dpi12_SEM]

WT05_xcoords = []
WT05_xcoords = [uniform(-0.05,0.05) for value in WTTR_dpi05_values]
# print WT_xcoords

WT07_xcoords = []
WT07_xcoords = [uniform(0.95,1.05) for value in WTTR_dpi07_values]
# print WT_xcoords

WT12_xcoords = []
WT12_xcoords = [uniform(1.95,2.05) for value in WTTR_dpi12_values]
# print WT_xcoords

FLX05_xcoords = []
FLX05_xcoords = [uniform(0.35,0.45) for value in FLXTR_dpi05_values]
# print FLX_xcoords

FLX07_xcoords = []
FLX07_xcoords = [uniform(1.35,1.45) for value in FLXTR_dpi07_values]
# print FLX_xcoords

FLX12_xcoords = []
FLX12_xcoords = [uniform(2.35,2.45) for value in FLXTR_dpi12_values]
# print FLX_xcoords

New_WTTR_dpi05_values = [value for value in WTTR_dpi05_values]
New_WTTR_dpi07_values = [value for value in WTTR_dpi07_values]
New_FLXTR_dpi05_values = [value for value in FLXTR_dpi05_values]
New_FLXTR_dpi07_values = [value for value in FLXTR_dpi07_values]

ax.scatter(WT05_xcoords,New_WTTR_dpi05_values, color = '#035069',zorder='3',alpha='0.8',edgecolors='none',s=50)
ax.scatter(WT07_xcoords,New_WTTR_dpi07_values, color = '#035069',zorder='3',alpha='0.8',edgecolors='none',s=50)
ax.scatter(WT12_xcoords,WTTR_dpi12_values, color = '#035069',zorder='3',alpha='0.8',edgecolors='none',s=50)
ax.scatter(FLX05_xcoords,New_FLXTR_dpi05_values, color = '#035069',zorder='3',alpha='0.8',edgecolors='none',s=50)
ax.scatter(FLX07_xcoords,New_FLXTR_dpi07_values, color = '#035069',zorder='3',alpha='0.8',edgecolors='none',s=50)
ax.scatter(FLX12_xcoords,FLXTR_dpi12_values, color = '#035069',zorder='3',alpha='0.8',edgecolors='none',s=50)



WT_Dev = ax.bar(xvalue, wt_yvalue, bar_width,align='center',color=('#838383','#5b5b5b','#0d0d0d'), linewidth=0)
KO_Dev = ax.bar(xvalue + 0.4, FLX_yvalue, bar_width, align='center', color=('#f3e2ae','#eaca6a','#DFB125'), linewidth=0)
ax.errorbar(xvalue, wt_yvalue,wt_yerr,fmt='none',ecolor= '#666666',elinewidth='2',capsize=5,capthick='2')
ax.errorbar(xvalue+0.4, FLX_yvalue,FLX_yerr,fmt='none',ecolor= '#666666',elinewidth='2',capsize=5,capthick='2')



# #plot WT development ECDF
# ax =axs[1,0]
#
# ecdf1 = sm.distributions.ECDF(WTTR_dpi03_values)
# ecdf2 = sm.distributions.ECDF(WTTR_dpi05_values)
# ecdf3 = sm.distributions.ECDF(WTTR_dpi07_values)
# ecdf4 = sm.distributions.ECDF(WTTR_dpi09_values)
# ecdf5= sm.distributions.ECDF(WTTR_dpi12_values)
#
# dpi03 = np.linspace(min(WTTR_dpi03_values), max(WTTR_dpi03_values))
# dpi05 = np.linspace(min(WTTR_dpi05_values), max(WTTR_dpi05_values))
# dpi07 = np.linspace(min(WTTR_dpi07_values), max(WTTR_dpi07_values))
# dpi09 = np.linspace(min(WTTR_dpi09_values), max(WTTR_dpi09_values))
# dpi12 = np.linspace(min(WTTR_dpi12_values), max(WTTR_dpi12_values))
#
# dpi03_ecdf = ecdf1(dpi03)
# dpi05_ecdf = ecdf2(dpi05)
# dpi07_ecdf = ecdf3(dpi07)
# dpi09_ecdf = ecdf4(dpi09)
# dpi12_ecdf = ecdf5(dpi12)
#
# ax.step(dpi03,dpi03_ecdf, color= '#b4b4b4', linewidth=2.0)
# ax.step(dpi05,dpi05_ecdf, color = '#838383', linewidth=2.0)
# ax.step(dpi07,dpi07_ecdf, color = '#5b5b5b', linewidth=2.0)
# ax.step(dpi09,dpi09_ecdf, color = '#343434', linewidth=2.0)
# ax.step(dpi12,dpi12_ecdf, color = '#0d0d0d', linewidth=2.0)
#
#
# #plot KO development ECDF
# ax =axs[1,1]
#
# ecdf1 = sm.distributions.ECDF(FLXTR_dpi03_values)
# ecdf2 = sm.distributions.ECDF(FLXTR_dpi05_values)
# ecdf3 = sm.distributions.ECDF(FLXTR_dpi07_values)
# ecdf4 = sm.distributions.ECDF(FLXTR_dpi09_values)
# ecdf5 = sm.distributions.ECDF(FLXTR_dpi12_values)
#
# dpi03 = np.linspace(min(FLXTR_dpi03_values), max(FLXTR_dpi03_values))
# dpi05 = np.linspace(min(FLXTR_dpi05_values), max(FLXTR_dpi05_values))
# dpi07 = np.linspace(min(FLXTR_dpi07_values), max(FLXTR_dpi07_values))
# dpi09 = np.linspace(min(FLXTR_dpi09_values), max(FLXTR_dpi09_values))
# dpi12 = np.linspace(min(FLXTR_dpi12_values), max(FLXTR_dpi12_values))
#
# dpi03_ecdf = ecdf1(dpi03)
# dpi05_ecdf = ecdf2(dpi05)
# dpi07_ecdf = ecdf3(dpi07)
# dpi09_ecdf = ecdf4(dpi09)
# dpi12_ecdf = ecdf5(dpi12)
#
# ax.step(dpi03,dpi03_ecdf, color= '#ccdce1',linewidth=2.0)
# ax.step(dpi05,dpi05_ecdf, color = '#81a7b4',linewidth=2.0)
# ax.step(dpi07,dpi07_ecdf, color = '#357287',linewidth=2.0)
# ax.step(dpi09,dpi09_ecdf, color = '#035069',linewidth=2.0)
# ax.step(dpi12,dpi12_ecdf, color = '#023849',linewidth=2.0)
#
#
# #Plot WT + KO ECDF
# ax =axs[1,2]
#
# ecdf1 = sm.distributions.ECDF(WTTR_dpi03_values)
# ecdf2 = sm.distributions.ECDF(WTTR_dpi05_values)
# ecdf3 = sm.distributions.ECDF(WTTR_dpi07_values)
# ecdf4 = sm.distributions.ECDF(WTTR_dpi09_values)
# ecdf5= sm.distributions.ECDF(WTTR_dpi12_values)
# ecdf6 = sm.distributions.ECDF(FLXTR_dpi03_values)
# ecdf7 = sm.distributions.ECDF(FLXTR_dpi05_values)
# ecdf8 = sm.distributions.ECDF(FLXTR_dpi07_values)
# ecdf9 = sm.distributions.ECDF(FLXTR_dpi09_values)
# ecdf10 = sm.distributions.ECDF(FLXTR_dpi12_values)
#
# wtdpi03 = np.linspace(min(WTTR_dpi03_values), max(WTTR_dpi03_values))
# wtdpi05 = np.linspace(min(WTTR_dpi05_values), max(WTTR_dpi05_values))
# wtdpi07 = np.linspace(min(WTTR_dpi07_values), max(WTTR_dpi07_values))
# wtdpi09 = np.linspace(min(WTTR_dpi09_values), max(WTTR_dpi09_values))
# wtdpi12 = np.linspace(min(WTTR_dpi12_values), max(WTTR_dpi12_values))
# FLXdpi03 = np.linspace(min(FLXTR_dpi03_values), max(FLXTR_dpi03_values))
# FLXdpi05 = np.linspace(min(FLXTR_dpi05_values), max(FLXTR_dpi05_values))
# FLXdpi07 = np.linspace(min(FLXTR_dpi07_values), max(FLXTR_dpi07_values))
# FLXdpi09 = np.linspace(min(FLXTR_dpi09_values), max(FLXTR_dpi09_values))
# FLXdpi12 = np.linspace(min(FLXTR_dpi12_values), max(FLXTR_dpi12_values))
#
# wtdpi03_ecdf = ecdf1(wtdpi03)
# wtdpi05_ecdf = ecdf2(wtdpi05)
# wtdpi07_ecdf = ecdf3(wtdpi07)
# wtdpi09_ecdf = ecdf4(wtdpi09)
# wtdpi12_ecdf = ecdf5(wtdpi12)
# FLXdpi03_ecdf = ecdf6(FLXdpi03)
# FLXdpi05_ecdf = ecdf7(FLXdpi05)
# FLXdpi07_ecdf = ecdf8(FLXdpi07)
# FLXdpi09_ecdf = ecdf9(FLXdpi09)
# FLXdpi12_ecdf = ecdf10(FLXdpi12)
#
# ax.step(wtdpi03,wtdpi03_ecdf, color= '#b4b4b4', linewidth=2.0)
# ax.step(wtdpi05,wtdpi05_ecdf, color = '#838383', linewidth=2.0)
# ax.step(wtdpi07,wtdpi07_ecdf, color = '#5b5b5b', linewidth=2.0)
# ax.step(wtdpi09,wtdpi09_ecdf, color = '#343434', linewidth=2.0)
# ax.step(wtdpi12,wtdpi12_ecdf, color = '#0d0d0d', linewidth=2.0)
# ax.step(FLXdpi03,FLXdpi03_ecdf, color= '#ccdce1',linewidth=2.0)
# ax.step(FLXdpi05,FLXdpi05_ecdf, color = '#81a7b4',linewidth=2.0)
# ax.step(FLXdpi07,FLXdpi07_ecdf, color = '#357287',linewidth=2.0)
# ax.step(FLXdpi09,FLXdpi09_ecdf, color = '#035069',linewidth=2.0)
# ax.step(FLXdpi12,FLXdpi12_ecdf, color = '#023849',linewidth=2.0)

plot.show()