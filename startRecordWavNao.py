# -*- encoding: UTF-8 -*-

import sys
import time
from naoqi import ALProxy

def startRecordWav():
    #record wav sound
    IP = "localhost"
    PORT = 9559
    
    print "starting to record"

    try:
        aur = ALProxy('ALAudioDevice', IP, PORT)
        print "ok audio dev"
    except Exception,e:
        print "Could not create proxy to ALAudioDevice"
        print "Error was: ",e
        sys.exit(1)

    print "start recording..."    
    aur.startMicrophonesRecording("/home/nao/AudioTransm/testToneTX.wav", "wav", 16000, (0,0,1,0))
   
