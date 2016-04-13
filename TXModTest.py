import sys
import struct
import numpy as np
from numpy.random import sample
import scipyWavWrite as sww


#the following variables setup the system
Fc = 10000       #simulate a carrier frequency of
Fbit = 100      #simulated bitrate of data
Fdev = 5000      #frequency deviation, make higher than bitrate
        #how many bits to send
A = 10           #transmitted signal amplitude
Fs = 48000      #sampling frequency for the simulator, must be higher than twice the carrier frequency
A_n = 3.0     #noise peak amplitude
    
"""
Data in
"""
def txMod(data_in):

    """
    #generate some random data for testing
    print "Generating data..."
    data_in = np.random.random_integers(0,1,N)
    """
    print data_in
    N=len(data_in)
    
   
    """
    VCO
    """
    print 'VCO...'
    #t = np.arange(0,np.float64(N)/np.float64(Fbit),1/np.float64(Fs), dtype=np.float)
    #extend the data_in to account for the bitrate and convert 0/1 to frequency
    m = np.zeros(0).astype(float)
    for bit in data_in:
        if bit == 0:
            m=np.hstack((m,np.multiply(np.ones(Fs/Fbit),Fc+Fdev)))
        else:
            m=np.hstack((m,np.multiply(np.ones(Fs/Fbit),Fc-Fdev)))
    #calculate the output of the VCO
    t=np.linspace(0,np.float(N)/np.float(Fbit),len(m))
    y=np.zeros(0)
    y=A * np.cos(2*np.pi*np.multiply(m,t))
    print "t", len(t)
    print "m", len(m)

    print 'Writing WAV file...'
    #scipy.io.wavfile.write('out.wav', Fs, y)
    sww.write('outRecX.wav', Fs, y)


