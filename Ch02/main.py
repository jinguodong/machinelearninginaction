import kNN
datingDataMat,datingLabels = kNN.file2matrix('datingTestSet.txt')
normMat, ranges, minVals = kNN.autoNorm(datingDataMat)
import matplotlib
import matplotlib.pyplot as plt
fit = plt.figure()
ax = fit.add_subplot(111)
from numpy import *
ax.scatter(normMat[:,0], normMat[:,1],15.0*array(datingLabels), 15.0*array(datingLabels))
plt.show()