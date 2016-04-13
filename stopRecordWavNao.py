# -*- encoding: UTF-8 -*-

import sys
import time
from naoqi import ALProxy

def stopRecordWav():
    #record wav sound
    IP = "localhost"
    PORT = 9559
    
    print "stopping"

    try:
        tts = ALProxy("ALAudioDevice", IP, PORT)
        print "ok tts"
    except Exception,e:
        print "Could not create proxy to ALAudioDevice"
        print "Error was: ",e
        sys.exit(1)

    tts.stopMicrophonesRecording()
    print "Stopped recording..."
