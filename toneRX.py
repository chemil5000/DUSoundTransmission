import numpy as np
import wave
import math
import scipyWavRead as swr


"""
Read Wav File
"""
rate, y = swr.read('toneTest2.wav')
fs=rate
"""
#Use when testing on a mono channelsignal = y
# sample rate, data
#####
"""

#Use when testing on the robot
#Robot records 4 channels so select only one of the channels
y_OneChann = y[:,0]
signal = y_OneChann
#####


signalNorm = signal/np.amax(signal)
N = len(signal)
T = 1.0/fs

#frequency to stop and start reading data
startTone = 360 #Hz
stopTone = 1200 #Hz

#Transmission Parameters tone second/frequncy
toneBandwidth = 20 #Hz
symbolNumber = 32 #Hz
minTone = 400
maxTone = minTone+(toneBandwidth*symbolNumber)
toneTime = 0.15 #seconds
fftSampleFreq = 1 #samples per toneTime
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

def main():
    decode = False
    rx_data = []
    for toneSymbol in range(0,int(N/fftSamplesInFrame)):
        #print ('time', toneSymbol*toneTime)
        #Compute the dominant frequency in that tone block
        startBlockFrame = toneSymbol*fftSamplesInFrame
        yf = np.fft.fft(signalNorm[startBlockFrame:(startBlockFrame+fftSamplesInFrame-1)])   
        ind = np.argsort((2.0/N * np.abs(yf[:N/2])))[-4:]
        index = np.sort(ind,0)[1] 

        freq = fftfreq(int(fftSamplesInFrame-1),(T))
        #print("freq", freq[index], ind)
       
        if (freq[index] < (startTone+(toneBandwidth/2.0))) and (freq[index] > (startTone-(toneBandwidth/2.0))):
            print('Start Tone Found')
            #start decoding data
            decode = True

        if (freq[index] < (stopTone+(toneBandwidth/2.0))) and (freq[index] > (stopTone-(toneBandwidth/2.0))):
            print('Stop Tone Found')
            #return the data
            decode = False
            #can we some how actively read in the data and tell the robot to stop listening?
            print rx_data
            return rx_data
            break

        if decode:
            if (freq[index]>minTone) and (freq[index]<maxTone):
                symbol = int(math.ceil(((freq[index]-minTone)/toneBandwidth)+.5)-1)
                print "freq", freq[index], '    decodedSymbol', symbol             
                #take advantage of being able to multisample each tone to verify the toneTime?
                rx_data.append(symbol)
            


if __name__ == "__main__":
    main()

