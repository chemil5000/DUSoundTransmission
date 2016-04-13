import numpy as np
import wave
import sys

spf = wave.open('testToneTX.wav','r')

#Extract Raw Audio from 1 Channel Wav File
signal = spf.readframes(-1)
#numpy returns an array on int16 from the string of signal
signal = np.fromstring(signal, 'Int16')
fs = spf.getframerate()
signalNorm = signal/np.amax(signal)
N = len(signal)
T = 1.0/fs

#Original tone second/frequncy
toneTime = .2
fftSampleFreq = 2 #samples per toneTime
fftSamplesInFrame = ((toneTime*fs)/fftSampleFreq)

def fftfreq(n,d):
    #from numpy
    val = 1.0 / (n * d)
    results = np.empty(n, int)
    N = (n-1)//2 + 1
    p1 = np.arange(0, N, dtype=int)
    results[:N] = p1
    p2 = np.arange(-(n//2), 0, dtype=int)
    results[N:] = p2
    return results * val

for toneBlock in range(0,int(N/fftSamplesInFrame)):
    print toneBlock
    #Compute the dominant frequency in that tone block
    startBlockFrame = toneBlock*fftSamplesInFrame
    yf = np.fft.fft(signalNorm[startBlockFrame:(startBlockFrame+fftSamplesInFrame-1)])   
    ind = np.argsort((2.0/N * np.abs(yf[:N/2])))[-4:]
    index = np.sort(ind,0)[1]
    print index    
    freq = fftfreq(int(fftSamplesInFrame-1),(T))
    print("frequency given", freq[index])



