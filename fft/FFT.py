import scipy
from scipy import io
from scipy.io import wavfile
import glob
import numpy as np
import os

BASE_DIR = "./"

def create_fft(fn):
	sample_rate,X = io.wavfile.read(fn)
	fft_features = abs(scipy.fft(X)[:1000])
	base_fn,ext = os.path.splitext(fn)
	data_fn = base_fn + ".fft"
	np.save(data_fn,fft_features)
	print("Written %s" % data_fn)


def read_fft(genre_list,base_dir=BASE_DIR):
	x = []
	y = []
	for label,genre in enumerate(genre_list):
		genre_dir = os.path.join(base_dir,genre,"*.fft.npy")
		file_list = glob.glob(genre_dir)
		for fn in file_list:
			fft_features = np.load(fn)
			x.append(fft_features[:1000])
			y.append(label)
	return np.array(x),np.array(y)