'''
Created on May 27, 2014
Logistic Regression Main Study
@author: Guodong Jin
'''

import logRegres
from numpy import *
dataArr,labelMat = logRegres.loadDataSet()
print len(dataArr)
print labelMat

res_w = logRegres.gradAscent(dataArr, labelMat)

print res_w

# logRegres.plotBestFit(res_w.getA())

res_w, l_w0, l_w1, l_w2= logRegres.stocGradAscent1_0(array(dataArr), labelMat, 100)
logRegres.plotBestFit(res_w)
# import matplotlib.pyplot as plt
# x = range(len(l_w0))
# fig = plt.figure()
# ax = fig.add_subplot(111)
# print res_w
# ax.plot(x, array(l_w1))
# plt.show()

