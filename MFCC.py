from scikits.talkbox.features import mfcc
import scipy
from scipy import io
from scipy.io import wavfile
import glob
import numpy as np
import os

BASE_DIRE = "./"
def write_ceps(ceps,fn):
	base_fn,ext = os.path.splitext(fn)
	data_fn = base_fn + ".ceps"
	np.save(data_fn,ceps)
	print("Written %s" % data_fn)

def create_ceps(fn):
	sample_rate,X = io.wavfile.read(fn)
	ceps,mspec,spec = mfcc(X)
	isNan = False
	for num in ceps:
		if np.isnan(num[1]):
			isNan = True

	if isNan == False:
		write_ceps(ceps,fn)
	else:
		print("")


def read_ceps(name_list,base_dir = BASE_DIRE):
	X,y = [],[]
	for label,name in enumerate(name_list):
		for fn in glob.glob(os.path.join(base_dir,name,"*.ceps.npy")):
			ceps = np.load(fn)
			num_ceps = len(ceps)
			X.append(np.mean(ceps[:],axis=0))
			y.append(label)
	return np.array(X),np.array(y)
