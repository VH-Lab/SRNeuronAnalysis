# import os
# import xml.etree.ElementTree as ET
# import glob
# filelocation=raw_input("Input annotation file location.")
# os.chdir(filelocation)
# annotationfiles=glob.glob(filelocation + "\*.xml")
# print annotationfiles
# tree = ET.parse(annotationfiles[0])
# root = tree.getroot()
# nodes = list(root.iter('node'))
# edges = list(root.iter('edge'))
# print root
# node_list=[[node.attrib] for node in nodes]
# edge_list=[[edge.attrib] for edge in edges]
# print node_list
# radii_list=[[node.attrib['radius']] for node in nodes]
# print radii_list
# soma_diameter = max(radii_list)
# print soma_diameter
# print edge_list
# source_list = [[edge.attrib['source']] for edge in edges]
# print source_list
# print source_list.count(['1'])


# from AnnotationReaderXML import *
# annotation_files = annotation_finder('C:\Users\Sarah\Desktop\Annotations\AlreadyAdded')
#
# for annotation_file in annotation_files:
#     # nodes,edges = annotation_parser(annotation_file)
#     # print nodes
#     #
#     # print 'soma size:'
#     # print soma_size(nodes,edges)
#     #
#     # print 'tree number:'
#     # print tree_number(nodes,edges)
#     #
#     # print 'branch number:'
#     # print branch_number(edges)
#     #
#     # print 'tip number:'
#     # print tip_number(nodes,edges)
#
#     print annotation_file[-29:-23]
#
#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
#
# # example data
# x = np.arange(0.1, 4, 0.5)
# y = np.exp(-x)
#
# # example variable error bar values
# yerr = 0.1 + 0.2*np.sqrt(x)
# xerr = 0.1 + yerr
# #
# # # First illustrate basic pyplot interface, using defaults where possible.
# # plt.figure()
# # plt.errorbar(x, y, xerr=0.2, yerr=0.4)
# # plt.title("Simplest errorbars, 0.2 in x, 0.4 in y")
#
# # Now switch to a more OO interface to exercise more features.
# fig, axs = plt.subplots(nrows=2, ncols=2, sharex=True)
# ax = axs[0,0]
# ax.errorbar(x, y, yerr=yerr, fmt='o')
# ax.set_title('Vert. symmetric')
#
# # With 4 subplots, reduce the number of axis ticks to avoid crowding.
# ax.locator_params(nbins=4)
#
# ax = axs[0,1]
# ax.errorbar(x, y, xerr=xerr, fmt='o')
# ax.set_title('Hor. symmetric')
#
# ax = axs[1,0]
# ax.errorbar(x, y, yerr=[yerr, 2*yerr], xerr=[xerr, 2*xerr], fmt='--o')
# ax.set_title('H, V asymmetric')
#
# ax = axs[1,1]
# ax.set_yscale('log')
# # Here we have to be careful to keep all y values positive:
# ylower = np.maximum(1e-2, y - yerr)
# yerr_lower = y - ylower
#
# ax.errorbar(x, y, yerr=[yerr_lower, 2*yerr], xerr=xerr,
#             fmt='o', ecolor='g', capthick=2)
# ax.set_title('Mixed sym., log y')
#
# fig.suptitle('Variable errorbars')
#
# plt.show()

# fake up some data
#

# import matplotlib.pyplot as plt
# import numpy as np
#
# data = [np.random.normal(0, std, 1000) for std in range(1, 6)]
# plt.boxplot(data, notch=True, patch_artist=True)
#
# plt.show()
#

# import matplotlib.pyplot as plt
# import numpy as np
#
# data = [np.random.normal(0, std, 1000) for std in range(1, 6)]
#
# box = plt.boxplot(data, notch=True, patch_artist=True)
#
# colors = ['cyan', 'lightblue', 'lightgreen', 'tan', 'pink']
# for patch, color in zip(box['boxes'], colors):
#     patch.set_facecolor(color)
#
# print box['boxes']
#
# plt.show()
#
#

import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plot

# sample = np.random.uniform(0, 1, 50)
# ecdf = sm.distributions.ECDF(sample)
#
# x = np.linspace(min(sample), max(sample))
# y = ecdf(x)
# plot.step(x, y)
# plot.show()

a = np.random.uniform(0, 20, 80)
sorted_ = np.sort(a)
yvals = np.arange(len(sorted_))/float(len(sorted_))
plot.plot(sorted_, yvals)

np.concatenate((wt_spread, wt_center, wt_flier_high, wt_flier_low),0)