# -*- coding: utf-8 -*-
import FFT
from matplotlib.pyplot import specgram
from sklearn.metrics import confusion_matrix
from sklearn.svm import LinearSVC
from sklearn.utils import resample
from matplotlib import pylab
import numpy as np

def normalisation(cm):
	new_cm = []
	for line in cm:
		new_array = []
		sum_val = 0
		for num in line:
			sum_val+=num
		print sum_val
		for num in line:
			new_array.append(float(num)/float(sum_val))
		new_cm.append(new_array)
	print(new_cm)
	return new_cm



def plot_confusion_matrix(cm,name_list,name,title):
	pylab.clf()
	pylab.matshow(cm,fignum=False,cmap='Blues',vmin=0,vmax=1.0)
	ax = pylab.axes()
	ax.set_xticks(range(len(name_list)))
	ax.set_xticklabels(name_list)
	ax.xaxis.set_ticks_position("bottom")
	ax.set_yticks(range(len(name_list)))
	ax.set_yticklabels(name_list)
	pylab.title(title)
	pylab.colorbar()
	pylab.grid(False)
	pylab.xlabel('Predict class')
	pylab.ylabel('True class')
	pylab.grid(False)
	pylab.show()

name_list = ["Uesaka_Sumire","Komatsu_Mikako","Okubo_Rumi","Takamori_Natsumi","Mikami_Shiori"]

x,y = FFT.read_fft(name_list)
svc = LinearSVC(C=1.0)
# x,y = resample(x,y,n_samples=len(y))
svc.fit(x[150:],y[150:])
prediction = svc.predict(x[:150])
# cm = confusion_matrix(y[:150],prediction)
# new_cm = normalisation(cm)


# test_name_list = ["Uesaka_Sumire_Anime","Komatsu_Mikako_Anime","Okubo_Rumi_Anime","Takamori_Natsumi_Anime","Mikami_Shiori_Anime"]
# test_x,test_y = FFT.read_fft(test_name_list)
# # prediction_anime = svc.predict(test_x)
# # cm_anime = confusion_matrix(test_y,prediction_anime)
# # new_cm_anime = normalisation(cm_anime)
# for t in test_x:
# 	print t
# plot_confusion_matrix(new_cm,name_list,"","Radio Voice")
# plot_confusion_matrix(new_cm_anime,name_list,"","Anime Voice")


