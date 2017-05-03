import cPickle
import numpy as np
from scipy.signal import argrelextrema
import matplotlib.pyplot as plt
from matplotlib import style

style.use('fivethirtyeight')
fig = plt.figure()
ax1 = fig.add_subplot(2,1,1)
ax2 = fig.add_subplot(2,1,2)
#ax3 = fig.add_subplot(2,1,3)

x = cPickle.load(open('s01.dat', 'rb'))
labels = x["labels"]
data = x["data"]
GSR = data[1,36,:] #1 for first video/trial and 37 for GSR channel
PPG = data[1,38,:] #39 for PPG channel
print PPG[100]
#PPG = np.reshape(PPG, (-1,1))
diffPPG = np.diff(PPG)
#diffPPG.append(0)
axes_x = range(0, 8064)

# ax1.plot(axes_x, GSR)
# #axes_x = range(0, 8063)
# ax2.plot(axes_x, PPG)
# #axes_x = range(0, 8062)
# #ax3.plot(axes_x, np.diff(diffPPG))
# plt.show()

##---------------------------- GSR Variables ------------------------------------##
###################################################################################
avGSR = np.average(GSR)
print "Average: ", avGSR
diffGSR = np.diff(GSR)
avdGSR = np.average(diffGSR)
print "Average of derivate: ", avdGSR
ndiffGSR = []
Nndiff = 0.0
Ndiff = 0.0
for g in range(0, diffGSR.shape[0]):
	Ndiff += 1
	if diffGSR[g]<0:
		ndiffGSR.append(diffGSR[g])
		Nndiff += 1
decRate = np.average(ndiffGSR)
print "Average decrease rate: ", decRate
decProp = Nndiff/Ndiff
print "Proportion of negative derivates: ", decProp
# for local minima
x = np.random.random(12)
localm = argrelextrema(GSR, np.less_equal, order = 500)
Nlocalm = localm[0].shape[0]
print "Number of local minima: ", Nlocalm
