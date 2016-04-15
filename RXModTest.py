import numpy as np
from numpy import (asarray, iscomplexobj, sinc)
import wave
import struct
import sys
import scipyWavRead as swr
import scipyHilbert as sh


#the following variables setup the system
Fc = 10000       #simulate a carrier frequency of
Fbit = 10      #simulated bitrate of data
Fdev = 5000      #frequency deviation, make higher than bitrate

A = 10           #transmitted signal amplitude
Fs = 48000      #sampling frequency for the simulator, must be higher than twice the carrier frequency


def rxDecode(wavFilePath):
    """
    Read Wav File
    """
    # Write a wave-file
    # sample rate, data
    rate, y = swr.read(wavFilePath)

    print 'mean', np.mean(y)
    print 'max', np.max(y)
    print 'min', np.min(y)

    """
    Differentiator
    """
    print 'Differentiating...'
    y_diff = np.diff(y,5)

    """
    Envelope detector
    """
    try:
        print 'Envelope...'
        #create an envelope detector
        y_env = np.abs(sh.hilbert(y_diff))
        y_filtered = y_env

        """
        slicer
        """
        print 'Slicing...'
        #calculate the mean of the signal
        mean = np.mean(y_filtered)
        #if the mean of the bit period is higher than the mean, the data is a 0
        rx_data = []
        sampled_signal = y_filtered[Fs/Fbit/2:len(y_filtered):Fs/Fbit]

        for bit in sampled_signal:
            if bit > mean:
                rx_data.append(0)
            else:
                rx_data.append(1)

        print rx_data
        return 'rx',rx_data
        print 'win?'
    except:
        print 'fail'