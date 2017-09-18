import matplotlib.pyplot as plot;plot.rcdefaults()
import numpy as np
import matplotlib.pyplot as plot
import random
import statsmodels.api as sm
from Database_Queries import summary_graphs
WTTR_values,WTDD_values,KOTR_values,KODD_values,WTTRM_values,WTTRF_values,WTDDM_values,WTDDF_values,KOTRM_values,KOTRF_values,KODDM_values,KODDF_values = summary_graphs('P21','tip_number')


fig,axs = plot.subplots(nrows=2, ncols=3, sharex=False)

#Plot WT/KO graph
ax =axs[0,0]

bins = np.linspace(0, 100, 50)


ax.hist(WTTR_values, bins, normed=1, alpha=0.5, label='WT TR',color='#0d0d0d')
ax.hist(KOTR_values, bins, normed=1, alpha=0.5, label='KO TR',color='#035069')
ax.legend(loc='upper right')

#Plot WT/KO * TR DR graph
ax =axs[0,1]

bins = np.linspace(0,100, 50)

ax.hist(WTTR_values, bins, normed=1,alpha=0.5, label='WT TR',color='#0d0d0d')
ax.hist(WTDD_values, bins, normed=1,alpha=0.5, label='KO TR',color='#035069')
ax.hist(KOTR_values, bins, normed=1,alpha=0.5, label='WT DR',color='#878787')
ax.hist(KODD_values, bins, normed=1,alpha=0.5, label='KO DR',color='#3D9CBC')

ax.legend(loc='upper right')

#plot geno*dep*sex graph
ax =axs[0,2]

bins = np.linspace(0, 100, 50)

ax.hist(WTTRM_values, bins, normed=1, alpha=0.5, label='WT TR M')
ax.hist(WTTRF_values, bins, normed=1, alpha=0.5, label='WT TR F')
ax.hist(WTDDM_values, bins, normed=1, alpha=0.5, label='KO TR M ')
ax.hist(WTDDF_values, bins, normed=1, alpha=0.5, label='KO TR F')
ax.hist(KOTRM_values, bins, normed=1, alpha=0.5, label='WT DR M')
ax.hist(KOTRF_values, bins, normed=1, alpha=0.5, label='WT DR F')
ax.hist(KODDM_values, bins, normed=1, alpha=0.5, label='KO DR M')
ax.hist(KODDF_values, bins, normed=1, alpha=0.5, label='KO DR F')
ax.legend(loc='upper right')


#plot WT vs KO eCDFs
ax =axs[1,0]
ecdf1 = sm.distributions.ECDF(WTTR_values)
ecdf2 = sm.distributions.ECDF(KOTR_values)

x = np.linspace(min(WTTR_values), max(WTTR_values))
z = np.linspace(min(KOTR_values), max(KOTR_values))
y = ecdf1(x)
q = ecdf2(z)
ax.step(x,y, color= '#0d0d0d',linewidth=2.0)
ax.step(z,q, color = '#035069', linewidth=2.0)


#plot Geno*Condition eCDFs
ax =axs[1,1]

ecdf1 = sm.distributions.ECDF(WTTR_values)
ecdf2 = sm.distributions.ECDF(WTDD_values)
ecdf3 = sm.distributions.ECDF(KOTR_values)
ecdf4 = sm.distributions.ECDF(KODD_values)

w = np.linspace(min(WTTR_values), max(WTTR_values))
x = np.linspace(min(WTDD_values), max(WTDD_values))
y = np.linspace(min(KOTR_values), max(KOTR_values))
z = np.linspace(min(KODD_values), max(KODD_values))


a = ecdf1(w)
b = ecdf2(x)
c= ecdf3(y)
d = ecdf4(z)

ax.step(w,a, color= '#0d0d0d',linewidth=2.0)
ax.step(x,b, color = '#878787',linewidth=2.0)
ax.step(y,c, color = '#035069',linewidth=2.0)
ax.step(z,d, color = '#3D9CBC',linewidth=2.0)


#plot Geno*Condition*Sex eCDFs
ax =axs[1,2]

ecdf1 = sm.distributions.ECDF(WTTRM_values)
ecdf2 = sm.distributions.ECDF(WTTRF_values)
ecdf3 = sm.distributions.ECDF(WTDDM_values)
ecdf4 = sm.distributions.ECDF(WTDDF_values)
ecdf5 = sm.distributions.ECDF(KOTRM_values)
ecdf6 = sm.distributions.ECDF(KOTRF_values)
ecdf7 = sm.distributions.ECDF(KODDM_values)
ecdf8 = sm.distributions.ECDF(KODDF_values)

w = np.linspace(min(WTTRM_values), max(WTTRM_values))
ww = np.linspace(min(WTTRF_values), max(WTTRF_values))
x = np.linspace(min(WTDDM_values), max(WTDDM_values))
xx = np.linspace(min(WTDDF_values), max(WTDDF_values))
y = np.linspace(min(KOTRM_values), max(KOTRM_values))
yy = np.linspace(min(KOTRF_values), max(KOTRF_values))
z = np.linspace(min(KODDM_values), max(KODDM_values))
zz = np.linspace(min(KODDF_values), max(KODDF_values))

a = ecdf1(w)
aa = ecdf1(ww)
b = ecdf2(x)
bb = ecdf2(xx)
c= ecdf3(y)
cc= ecdf3(yy)
d = ecdf4(z)
dd = ecdf4(zz)

ax.step(w,a , color= '#0d0d0d', linewidth=2.0)
ax.step(ww,aa, color= '#0d0d0d', linewidth=4.0, linestyle='dashed')
ax.step(x,b, color = '#878787', linewidth=2.0)
ax.step(xx,bb, color = '#878787', linewidth=2.0, linestyle='dashed')
ax.step(y,c, color = '#035069',linewidth=2.0)
ax.step(yy,cc, color = '#035069', linewidth=2.0, linestyle='dashed')
ax.step(z,d, color = '#3D9CBC', linewidth=2.0)
ax.step(zz,dd, color = '#3D9CBC', linewidth=2.0, linestyle='dashed')


plot.show()


