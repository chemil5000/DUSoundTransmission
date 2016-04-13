# -*- encoding: UTF-8 -*-

import sys
import time
from naoqi import ALProxy

def playWav(input):
    #play wav sound
    IP = "localhost"
    PORT = 9559
    try: 
        aup = ALProxy('ALAudioPlayer', IP, PORT) 
    except Exception,e:
        print "Could not create proxy to ALAudioPlayer"
        print "Error was: ",e
        sys.exit(1)
	    
    #Launchs the playing of a file on the left speaker to a volume of 50%
    aup.playFile('/home/nao/AudioTransm/' + input,1,0)
