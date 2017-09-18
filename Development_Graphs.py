import math
import matplotlib.pyplot as plot;plot.rcdefaults()
import numpy as np
import matplotlib.pyplot as plot
import statsmodels.api as sm
from Database_Queries import dev_graphs
WTTR_P7_values, WTTR_P12_values, WTTR_P16_values, WTTR_P21_values, WTTR_P30_values, KOTR_P7_values, KOTR_P12_values, KOTR_P16_values, KOTR_P21_values, KOTR_P30_values = dev_graphs('branch_number')

#Calculate Means
WTTR_P7_Mean = np.mean(WTTR_P7_values)
WTTR_P12_Mean = np.mean(WTTR_P12_values)
WTTR_P16_Mean = np.mean(WTTR_P16_values)
WTTR_P21_Mean = np.mean(WTTR_P21_values)
WTTR_P30_Mean = np.mean(WTTR_P30_values)
KOTR_P7_Mean = np.mean(KOTR_P7_values)
KOTR_P12_Mean = np.mean(KOTR_P12_values)
KOTR_P16_Mean = np.mean(KOTR_P16_values)
KOTR_P21_Mean = np.mean(KOTR_P21_values)
KOTR_P30_Mean = np.mean(KOTR_P30_values)


#Calculate SEM
WTTR_P7_SEM  = np.std(WTTR_P7_values,ddof=1) / math.sqrt(len(WTTR_P7_values))
WTTR_P12_SEM = np.std(WTTR_P12_values,ddof=1) / math.sqrt(len(WTTR_P12_values))
WTTR_P16_SEM = np.std(WTTR_P16_values,ddof=1) / math.sqrt(len(WTTR_P16_values))
WTTR_P21_SEM = np.std(WTTR_P21_values,ddof=1) / math.sqrt(len(WTTR_P21_values))
WTTR_P30_SEM = np.std(WTTR_P30_values,ddof=1) / math.sqrt(len(WTTR_P30_values))
KOTR_P7_SEM  = np.std(KOTR_P7_values,ddof=1) / math.sqrt(len(KOTR_P7_values))
KOTR_P12_SEM = np.std(KOTR_P12_values,ddof=1) / math.sqrt(len(KOTR_P12_values))
KOTR_P16_SEM = np.std(KOTR_P16_values,ddof=1) / math.sqrt(len(KOTR_P16_values))
KOTR_P21_SEM = np.std(KOTR_P21_values,ddof=1) / math.sqrt(len(KOTR_P21_values))
KOTR_P30_SEM = np.std(KOTR_P30_values,ddof=1) / math.sqrt(len(KOTR_P30_values))


#Make Blank Figure
fig,axs = plot.subplots(nrows=2, ncols=3, sharex=False, sharey='row')

#Plot WT Dev Graph
ax=axs[0,0]
objects = ('WT P7', 'WT P12', 'WT P16', 'WT P21', 'WT P30')
xvalue = np.arange(len(objects))
yvalue = [WTTR_P7_Mean, WTTR_P12_Mean, WTTR_P16_Mean,WTTR_P21_Mean, WTTR_P30_Mean]
yerr = [WTTR_P7_SEM, WTTR_P12_SEM, WTTR_P16_SEM, WTTR_P21_SEM, WTTR_P30_SEM]

ax.bar(xvalue, yvalue, align='center', alpha=1, color=('#b4b4b4','#838383','#5b5b5b','#343434','#0d0d0d'), linewidth=0)
ax.set_title('WT Development')
ax.errorbar(xvalue,yvalue,yerr,fmt='none',ecolor= '#666666',elinewidth='2',capsize=10,capthick='2')


#Plot KO Dev Graph
ax=axs[0,1]
opacity=1.0

objects = ('KO P7', 'KO P12', 'KO P16', 'KO P21', 'KO P30')
xvalue = np.arange(len(objects))
yvalue = [KOTR_P7_Mean, KOTR_P12_Mean, KOTR_P16_Mean, KOTR_P21_Mean, KOTR_P30_Mean]
yerr = [KOTR_P7_SEM, KOTR_P12_SEM, KOTR_P16_SEM, KOTR_P21_SEM, KOTR_P30_SEM]

ax.bar(xvalue, yvalue, align='center', alpha=1, color=('#ccdce1','#81a7b4','#357287','#035069','#023849'), linewidth=0)
ax.set_title('KO Development')
ax.errorbar(xvalue,yvalue,yerr,fmt='none',ecolor= '#666666',elinewidth='2',capsize=10,capthick='2')


#Plot WT + KO Dev Graph
ax=axs[0,2]
group_n = 5
bar_width = 0.35
ax.set_title('WT and KO Development')

xvalue = np.arange(group_n)
wt_yvalue = [WTTR_P7_Mean,WTTR_P12_Mean,WTTR_P16_Mean,WTTR_P21_Mean,WTTR_P30_Mean]
ko_yvalue = [KOTR_P7_Mean,KOTR_P12_Mean,KOTR_P16_Mean,KOTR_P21_Mean,KOTR_P30_Mean]
wt_yerr =  [WTTR_P7_SEM, WTTR_P12_SEM, WTTR_P16_SEM, WTTR_P21_SEM, WTTR_P30_SEM]
ko_yerr = [KOTR_P7_SEM, KOTR_P12_SEM, KOTR_P16_SEM, KOTR_P21_SEM, KOTR_P30_SEM]


WT_Dev = ax.bar(xvalue, wt_yvalue, bar_width,align='center',color=('#b4b4b4','#838383','#5b5b5b','#343434','#0d0d0d'), linewidth=0)
KO_Dev = ax.bar(xvalue + 0.4, ko_yvalue, bar_width, align='center', color=('#ccdce1','#81a7b4','#357287','#035069','#023849'), linewidth=0)
ax.errorbar(xvalue, wt_yvalue,wt_yerr,fmt='none',ecolor= '#666666',elinewidth='2',capsize=5,capthick='2')
ax.errorbar(xvalue+0.4, ko_yvalue,ko_yerr,fmt='none',ecolor= '#666666',elinewidth='2',capsize=5,capthick='2')



#plot WT development ECDF
ax =axs[1,0]

ecdf1 = sm.distributions.ECDF(WTTR_P7_values)
ecdf2 = sm.distributions.ECDF(WTTR_P12_values)
ecdf3 = sm.distributions.ECDF(WTTR_P16_values)
ecdf4 = sm.distributions.ECDF(WTTR_P21_values)
ecdf5= sm.distributions.ECDF(WTTR_P30_values)

p7 = np.linspace(min(WTTR_P7_values), max(WTTR_P7_values))
p12 = np.linspace(min(WTTR_P12_values), max(WTTR_P12_values))
p16 = np.linspace(min(WTTR_P16_values), max(WTTR_P16_values))
p21 = np.linspace(min(WTTR_P21_values), max(WTTR_P21_values))
p30 = np.linspace(min(WTTR_P30_values), max(WTTR_P30_values))

p7_ecdf = ecdf1(p7)
p12_ecdf = ecdf2(p12)
p16_ecdf = ecdf3(p16)
p21_ecdf = ecdf4(p21)
p30_ecdf = ecdf5(p30)

ax.step(p7,p7_ecdf, color= '#b4b4b4', linewidth=2.0)
ax.step(p12,p12_ecdf, color = '#838383', linewidth=2.0)
ax.step(p16,p16_ecdf, color = '#5b5b5b', linewidth=2.0)
ax.step(p21,p21_ecdf, color = '#343434', linewidth=2.0)
ax.step(p30,p30_ecdf, color = '#0d0d0d', linewidth=2.0)


#plot KO development ECDF
ax =axs[1,1]

ecdf1 = sm.distributions.ECDF(KOTR_P7_values)
ecdf2 = sm.distributions.ECDF(KOTR_P12_values)
ecdf3 = sm.distributions.ECDF(KOTR_P16_values)
ecdf4 = sm.distributions.ECDF(KOTR_P21_values)
ecdf5 = sm.distributions.ECDF(KOTR_P30_values)

p7 = np.linspace(min(KOTR_P7_values), max(KOTR_P7_values))
p12 = np.linspace(min(KOTR_P12_values), max(KOTR_P12_values))
p16 = np.linspace(min(KOTR_P16_values), max(KOTR_P16_values))
p21 = np.linspace(min(KOTR_P21_values), max(KOTR_P21_values))
p30 = np.linspace(min(KOTR_P30_values), max(KOTR_P30_values))

p7_ecdf = ecdf1(p7)
p12_ecdf = ecdf2(p12)
p16_ecdf = ecdf3(p16)
p21_ecdf = ecdf4(p21)
p30_ecdf = ecdf5(p30)

ax.step(p7,p7_ecdf, color= '#ccdce1',linewidth=2.0)
ax.step(p12,p12_ecdf, color = '#81a7b4',linewidth=2.0)
ax.step(p16,p16_ecdf, color = '#357287',linewidth=2.0)
ax.step(p21,p21_ecdf, color = '#035069',linewidth=2.0)
ax.step(p30,p30_ecdf, color = '#023849',linewidth=2.0)


#Plot WT + KO ECDF
ax =axs[1,2]

ecdf1 = sm.distributions.ECDF(WTTR_P7_values)
ecdf2 = sm.distributions.ECDF(WTTR_P12_values)
ecdf3 = sm.distributions.ECDF(WTTR_P16_values)
ecdf4 = sm.distributions.ECDF(WTTR_P21_values)
ecdf5= sm.distributions.ECDF(WTTR_P30_values)
ecdf6 = sm.distributions.ECDF(KOTR_P7_values)
ecdf7 = sm.distributions.ECDF(KOTR_P12_values)
ecdf8 = sm.distributions.ECDF(KOTR_P16_values)
ecdf9 = sm.distributions.ECDF(KOTR_P21_values)
ecdf10 = sm.distributions.ECDF(KOTR_P30_values)

wtp7 = np.linspace(min(WTTR_P7_values), max(WTTR_P7_values))
wtp12 = np.linspace(min(WTTR_P12_values), max(WTTR_P12_values))
wtp16 = np.linspace(min(WTTR_P16_values), max(WTTR_P16_values))
wtp21 = np.linspace(min(WTTR_P21_values), max(WTTR_P21_values))
wtp30 = np.linspace(min(WTTR_P30_values), max(WTTR_P30_values))
kop7 = np.linspace(min(KOTR_P7_values), max(KOTR_P7_values))
kop12 = np.linspace(min(KOTR_P12_values), max(KOTR_P12_values))
kop16 = np.linspace(min(KOTR_P16_values), max(KOTR_P16_values))
kop21 = np.linspace(min(KOTR_P21_values), max(KOTR_P21_values))
kop30 = np.linspace(min(KOTR_P30_values), max(KOTR_P30_values))

wtp7_ecdf = ecdf1(wtp7)
wtp12_ecdf = ecdf2(wtp12)
wtp16_ecdf = ecdf3(wtp16)
wtp21_ecdf = ecdf4(wtp21)
wtp30_ecdf = ecdf5(wtp30)
kop7_ecdf = ecdf6(kop7)
kop12_ecdf = ecdf7(kop12)
kop16_ecdf = ecdf8(kop16)
kop21_ecdf = ecdf9(kop21)
kop30_ecdf = ecdf10(kop30)

ax.step(wtp7,wtp7_ecdf, color= '#b4b4b4', linewidth=2.0)
ax.step(wtp12,wtp12_ecdf, color = '#838383', linewidth=2.0)
ax.step(wtp16,wtp16_ecdf, color = '#5b5b5b', linewidth=2.0)
ax.step(wtp21,wtp21_ecdf, color = '#343434', linewidth=2.0)
ax.step(wtp30,wtp30_ecdf, color = '#0d0d0d', linewidth=2.0)
ax.step(kop7,kop7_ecdf, color= '#ccdce1',linewidth=2.0)
ax.step(kop12,kop12_ecdf, color = '#81a7b4',linewidth=2.0)
ax.step(kop16,kop16_ecdf, color = '#357287',linewidth=2.0)
ax.step(kop21,kop21_ecdf, color = '#035069',linewidth=2.0)
ax.step(kop30,kop30_ecdf, color = '#023849',linewidth=2.0)

plot.show()