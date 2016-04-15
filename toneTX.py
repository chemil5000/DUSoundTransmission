#!/usr/bin/env python
import sys
import wave
import math
import time
import struct
import random
import argparse
import numpy as np
from itertools import *
import symbolPrep as symp

def grouper(n, iterable, fillvalue=None):
    "grouper(3, 'ABCDEFG', 'x') --> ABC DEF Gxx"
    args = [iter(iterable)] * n
    return izip_longest(fillvalue=fillvalue, *args)

def sine_wave(frequency=440.0, framerate=48000, amplitude=1):
    # Generate a sine wave at a given frequency of infinite length.
    period = int(framerate / frequency)
    if amplitude > 1.0: amplitude = 1.0
    if amplitude < 0.0: amplitude = 0.0
    lookup_table = [float(amplitude) * math.sin(2.0*math.pi*float(frequency)*(float(i%period)/float(framerate))) for i in xrange(period)]
    return (lookup_table[i%period] for i in count(0))

def compute_samples(channels, nsamples=None):
    # create a generator which computes the samples.
    return islice(izip(*(imap(sum, izip(*channel)) for channel in channels)), nsamples)

def write_wavefile(w, filename, samples, nframes=None, nchannels=2, sampwidth=2, framerate=44100, bufsize=2048):
    "Write samples to a wavefile."
    max_amplitude = float(int((2 ** (sampwidth * 8)) / 2) - 1)
    # split the samples into chunks (to reduce memory consumption and improve performance)
    for chunk in grouper(bufsize, samples):
        frames = ''.join(''.join(struct.pack('h', int(max_amplitude * sample)) for sample in channels) for channels in chunk if channels is not None)
        w.writeframesraw(frames)

    return filename


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('filename', help="The file to generate.")
    args = parser.parse_args()

    #data for testing
    N=100
    data_in = np.random.random_integers(0,1,N)
    symbolArray = symp.symbolConverter(data_in)


    #Transmission Parameters
    toneBandwidth = 20 #Hz
    minTone = 400
    symbolNumber = 33
    toneTime = 0.15 #seconds
    rate = 48000
    #frequency to stop and start reading data
    startTone = 360 #Hz
    stopTone = 1200 #Hz

 
    # write the samples to a file
    if args.filename == '-':
        filename = sys.stdout
    else:
        filename = args.filename

    w = wave.open(filename, 'w')
    w.setparams((1, 2, rate, rate * toneTime, 'NONE', 'not compressed'))
    t0= time.time()
    tone = ((sine_wave(startTone, 48000, 1),) for i in range(1))
    t1= time.time()
    print 'time for tone: ', t1-t0
    t0= time.time()
    samples = compute_samples(tone, 48000 * toneTime)
    t1= time.time()
    print 'time for samples: ', t1-t0
    t0= time.time()
    write_wavefile(w, filename, samples, 48000 * toneTime, 1, 16 / 8, 48000)
    t1= time.time()
    print 'time for write: ', t1-t0 

   
    for symbol in symbolArray:
        #after testing.. it will probably be faster to premake the tones and then call them? 
        #what is the size of the message necessay to say that you probably will need all the tones?...
        tone = ((sine_wave(minTone+(int(symbol)*20), 48000, 1),) for i in range(1))
        samples = compute_samples(tone, 48000 * toneTime)
        write_wavefile(w, filename, samples, 48000 * toneTime, 1, 16 / 8, 48000)

    #cheesy stop tone
    tone = ((sine_wave(stopTone, 48000, 1),) for i in range(1))
    samples = compute_samples(tone, 48000 * toneTime)
    write_wavefile(w, filename, samples, 48000 * toneTime, 1, 16 / 8, 48000)
    w.close()

if __name__ == "__main__":
    main()