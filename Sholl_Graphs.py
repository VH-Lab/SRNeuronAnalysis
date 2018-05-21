import matplotlib.pyplot as plot;plot.rcdefaults()
import numpy as np
import matplotlib.pyplot as plot
import math
from scipy import stats
from Database_Queries import sholl_values

WTTR_values, KOTR_values, WTDD_values, KODD_values= sholl_values('P21','sholl')

WTTR_Matrix = np.matrix(WTTR_values)
WTTR_SEM = stats.sem(WTTR_Matrix)
WTTR_SEM = WTTR_SEM.tolist()

WTDD_Matrix = np.matrix(WTDD_values)
WTDD_SEM = stats.sem(WTDD_Matrix)
WTDD_SEM = WTDD_SEM.tolist()

KOTR_Matrix = np.matrix(KOTR_values)
KOTR_SEM = stats.sem(KOTR_Matrix)
KOTR_SEM = KOTR_SEM.tolist()

KODD_Matrix = np.matrix(KODD_values)
KODD_SEM = stats.sem(KODD_Matrix)
KODD_SEM = KODD_SEM.tolist()

WTTR_values = [np.array(sholl_intersections) for sholl_intersections in WTTR_values]
WTTR_values_summed = np.zeros(shape = (1,50))
for sholl_intersection_array in WTTR_values:
    WTTR_values_summed = WTTR_values_summed + sholl_intersection_array
# print WTTR_values_summed
WTTR_Mean = np.divide(WTTR_values_summed, len(WTTR_values))
WTTR_Mean = WTTR_Mean.tolist()
print WTTR_Mean

WTDD_values = [np.array(sholl_intersections) for sholl_intersections in WTDD_values]
WTDD_values_summed = np.zeros(shape = (1,50))
for sholl_intersection_array in WTDD_values:
    WTDD_values_summed = WTDD_values_summed + sholl_intersection_array
# print WTDD_values_summed
WTDD_Mean = np.divide(WTDD_values_summed, len(WTDD_values))
WTDD_Mean = WTDD_Mean.tolist()
# print WTDD_Mean

KOTR_values = [np.array(sholl_intersections) for sholl_intersections in KOTR_values]
KOTR_values_summed = np.zeros(shape = (1,50))
for sholl_intersection_array in KOTR_values:
    KOTR_values_summed = KOTR_values_summed + sholl_intersection_array
# print KOTR_values_summed
KOTR_Mean = np.divide(KOTR_values_summed, len(KOTR_values))
KOTR_Mean = KOTR_Mean.tolist()
# print KOTR_Mean

KODD_values = [np.array(sholl_intersections) for sholl_intersections in KODD_values]
KODD_values_summed = np.zeros(shape = (1,50))
for sholl_intersection_array in KODD_values:
    KODD_values_summed = KODD_values_summed + sholl_intersection_array
# print KODD_values_summed
KODD_Mean = np.divide(KODD_values_summed, len(KODD_values))
KODD_Mean = KODD_Mean.tolist()
# print KODD_Mean



fig,axs = plot.subplots(nrows=1, ncols=2, sharex=False)

#WT vs KO Sholl
ax =axs[0]

xvalue = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 340, 350, 360, 370, 380, 390, 400, 410, 420, 430, 440, 450, 460, 470, 480, 490, 500]
WT_yvalue = WTTR_Mean[0]
KO_yvalue = KOTR_Mean[0]

ax.plot(xvalue, WT_yvalue, 'o', color = '#0d0d0d', ms='10')
ax.errorbar(xvalue, WT_yvalue, WTTR_SEM, fmt = '#0d0d0d', linewidth = '3', ecolor='#666666', elinewidth='2', capsize=10, capthick='2')
ax.plot(xvalue,KO_yvalue,'o', color = '#035069', ms='10')
ax.errorbar(xvalue, KO_yvalue, KOTR_SEM, fmt = '#035069', linewidth = '3', ecolor='#666666', elinewidth='2', capsize=10, capthick='2')

ax.set_ylabel('Metric')
ax.set_title('WT vs. KO')


#
#Geno * Dep Sholl
ax = axs[1]

xvalue = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 340, 350, 360, 370, 380, 390, 400, 410, 420, 430, 440, 450, 460, 470, 480, 490, 500]
WTTR_yvalue = WTTR_Mean[0]
KOTR_yvalue = KOTR_Mean[0]
WTDD_yvalue = WTDD_Mean[0]
KODD_yvalue = KODD_Mean[0]

ax.plot(xvalue, WTTR_yvalue, 'o', color = '#0d0d0d', ms='10')
ax.errorbar(xvalue, WTTR_yvalue, WTTR_SEM, fmt = '#0d0d0d', linewidth = '3', ecolor='#666666', elinewidth='2', capsize=10, capthick='2')
ax.plot(xvalue,KOTR_yvalue,'o', color = '#035069', ms='10')
ax.errorbar(xvalue, KOTR_yvalue, KOTR_SEM, fmt = '#035069', linewidth = '3', ecolor='#666666', elinewidth='2', capsize=10, capthick='2')
ax.plot(xvalue, WTDD_yvalue, 'o', color = '#878787', ms='10')
ax.errorbar(xvalue, WTDD_yvalue, WTDD_SEM, fmt = '#878787', linewidth = '3', ecolor='#666666', elinewidth='2', capsize=10, capthick='2')
ax.plot(xvalue,KODD_yvalue,'o', color = '#3D9CBC', ms='10')
ax.errorbar(xvalue, KODD_yvalue, KODD_SEM, fmt = '#3D9CBC', linewidth = '3', ecolor='#666666', elinewidth='2', capsize=10, capthick='2')

ax.set_ylabel('Metric')
ax.set_title('Geno*Dep')



plot.show()