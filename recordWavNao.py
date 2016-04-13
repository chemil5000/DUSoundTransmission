# -*- encoding: UTF-8 -*-

import sys
import time
from naoqi import ALProxy

def recordWav(input):
    #record wav sound
    IP = "192.168.0.100"
    PORT = 9559
    
    print "running"

    try:
        aur = ALProxy('ALAudioDevice', IP, PORT)
        print "ok audio dev"
    except Exception,e:
        print "Could not create proxy to ALAudioDevice"
        print "Error was: ",e
        sys.exit(1)


    print "start recording..."    
    aur.startMicrophonesRecording(input)
    time.sleep(5)
    aur.stopMicrophonesRecording()
    print "Stop recording..."
