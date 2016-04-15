import numpy as np
import matplotlib.pyplot as plt
#https://tomroelandts.com/articles/how-to-create-simple-band-pass-and-band-reject-filters

fs = 48000
LowHz  = 300
HighHz = 1300

fL = LowHz/fs  # Cutoff frequency as a fraction of the sampling rate (in (0, 0.5)).
fH = HighHz/fs  # Cutoff frequency as a fraction of the sampling rate (in (0, 0.5)).
b = 0.008  # Transition band, as a fraction of the sampling rate (in (0, 0.5)).

def noiseFilter(data_in):

	N = int(np.ceil((4 / b)))
	if not N % 2: N += 1  # Make sure that N is odd.
	n = np.arange(N)
	 
	# Compute a low-pass filter with cutoff frequency fH.
	hlpf = np.sinc(2 * fH * (n - (N - 1) / 2.))
	hlpf *= np.blackman(N)
	hlpf = hlpf / np.sum(hlpf)
	 
	# Compute a high-pass filter with cutoff frequency fL.
	hhpf = np.sinc(2 * fL * (n - (N - 1) / 2.))
	hhpf *= np.blackman(N)
	hhpf = hhpf / np.sum(hhpf)
	hhpf = -hhpf
	hhpf[(N - 1) / 2] += 1
	 
	# Convolve both filters.
	h = np.convolve(hlpf, hhpf)
	s = np.convolve(data_in, hlpf)

	fig, ax = plt.subplots()
	ax.plot(data_in)
	plt.show()
	fig1, ax1 = plt.subplots()
	ax1.plot(s)
	plt.show()
	return s




